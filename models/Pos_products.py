import random
import re
from odoo import api, models,fields
from odoo.exceptions import ValidationError
from odoo.osv.expression import get_unaccent_wrapper

#inventory
class PoS_products(models.Model):
    _name="pos.products"
    _inherit = "res.partner"


    name=fields.Char("Product Name")
    # image = fields.Binary("Product Image")
    # image_1920
    list_price= fields.Float("Price")
    qut= fields.Integer("Quntity")
    sku=fields.Char("Product ID (SKU)")
    discount= fields.Float("% Discount",digits=(4,2))
    
    # @api.depends('discount')
    # def cal_discount(self):
    #     for rec in self:
    #         dic_amount= (rec.discount/100) * rec.list_price
    #         rec.price_af_dis= rec.list_price-dic_amount
    #     # self.price_af_dis=rec.price_af_dis
    
    # code to remove inherit error
    def _compute_partner_share(self):
        pass
    def _compute_commercial_partner(self):
        pass
    channel_ids = fields.Integer("Test")

    def default_get(self, fields_list):
        return super().default_get(fields_list)

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        self = self.with_user(name_get_uid or self.env.uid)
        # as the implementation is in SQL, we force the recompute of fields if necessary
        self.recompute(['display_name'])
        self.flush()
        if args is None:
            args = []
        order_by_rank = self.env.context.get('pos_products_search_mode')
        if (name or order_by_rank) and operator in ('=', 'ilike', '=ilike', 'like', '=like'):
            self.check_access_rights('read')
            where_query = self._where_calc(args)
            self._apply_ir_rules(where_query, 'read')
            from_clause, where_clause, where_clause_params = where_query.get_sql()
            from_str = from_clause if from_clause else 'pos_products'
            where_str = where_clause and (" WHERE %s AND " % where_clause) or ' WHERE '

            # search on the name of the contacts and of its company
            search_name = name
            if operator in ('ilike', 'like'):
                search_name = '%%%s%%' % name
            if operator in ('=ilike', '=like'):
                operator = operator[1:]

            unaccent = get_unaccent_wrapper(self.env.cr)

            fields = self._get_name_search_order_by_fields()

            query = """SELECT pos_products.id
                         FROM {from_str}
                      {where} ({email} {operator} {percent}
                           OR {display_name} {operator} {percent}
                           OR {reference} {operator} {percent}
                           OR {vat} {operator} {percent})
                           -- don't panic, trust postgres bitmap
                     ORDER BY {fields} {display_name} {operator} {percent} desc,
                              {display_name}
                    """.format(from_str=from_str,
                               fields=fields,
                               where=where_str,
                               operator=operator,
                               email=unaccent('pos_products.email'),
                               display_name=unaccent('pos_products.display_name'),
                               reference=unaccent('pos_products.ref'),
                               percent=unaccent('%s'),
                               vat=unaccent('pos_products.vat'),)

            where_clause_params += [search_name]*3  # for email / display_name, reference
            where_clause_params += [re.sub(r'[^a-zA-Z0-9\-\.]+', '', search_name) or None]  # for vat
            where_clause_params += [search_name]  # for order by
            if limit:
                query += ' limit %s'
                where_clause_params.append(limit)
            self.env.cr.execute(query, where_clause_params)
            return [row[0] for row in self.env.cr.fetchall()]

        return super(PoS_products, self)._name_search(name, args, operator=operator, limit=limit, name_get_uid=name_get_uid)

    price_af_dis= fields.Float("Price After Discount") #,compute=cal_discount,store=True

    @api.model
    def create(self, vals_list):
        nxt_ran_int= random.randint(10,99)
        res= super(PoS_products,self).create(vals_list)
        fst_let= res.name.split()
        # fst_let=fst_let.upper()
        res.sku=f"{fst_let[0]}_{nxt_ran_int}-{res.id}"
        res.name=f"[{res.sku}] {res.name}"

        dic_amount= (res.discount/100) * res.list_price
        res.price_af_dis= res.list_price-dic_amount
        return res

class PoS_products_data(models.Model):
    _name='pos.products_data'
    name=fields.Many2one('pos.products',string="Product Name")
    price= fields.Float("Price",related='name.list_price')
    discount= fields.Float("% Discount",digits=(4,2),related='name.discount')
    qut= fields.Integer("Quntity")

    @api.depends('price','qut')
    def _cal_total(self):
        for rec in self:
            rec.amount= rec.name.price_af_dis* rec.qut
            

    amount=fields.Float("Total",compute=_cal_total,store=True)

    # to update stock
    @api.model
    def create(self, vals_list):
        res= super(PoS_products_data,self).create(vals_list)
        if res.name.qut<res.qut:
            raise ValidationError(f"{res.name.name} is Out off Stock")
        else:
            res.name.qut-=res.qut  
        return res

    product_id= fields.Many2one(comodel_name="pos.checkout")


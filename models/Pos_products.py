import random
from odoo import api, models,fields
from odoo.exceptions import ValidationError

#inventory
class PoS_products(models.Model):
    _name="pos.products"
    name=fields.Char("Product Name")
    pro_image= fields.Binary("Product Image")
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


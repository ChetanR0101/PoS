import random
from odoo import api, models,fields

#inventory
class PoS_products(models.Model):
    _name="pos.products"
    name=fields.Char("Product Name")
    image= fields.Binary("Product Image")
    price= fields.Float("Price")
    qut= fields.Integer("Quntity")
    sku=fields.Char("Product ID (SKU)")
    discount= fields.Float("% Discount",digits=(4,2))
    

    @api.model
    def create(self, vals_list):
        nxt_ran_int= random.randint(10,99)
        res= super(PoS_products,self).create(vals_list)
        fst_let= res.name[0:4]
        fst_let=fst_let.upper()
        res.sku=f"{fst_let}_{nxt_ran_int}-{res.id}"
        res.name=f"[{res.sku}] {res.name}"
        return res

class PoS_products_data(models.Model):
    _name='pos.products_data'
    name=fields.Many2one('pos.products',string="Product Name")
    price= fields.Float("Price",related='name.price')
    discount= fields.Float("% Discount",digits=(4,2),related='name.discount')
    qut= fields.Integer("Quntity")

    @api.depends('price','qut')
    def _cal_total(self):
        for rec in self:
            rec.amount= rec.price* rec.qut
            

    amount=fields.Float("Total",compute=_cal_total,store=True)

    # to update stock
    @api.model
    def create(self, vals_list):
        res= super(PoS_products_data,self).create(vals_list)
        res.name.qut-=res.qut  
        return res

    product_id= fields.Many2one(comodel_name="pos.checkout")


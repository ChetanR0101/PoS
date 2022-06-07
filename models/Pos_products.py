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
    
    # To generate tanker record id
    @api.model
    def create(self, vals_list):
        nxt_ran_int= random.randint(10,99)
        res= super(PoS_products,self).create(vals_list)
        fst_let= res.name[0:3]
        fst_let.upper()
        res.sku=fst_let+str(nxt_ran_int)+str(res.id)
        res.name=f"[{res.sku}] {res.name}"
        return res



from odoo import models,fields

#inventory
class PoS_inventory(models.Model):
    _name="pos.inventory"

    name=fields.Char("Product Name")
    
    qut= fields.Integer("Quntity")


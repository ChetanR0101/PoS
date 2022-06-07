from odoo import models,fields, api

#inventory test
class PoS_inventory(models.Model):
    _name="pos.inventory"

    name=fields.Char("Product Name")
    qut= fields.Integer("Quntity")

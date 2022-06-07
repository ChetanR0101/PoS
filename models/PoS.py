from odoo import models,fields, api

#inventory
class PoS_inventory(models.Model):
    _name="pos.inventory"

    name=fields.Char("Product Name")
    qut= fields.Integer("Quntity")

class PoS_checkout(models.Model):
    _name="pos.checkout"

    name= fields.Char("Customer Name")
    date=fields.Date("Date")
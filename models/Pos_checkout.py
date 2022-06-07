from odoo import models,fields


# checkout
class PoS_checkout(models.Model):
    _name="pos.checkout"

    name = fields.Char(string="Customer Name")
    date=fields.Date("Date")
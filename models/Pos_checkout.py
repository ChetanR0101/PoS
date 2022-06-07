from odoo import models,fields


# checkout
class PoS_checkout(models.Model):
    _name="pos.checkout"

    name= fields.Char(string="Customer Name")
    date=fields.Date("Date")

    product_ids= fields.One2many(comodel_name="pos.products_data",inverse_name="product_id")

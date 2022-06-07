from odoo import models,fields

#inventory
class PoS_checkin(models.Model):
    _name="pos.checkin"
    name=fields.Many2one(string="Product Name",comodel_name="pos.products")
    in_qut= fields.Integer("Quntity")

    discount= fields.Float("% Discount",digits=(4,2))

    


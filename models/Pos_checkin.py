from datetime import datetime
from odoo import api, models,fields

#inventory
class PoS_checkin(models.Model):
    _name="pos.checkin"
    name=fields.Many2one(string="Product Name",comodel_name="pos.products")
    date= fields.Date("Date",default=datetime.today())
    in_qut= fields.Integer("Quntity")
    
    

    @api.model
    def create(self, vals_list):
        res=super(PoS_checkin,self).create(vals_list)
        res.name.qut += res.in_qut # to add stock
        print("Val>>>> ", vals_list)
        return res

    


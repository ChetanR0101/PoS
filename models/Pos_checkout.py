from odoo import api, models,fields


# checkout
class PoS_checkout(models.Model):
    _name="pos.checkout"

    name= fields.Char(string="Customer Name")
    date=fields.Date("Date")

    @api.depends('product_ids.amount')
    @api.onchange('product_ids')
    def cal_grand_sum(self):
        self.grand_sum=0
        for rec in self.product_ids:
            self.grand_sum += rec.amount

    grand_sum=fields.Float("Grand Sum",compute=cal_grand_sum,store=True)

    invoice_id= fields.Char("Invoice Id")
    @api.model
    def create(self, vals_list):
        res= super(PoS_checkout,self).create(vals_list)
        res.invoice_id=f"{res.date}-{res.id}" 
        return res


    product_ids= fields.One2many(comodel_name="pos.products_data",inverse_name="product_id")

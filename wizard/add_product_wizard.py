from odoo import models, fields


class Add(models.TransientModel):
    _name = 'add.add'
    _description = 'add_wizard'

product_set_id = fields.Many2one('product.set', string='Product Set', required=True, ondelete='cascade')
product_id = fields.Many2one('product.product', string='Product')

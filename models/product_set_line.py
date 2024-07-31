from odoo import models, fields , api


class Lines(models.Model):
    _name = 'product.set.line'
    _description = 'Line Description'

    product_set_id = fields.Many2one('product.set', string='Product Set', required=True, ondelete='cascade')
    product_id = fields.Many2one('product.product', string='Product')
    quantity_prod = fields.Float(string='Quantity', store=True , default=0)
    unit_id = fields.Many2one('uom.uom', string='Unit of Measure')
    reference_prod = fields.Char(string='Reference')

    # @api.onchange('quantity')
    # def _onchange_quantity(self):
    #     if self.quantity and self.lines:
    #         original_quantity = self._origin.quantity if self._origin.quantity else 1
    #         original_quantity_prod =line._origin.quantity_prod if line._origin.quantity_prod else 1
    #         if original_quantity and original_quantity_prod:
    #             # percentage_change = self.quantity / original_quantity
    #             for line in self.lines:
    #                 line.quantity_prod = line.quantity_prod * (original_quantity/original_quantity_prod)


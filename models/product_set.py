from odoo import models, fields , api
import logging

_logger = logging.getLogger(__name__)


class Sets(models.Model):
    _name = 'product.set'
    _description = 'Set Description'

    name = fields.Char(string='Name', required=True)
    lines = fields.One2many('product.set.line' , 'product_set_id' , string='Lines')
    reference = fields.Char(string="Reference")
    quantity = fields.Float(string="Quantity" , default=0)

    # @api.onchange('quantity')
    # def _onchange_quantity(self):
    #     if self.quantity and self.lines:
    #         original_quantity = self._origin.quantity
    #
    #         if original_quantity :
    #
    #             for line in self.lines:
    #
    #
    #                 line.quantity_prod = line.quantity_prod * (self.quantity/original_quantity)


    @api.onchange('quantity')
    def _onchange_quantity(self):
        _logger.info("Onchange triggered for quantity")
        if self.quantity and self.lines:
            original_quantity = self._origin.quantity if self._origin else 1
            _logger.info(f"Original Quantity: {original_quantity}, New Quantity: {self.quantity}")

            if original_quantity:
                for line in self.lines:
                    original_quantity_prod = line._origin.quantity_prod if line._origin else 1
                    _logger.info(f"Line Original Quantity Prod: {original_quantity_prod}")
                    line.quantity_prod = original_quantity_prod * (self.quantity / original_quantity)
                    _logger.info(f"Updated Line Quantity Prod: {line.quantity_prod}")


    def action_wizard(self) :
        return {
            'name': ('Add'),
            'view_mode': 'form',
            'res_model': 'add.add',
            'type': 'ir.actions.act_window',
            'target': 'new',
        }




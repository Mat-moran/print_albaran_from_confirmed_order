from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"



    def get_state_picking(self):
        """
        Get picking state of the order. If ordered qtys are equal to delivered
        qtys done is True

        """

        uom_qtys = self.order_line.mapped('product_uom_qty')
        del_qtys = self.order_line.mapped('qty_delivered')

        done = uom_qtys == del_qtys


        return done


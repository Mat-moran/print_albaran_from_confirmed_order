from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"


    def get_state_picking(self):

        state = 'done'

        return state


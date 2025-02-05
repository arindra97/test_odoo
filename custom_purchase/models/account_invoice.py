# -*- coding: utf-8 -*-
from itertools import groupby

from odoo import api, fields, models, _

class AccountMove(models.Model):
    _inherit = ['account.move']
    _description = "Invoice"

    purchase_order_news_id = fields.Many2one('purchase.order.news', string='Purchase Order News')

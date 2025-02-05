# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class PurchaseOrder(models.Model):
    _inherit = ["purchase.order"]
    _description = "Purchase Order"

    purchase_order_news_ids = fields.One2many('purchase.order.news', 'purchase_order_id', string="Berita Acara") 
    po_news_count = fields.Integer(compute="_compute_po_news", string='PO News Count', copy=False, default=0, store=True)

    def action_create_purchase_order_news(self):
        """This function returns an action that display existing po news of
        given purchase order news ids. 
        """
        try:
            po_news_form_id = self.env['ir.model.data']._xmlid_lookup('custom_purchase.purchase_order_news_view_form')[2]
        except ValueError:
            po_news_form_id = False
        ctx = dict(self.env.context or {})
        ctx.update({
            'default_purchase_order_id': self.id,
            'default_partner_id': self.partner_id.id,
            'default_state': 'draft'
        })

        return{
            'name': "Berita Acara",
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': "purchase.order.news",
            'views': [(po_news_form_id, 'form')],
            'view_id': po_news_form_id,
            'target': 'new',
            'context': ctx,
        }
    
    @api.depends('purchase_order_news_ids')
    def _compute_po_news(self):
        for order in self:
            order.po_news_count = len(order.purchase_order_news_ids)

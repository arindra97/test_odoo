# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError

class PurchaseOrderNews(models.Model):
    _name = "purchase.order.news"
    _description = "Purchase Order News"

    approve_employee_id = fields.Many2one('hr.employee', string='Employee')
    delivery_date = fields.Date(string='Delivery Date')
    name = fields.Char("No Doc")
    news_information = fields.Text('News Information')
    origin = fields.Char("Source Document")
    partner_id = fields.Many2one('res.partner', string='Partner')
    purchase_order_id = fields.Many2one('purchase.order', string='Purchase Order ID')
    invoice_po_news_id = fields.Many2one('account.move', string='ID Invoice BA')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submit', 'Submit'),
        ('approve', 'Approve'),
        ('done', 'Done')
    ], string='Status', readonly=True, index=True, copy=False, default='draft', tracking=True)
    
    @api.model
    def create(self, vals):
        if vals.get('name', '/') == '/':
            vals['name'] = self.env['ir.sequence'].next_by_code('purchase.order.news') or '/'
        return super(PurchaseOrderNews, self).create(vals)
        
    def button_draft(self):
        self.write({'state': 'draft'})

    def button_submit(self):
        self.write({'state': 'submit'})

    def button_approve(self):
        # 1. Perform any pre-approval logic (e.g., state changes, validations)
        if self.state == 'done':
            raise UserError(_("This Berita Acara is already marked as Done."))

        self.write({'state': 'approve'})

        # 2. Create the Supplier Invoice (account.move)
        invoice = self.env['account.move'].create({
            'move_type': 'in_invoice',  # Supplier invoice
            'partner_id': self.partner_id.id,  # From the BA
            'purchase_order_news_id': self.id,  # Link to the BA
            'payment_reference': self.name,  # BA number as invoice reference
            'invoice_date': fields.Date.today(),  # Set invoice date
        })

        self.write({'state': 'done','invoice_po_news_id':invoice.id})

        # 3. return the invoice to the user
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'account.move',
            'res_id': invoice.id,
            'view_mode': 'form',
            'target': 'new',  # Open in a new window/tab
        }

    def button_done(self):
        self.write({'state': 'done'})

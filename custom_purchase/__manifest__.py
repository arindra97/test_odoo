# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Custom Purchase',
    'version': '1.0',
    'author': 'Muhammad Arindra Khoiru Syawal',
    'category': 'Inventory/Purchase',
    'sequence': 35,
    'summary': 'Custom Purchase orders with order news',
    'description': "",
    'website': '#',
    'depends': ['purchase'],
    'data': [
        'data/purchase_sequence.xml',
        'security/purchase_security.xml',
        'security/ir.model.access.csv',

        'views/purchase_views.xml',
        'views/purchase_order_news_views.xml',
        
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'assets': {
        'web.assets_backend': [
        ],
        'web.assets_frontend': [
        ],
        'web.assets_qweb': [
        ],
    },
}

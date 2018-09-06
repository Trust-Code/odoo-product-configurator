# -*- coding: utf-8 -*-
{
    'name': 'Product Configurator Wizard for Stock',
    'version': '10.0.1.0.0',
    'category': 'Generic Modules/Base',
    'summary': 'Back-end Product Configurator',
    'author': 'Trustcode',
    'license': 'AGPL-3',
    'website': 'http://www.trustcode.com.br',
    'depends': ['stock', 'product_configurator_wizard'],
    "data": [
        'views/stock_picking.xml',
    ],
    'images': [
        'static/description/cover.png'
    ],
    'installable': True,
    'auto_install': False,
}

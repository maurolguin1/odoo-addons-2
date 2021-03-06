# -*- coding: utf-8 -*-
# © 2012-2014 Guewen Baconnier (Camptocamp SA)
# © 2015 Roberto Lizana (Trey)
# © 2016 Pedro M. Baeza
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Multiple Barcode on products',
    'version': '9.0.0.0.0',
    'license': 'AGPL-3',
    'author': "jeo Software",
    'category': 'Product Management',
    'depends': ['product'],
    'website': 'http://jeosoft.com.ar',
    'data': [
        'views/product_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
}

# -*- coding: utf-8 -*-
{
    'name': "my_custom_app",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'point_of_sale', 'sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/pos_order_views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'my_custom_app/static/src/scss/my_custom_app.scss',
        ],
        'point_of_sale._assets_pos': [
            'my_custom_app/static/src/js/pos_custom_screen.js',
            'my_custom_app/static/src/scss/pos_custom.scss',
            'my_custom_app/static/src/xml/pos_templates.xml',
        ],
    },
}

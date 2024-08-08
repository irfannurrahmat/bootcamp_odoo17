# -*- coding: utf-8 -*-
{
    'name': "Odoo Training Bootcamp",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "Irfan N",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock', 'sale_management', 'mail'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/sequence_data.xml',
        'data/scheduler_data.xml',
        'data/data.xml',
        'wizard/training_wizard_views.xml',
        'report/report_action.xml',
        'report/report_training_session.xml',
        'views/menu_item.xml',
        'views/training_views.xml',
        'views/partner_views.xml',
        
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}


# -*- coding: utf-8 -*-
{

    'name': "To-do Application",

    'summary': """
        Manage Your Personal To-Do
        """,

    'description': """
        For Learning Purposes
    """,

    'author': "Dan Mutwiri FBI",
    'website': "http://www.FBI_KENIA.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/.xml', 
        # 'views/.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
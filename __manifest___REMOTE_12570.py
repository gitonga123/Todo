# -*- coding: utf-8 -*-
{
    'name': "To-Do Application",

    'summary': """
            Manage Your Personal To-DO Tasks.
        """,

    'description': """
        Manage Your Personal To-Do Tasks Everyday and Everywhere and Anyhow.
    """,

    'author': "Learning Odoo",
    'website': "http://www.otbafrica.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'security/todo_access_rules.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
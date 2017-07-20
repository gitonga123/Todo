# -*- coding: utf-8 -*-
{
<<<<<<< HEAD
    'name': "To-do Application",

    'summary': """
        Manage Your Personal To-Do
        """,

    'description': """
        For Learning Purposes
    """,

    'author': "Dan Mutwiri FBI",
    'website': "http://www.FBI_KENIA.com",
=======
    'name': "To-Do Application",

    'summary': """
            Manage Your Personal To-DO Tasks.
        """,

    'description': """
        Manage Your Personal To-Do Tasks Everyday and Everywhere and Anyhow.
    """,

    'author': "Learning Odoo",
    'website': "http://www.otbafrica.com",
>>>>>>> c7efeb3aa008d20d82f33b8f02a31a9ab9391f84

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
<<<<<<< HEAD
        # 'security/ir.model.access.csv',
        'views/.xml', 
        'views/.xml',
=======
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'security/todo_access_rules.xml'
>>>>>>> c7efeb3aa008d20d82f33b8f02a31a9ab9391f84
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
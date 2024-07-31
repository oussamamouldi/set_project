# {
#     'name': "set_project",
#
#     'summary': """
#     sets in module sales
# """,
#
#     'description': """sets in module sales""",
#
#     'author': "Mouldi Oussama",
#     'website': "",
#
#     'sequence':  15,
#     'category': '',
#     'version': '17.0.0.1.0',
#
#
#     'depends': ['base'],
#
#
#     'data': [
#         'security/ir.model.access.csv',
#         'views/Sets.xml',
#
#     ],
#     'installable': True,
#     'application' : True ,
#     'license' : 'LGPL-3',
# }
{
    'name': "Product Set Management",
    'summary': "Manage product sets and their lines",
    'description': """
        This module addities and units of measure.
    """,
    'author': "Mouldi Oussama",
    'website': "",

    'category': 'Sales',
    'version': '17.0.0.1.0',

    'depends': ['base','product','uom'],

    'data': [
        'security/ir.model.access.csv',
        'views/Sets.xml',
        'views/product_line.xml',
        'views/add_product_wizard_view.xml',
    ],

    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}

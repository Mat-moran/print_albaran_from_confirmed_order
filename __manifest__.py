# -*- coding: utf-8 -*-
{
    'name': "print_albaran_from_confirmedOrder",

    'summary': """
        Módulo creado para poder imprimir un albarán desde la ventana de pedidos.""",

    'description': """
        Módulo creado para poder imprimir un albarán desde la ventana de pedidos.
    """,

    'author': "Amadeo Morán Guerrero",
    'website': "http://www.davidmoran.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '13.0.0.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base','stock','mrp','website','sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'reports/report_albaran.xml',
    ],
    "application":False,
    "installable":True,
}

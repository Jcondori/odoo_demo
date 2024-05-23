# -*- coding: utf-8 -*-
{
    'name': "Odoo Demo",

    'summary': """
        Esto es un resumen""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Customizations',
    'version': '16.0.0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'account',
        'account_reports',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/res.partner.category.csv',
        'data/res_partner_category_data.xml',
        'views/cita_medica_views.xml',
        'views/templates.xml',
        'views/res_partner_views.xml',
        'views/report_cita.xml',
        'views/odoo_demo_report.xml',
        'wizards/cita_medica_wizard_views.xml',
        'report/cita_medica_doctor_report_views.xml',
        'report/cita_medica_doctor_excel_report_views.xml',
        'report/cita_medica_report_handler_views.xml',
    ],
    # # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
    'license': 'LGPL-3',
}

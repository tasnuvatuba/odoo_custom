# __manifest__.py
{
    'name': 'Employee NOC Template Management',
    'version': '1.0',
    'category': 'Human Resources',
    'summary': 'Module to manage and generate NOC certificates for employees',
    'description': """
        This module allows the creation and management of NOC (No Objection Certificate) templates
        for employees in the HR module. Users can select an employee, auto-populate details, 
        and generate a printable NOC certificate.
    """,
    'license': 'LGPL-3',
    'depends': ['base', 'hr'],
    'assets': {
        'web.assets_common': [
            'hr_templates/static/src/css/bg.css',  # Include your CSS file
        ],
    },
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',

        'views/employee_view.xml',
        'views/noc_form.xml',          # Form and tree views for NOC template model
        'views/menu_items.xml',

        'reports/noc_certificate_template.xml'  # QWeb template for the printable NOC report
    ],


    'installable': True,
    'application': False,
    'auto_install': False,
}

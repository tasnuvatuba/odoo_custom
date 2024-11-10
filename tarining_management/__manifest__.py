{
    "name": "Training Management System",
    "version": "1.0",
    "description": """
        A simple Training Management System streamlines the planning, delivery, 
        and tracking of training programs to enhance employee skills and performance.
    """,
    "depends": ["base"],
    "data": [
        'security/ir.model.access.csv',

        'views/training_session_view.xml',
        'views/menu_items.xml'
    ],
    "demo": [
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3"
}

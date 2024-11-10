{
    "name": "Real Estate Ads",
    "version": "1.0",
    "description": """
        Real Estate module to show available properties
    """,
    "Category": "Sales",
    "depends": ["base", "mail"],
    "data": [
        'security/ir.model.access.csv',
        'security/res_groups.xml',
        'security/model_access.xml',
        'security/ir_rule.xml',

        'views/property_view.xml',
        'views/property_type_view.xml',
        'views/property_tag_view.xml',
        'views/property_offer_view.xml',
        'views/menu_items.xml',

        #data files
        #'data/property_type.xml'
        'data/estate.property.type.csv', #csv file name should definitely follow this structure
        
        #report
        'report/report_template.xml',
        'report/property_report.xml'
    ],
    "demo": [
        'demo/property_tag.xml'
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3"
}

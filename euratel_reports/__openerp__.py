{
    'name': 'EuraTel Reports',
    'category': 'Report',
    'summary': 'Reports for EuraTel GmbH',
    'version': '1.0',
    'description': """
Reports for Euratel GmbH
        """,
    'author': 'artmin IT-Dienstleistungen',
    'depends': ['sale'],
    'data': [
        'views/euratel_layout.xml',
        'views/euratel_invoice.xml',
        'views/res_company_view.xml',
    ],
    'installable': True,
    'auto-install' : False,
}

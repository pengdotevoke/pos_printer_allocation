{
    'name': 'POS Printer Allocation',
    'version': '1.0',
    'category': 'Point of Sale',
    'summary': 'Allocate print jobs between printers based on 60%-40% logic',
    'author': 'James Oginga',
    'depends': ['point_of_sale'],
    'data': [
    'security/ir.model.access.csv',
    'views/printer_allocation_views.xml',
     ],
    'assets': {
        'point_of_sale.assets': [
            'pos_printer_allocation/static/src/js/pos_printer_allocation.js',
        ],
    },
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}

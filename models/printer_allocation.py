from odoo import models, fields

class PrinterAllocation(models.Model):
    _name = 'printer.allocation'
    _description = 'POS Printer Allocation'

    printer_a = fields.Char(string="Printer A", required=True)
    printer_b = fields.Char(string="Printer B", required=True)
    printer_a_count = fields.Integer(string="Printer A Count", default=0)
    printer_b_count = fields.Integer(string="Printer B Count", default=0)
    total_jobs = fields.Integer(string="Total Jobs", default=0)

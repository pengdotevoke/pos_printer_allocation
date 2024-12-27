from odoo import http
from odoo.http import request

class POSPrinterAllocation(http.Controller):

    @http.route('/pos/print_receipt', type='json', auth='user')
    def print_receipt(self, order_id):
        """Allocate receipt printing between printers."""
        allocation = request.env['printer.allocation'].sudo().search([], limit=1)
        if not allocation:
            return {"error": "Printer allocation settings not configured."}

        # Simulate allocation logic
        allocation.total_jobs += 1
        a_quota = int(allocation.total_jobs * 0.6)
        b_quota = allocation.total_jobs - a_quota

        if allocation.printer_a_count < a_quota:
            printer_name = allocation.printer_a
            allocation.printer_a_count += 1
        else:
            printer_name = allocation.printer_b
            allocation.printer_b_count += 1

        allocation.write({
            "printer_a_count": allocation.printer_a_count,
            "printer_b_count": allocation.printer_b_count,
            "total_jobs": allocation.total_jobs,
        })

        # Simulate a print action
        print(f"Printing order {order_id} to {printer_name}")
        return {"success": f"Receipt sent to {printer_name}"}

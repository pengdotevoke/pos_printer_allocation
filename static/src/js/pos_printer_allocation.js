odoo.define('pos_printer_allocation.PaymentScreen', function (require) {
    'use strict';

    const PaymentScreen = require('point_of_sale.PaymentScreen');
    const rpc = require('web.rpc');

    const CustomPaymentScreen = PaymentScreen => class extends PaymentScreen {
        async validateOrder(isForceValidate) {
            const order = this.env.pos.get_order();
            if (!order) return;

            try {
                // Call the backend allocation route
                const result = await rpc.query({
                    route: '/pos/print_receipt',
                    params: { order_id: order.uid },
                });

                if (result.error) {
                    this.showPopup('ErrorPopup', {
                        title: 'Printer Error',
                        body: result.error,
                    });
                    return;
                }

                this.showPopup('ConfirmPopup', {
                    title: 'Print Success',
                    body: result.success,
                });

                // Proceed with default behavior
                await super.validateOrder(isForceValidate);
            } catch (error) {
                console.error('Error in POS printer allocation:', error);
            }
        }
    };

    return CustomPaymentScreen;
});

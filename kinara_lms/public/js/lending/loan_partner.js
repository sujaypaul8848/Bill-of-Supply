frappe.ui.form.on("Loan Partner", {
	refresh(frm) {
        frm.events.toggle_processing_fee_billing(frm);
    },

    toggle_processing_fee_billing(frm) {
        frappe.db.get_value("Item", {"is_processing_fee": 1}, "name", (r) => {
            if(!frm.doc.shareables || !r.name || !frm.doc.shareables.some(s => s.shareable_type === r.name)) {
                frm.toggle_display("processing_fee_billing", 0);
            } else {
                frm.toggle_display("processing_fee_billing", 1);
            }
        });
    },
});

frappe.ui.form.on('Loan Partner Shareable', {
	shareable_type(frm) {
        frm.events.toggle_processing_fee_billing(frm);
	}
});
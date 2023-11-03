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

    kinara_security_emi_partner_ratio: function(frm) {
		frm.set_value("kinara_security_emi_own_ratio", 100 - frm.doc.kinara_security_emi_partner_ratio);
	},

	kinara_security_emi_own_ratio: function(frm) {
		frm.set_value("kinara_security_emi_partner_ratio", 100 - frm.doc.kinara_security_emi_own_ratio);
	},
});

frappe.ui.form.on('Loan Partner Shareable', {
	shareable_type(frm) {
        frm.events.toggle_processing_fee_billing(frm);
	}
});
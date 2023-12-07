frappe.ui.form.on('Loan Disbursement', {
	against_loan: function(frm) {
		frappe.db.get_value('Loan',frm.doc.against_loan,'repayment_schedule_type', (r) => {
			if (r) {
				set_field_options("repayment_schedule_type", r.repayment_schedule_type)
			}
		})
		
	},
	refresh: function(frm) {
		if(frm.doc.against_loan){
		frappe.db.get_value('Loan',frm.doc.against_loan,'repayment_schedule_type', (r) => {
			if (r) {
				set_field_options("repayment_schedule_type", r.repayment_schedule_type)
			}
		})
	}
	},

});

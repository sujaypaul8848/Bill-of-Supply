frappe.ui.form.on("Company", {
    refresh(frm){
        defaultDisbursementAccountFilter(frm);
    },
});

function defaultDisbursementAccountFilter(frm){
    
    frm.set_query('default_disbursement_account', () => {
        return {
            filters: [
                ["company", "=", frm.doc.company_name],
            ]
        };
    });
}
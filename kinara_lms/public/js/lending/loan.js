
frappe.ui.form.on("Loan", {
    refresh(frm){
        applyCustomerTypeFilter(frm);
    },
});

function applyCustomerTypeFilter(frm){
    frm.set_query('applicant', () => {
        return {
            filters: [
                ["customer_type", "!=", "Individual"],
            ]
        };
    });
    frm.set_query('custom_individual_applicant', () => {
        return {
            filters: [
                ["customer_type", "=", "Individual"],
            ]
        };
    });
    frm.fields_dict['custom_co_applicants'].grid.get_field('co_applicant').get_query = function(doc, cdt, cdn) {
        return {
            filters: [
                ["customer_type", "=", "Individual"],
            ]
        };
    };
    frm.fields_dict['custom_guarantors'].grid.get_field('guarantors').get_query = function(doc, cdt, cdn) {
        return {
            filters: [
                ["customer_type", "=", "Individual"],
            ]
        };
    };
};


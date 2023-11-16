function applyFilter(frm, field, filtersList){
    frm.set_query(field, () => {
        return {
            filters: filtersList
        }
    });
}

function applyChildTableFilter(frm, childTable, field, filtersList){
    frm.fields_dict[childTable].grid.get_field(field).get_query = function(doc, cdt, cdn) {
        return {
            filters: filtersList
        };
    };
}

frappe.ui.form.on("Loan", {
    refresh(frm){
        applyFilter(frm, "applicant", [["customer_type", "!=", "Individual"]])
        applyFilter(frm, "custom_individual_applicant", [["customer_type", "=", "Individual"]])
        applyChildTableFilter(frm, 'custom_co_applicants', 'co_applicant', [["customer_type", "=", "Individual"]])
        applyChildTableFilter(frm, 'custom_guarantors', 'guarantors', [["customer_type", "=", "Individual"]])
        
    }
})

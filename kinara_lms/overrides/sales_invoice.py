import frappe

def before_save(doc,method=None):
    if doc.loan:
        applicant = frappe.db.get_value('Loan',doc.loan,'custom_individual_applicant')
        if applicant:
            applicant_name, mobile_no = frappe.db.get_value('Customer', applicant, ['customer_name', 'mobile_no'])        
            if applicant_name:
                doc.custom_applicant_name = applicant_name
            if mobile_no:
                doc.custom_applicant_mobile_no = mobile_no
                
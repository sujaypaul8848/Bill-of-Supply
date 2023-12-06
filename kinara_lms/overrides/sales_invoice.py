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


def set_company_billing_address(doc,method=None):
    company_gst_regime = frappe.db.get_value('Company', doc.company, 'gst_regime')
    result = None
    if company_gst_regime == "Decentralized":
        customer_state = frappe.db.get_value('Address', doc.customer_address, 'state')
        filter = f"""ads.state = "{customer_state}" """
        result = execute_query(doc.company, filter)
    if not result:
        filter = f"ads.is_primary_address = 1"
        result = execute_query(doc.company, filter)
    doc.company_address = result[0]['name']
    doc.company_gstin = result[0]['gstin']


def execute_query(company_name,filter):
    conditions = f"""WHERE dl.parenttype = "Address" 
                    AND dl.parentfield = "links" 
                    AND dl.link_doctype = "Company" 
                    AND dl.link_name = "{company_name}" 
                    AND {filter}"""
    result = frappe.db.sql(f"""SELECT ads.name, ads.gstin
                                FROM `tabAddress` as ads
                                JOIN `tabDynamic Link` as dl
                                ON ads.name = dl.parent
                                {conditions}
                                LIMIT 1""", as_dict = True)
    return result
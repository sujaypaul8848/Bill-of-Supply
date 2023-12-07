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

def before_validate(doc,method=None):
    if doc.loan_partner:
        set_loan_partner_address(doc)
    set_company_billing_address(doc)
    


def set_company_billing_address(doc):
    company_gst_regime = frappe.db.get_value('Company', doc.company, 'gst_regime')
    result = None
    if company_gst_regime == "Decentralized":
        customer_state = frappe.db.get_value('Address', doc.customer_address, 'state')
        filter = f"""ads.state = "{customer_state}" """ #get company address matching customer's state
        result = execute_query(doc.company, filter, "Company")     #will return state if customer is present in company state
    if not result:
        filter = f"ads.is_primary_address = 1"          #get company primary address
        result = execute_query(doc.company, filter, "Company")     #will be used when regime is centralied or customer is not present in company state
    doc.company_address = result[0]['name']             #company address html is set automatically on save
    doc.company_gstin = result[0]['gstin']

def set_loan_partner_address(doc,method=None):
    loan_partner_gst_regime = frappe.db.get_value('Loan Partner', doc.loan_partner, 'organization_type')
    result = None
    if loan_partner_gst_regime == "Decentralized":
        customer_state = frappe.db.get_value('Address', doc.customer_address, 'state')
        filter = f"""ads.state = "{customer_state}" """ #get loan partner address matching customer's state
        result = execute_query(doc.loan_partner, filter, "Loan Partner")     #will return state if customer is present in loan partner state
    if not result:
        filter = f"ads.is_primary_address = 1"          #get loan partner primary address
        result = execute_query(doc.loan_partner, filter, "Loan Partner")     #will be used when regime is centralied or customer is not present in loan partner state
    doc.loan_partner_address = result[0]['name']             
    doc.loan_partner_gstin = result[0]['gstin']


def execute_query(link_name, filter, link_doctype):
    conditions = f"""WHERE dl.parenttype = "Address" 
                    AND dl.parentfield = "links" 
                    AND dl.link_doctype = "{link_doctype}" 
                    AND dl.link_name = "{link_name}" 
                    AND {filter}"""
    result = frappe.db.sql(f"""SELECT ads.name, ads.gstin
                                FROM `tabAddress` as ads
                                JOIN `tabDynamic Link` as dl
                                ON ads.name = dl.parent
                                {conditions}
                                LIMIT 1""", as_dict = True)
    return result
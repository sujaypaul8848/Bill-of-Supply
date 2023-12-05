import frappe

def validate_default_disbursement_account(doc, method=None):
    if doc.default_disbursement_account:
        bank_account = frappe.get_doc("Bank Account", doc.default_disbursement_account)
        if bank_account.Company != doc.company_name:
            frappe.throw(f"Account Should Belong to the Same Company")
        if bank_account.account_type not in ["Disbursement", "Disbursement & Collections"]:
            frappe.throw(f"Account Type Sould Be Disbursement or Disbursement & Collections")

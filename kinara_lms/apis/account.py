import frappe



@frappe.whitelist()
def get_default_disbursement_account(**kwargs):
	doc = frappe.get_doc("Company", kwargs["Company Name"])
	if not doc.default_disbursement_account:
		frappe.throw("No Default Disbursement Account Found")
	doc = frappe.get_doc("Account", doc.default_disbursement_account)
	return doc
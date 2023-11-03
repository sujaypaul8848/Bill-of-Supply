import frappe
from frappe import _


def validate_loan_partner(doc, method=None):
	if doc.kinara_security_emi_shared:
		for field in ["kinara_security_emi_partner_ratio", "kinara_security_emi_own_ratio"]:
			if not doc.get(field) or doc.get(field) < 1 or doc.get(field) > 99:
				frappe.throw(_("{0} should be between 1 and 99").format(frappe.bold(frappe.unscrub(field))))

import frappe
from frappe import _


def validate_contact(doc, method=None):
	for phone_no in doc.phone_nos:
		if len(phone_no.phone) != 10:
			frappe.throw(_("Phone number {0} needs to be of 10 digits").format(frappe.bold(phone_no.phone)))

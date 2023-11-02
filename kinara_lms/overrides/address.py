import frappe


def kinara_address_validate(doc, method=None):
	if doc.state:
		doc.state = frappe.db.get_value("Kinara State", doc.state, "system_state_name")
	
	customer = frappe.db.get_value("Customer", {"customer_primary_address": doc.name})
	if customer:
		frappe.db.set_value("Customer", customer, {"gstin": doc.gstin, "gst_category": doc.gst_category})

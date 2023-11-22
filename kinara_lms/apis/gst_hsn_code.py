import frappe


@frappe.whitelist()
def get_max_tax_rate(**kwargs):
	doc = frappe.get_doc("GST HSN Code", kwargs["HSN Code"])
	if not doc.taxes:
		return {"error" : "No Item Tax Template Available"}
	first_item_tax_template = doc.taxes[0].item_tax_template
	doc = frappe.get_doc("Item Tax Template", first_item_tax_template)
	max_tax_rate = max((tax.tax_rate for tax in doc.taxes), default=None)
	return {"tax_rate" : max_tax_rate}
# Copyright (c) 2023, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt


import frappe


def execute():
	if frappe.db.exists("Custom Field", {"name": "Loan Security-section_break_kinara_details"}):
		frappe.db.set_value(
			"Custom Field", {"name": "Loan Security-section_break_kinara_details"}, "insert_after", "disabled"
		)

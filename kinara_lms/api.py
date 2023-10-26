import json

import frappe


@frappe.whitelist()
def create_charge(args):
	if isinstance(args, str):
		args = json.loads(args)

	args = frappe._dict(args)
	
	charge = frappe.get_doc({
		"doctype": "Item",
		"item_code": args.charge_code,
		"item_name": args.charge_name,
		"gst_hsn_code": args.gst_hsn_code,
		"tax_inclusive": args.tax_inclusive,
		"item_defaults": [{
			"income_account": args.income_gl,
			"default_receivable_account": args.receivable_gl,
			"default_waiver_account": args.waiver_gl,
			"default_write_off_account": args.write_off_gl,
			"default_suspense_account": args.suspense_gl,
		}],
		"item_group": "Charges",
		"is_stock_item": 0,
	})

	if args.tax_applicable:
		charge.append("taxes", {"item_tax_template": "GST 18% - KCPL"})
	else:
		charge.is_nil_exempt = 1
	
	charge.insert()

	return charge


@frappe.whitelist()
def create_collateral(args):
	if isinstance(args, str):
		args = json.loads(args)

	args = frappe._dict(args)
	
	loan_security = frappe.get_doc({
		"doctype": "Loan Security",
		"loan_security_code": args.collateral_id,
		"loan_security_name": args.collateral_name,
		"unit_of_measure": "Nos",
		"loan_security_type": "Property",
		"security_owner_type": args.collateral_owner_type,
		"security_owner": args.collateral_owner,
		"kinara_collateral_type": args.kinara_collateral_type,
		"kinara_collateral_subtype": args.kinara_collateral_subtype,
		"kinara_collateral_ltv_amount": args.kinara_collateral_ltv_amount,
		"kinara_collateral_condition": args.kinara_collateral_condition,
		"kinara_description": args.kinara_description,
		"kinara_manufacturer_name": args.kinara_manufacturer_name,
		"kinara_model_number": args.kinara_model_number,
		"kinara_serial_number": args.kinara_serial_number,
		"kinara_entity_urn": args.kinara_entity_urn,
		"kinara_cersai_charge_required": args.kinara_cersai_charge_required
	}).insert()

	loan_security_assignment = frappe.new_doc("Loan Security Assignment")
	loan_security_assignment.applicant_type = args.applicant_type
	loan_security_assignment.applicant = args.applicant

	loan_security_assignment.append("securities", {
		"loan_security": loan_security.name,
		"qty": 1,
		"loan_security_price": args.collateral_value,
	})

	loan_security_assignment.insert()

	return loan_security_assignment


@frappe.whitelist()
def release_collateral_against_loan(args):
	if isinstance(args, str):
		args = json.loads(args)

	args = frappe._dict(args)

	loan_security_release = frappe.new_doc("Loan Security Release")
	loan_security_release.loan = args.loan

	loan_security_release.append("securities", {
		"loan_security": args.collateral_id,
		"qty": 1,
	})

	loan_security_release.insert()
	loan_security_release.submit()

	return loan_security_release


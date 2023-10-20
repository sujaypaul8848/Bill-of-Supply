import frappe

def created_loan_related_docs(doc, method=None):
	for d in doc.get("entities") or []:
		frappe.get_doc({
			"doctype": "Loan Entity Mapping",
			"loan": doc.name,
			"entity": d.get("entity"),
			"entity_relationship_type": d.get('entity_relationship_type')
		}).insert()
	
	for d in doc.get("loan_documents") or []:
		frappe.get_doc({
			"doctype": "Loan Documents",
			"loan": doc.name,
			"document_type": doc.name,
			"document_details": d.get("document_details")
		}).insert()

	for d in doc.get("insurance_details"):
		insurance_doc = frappe.new_doc("Loan Insurance")
		insurance_doc.loan = doc.name
		insurance_doc.insurer_entity_id = d.get("insurer_entity_id")
		insurance_doc.insurer_entity_type = d.get("insurer_entity_type")
		insurance_doc.insurer_urn = d.get("insurer_urn")
		insurance_doc.insurance_id = d.get("insurance_id")
		insurance_doc.insurance_premium = d.get("insurance_premium")
		insurance_doc.insured_amount = d.get("insured_amount")
		insurance_doc.nominee_urn = d.get("nominee_urn")
		insurance_doc.start_date = d.get("start_date")
		insurance_doc.end_date = d.get("end_date")
		insurance_doc.save()

	for d in doc.get("disbursement_details"):
		disbursement_doc = frappe.new_doc("Loan Disbursement")
		disbursement_doc.against_loan = doc.name
		disbursement_doc.disbursement_date= d.get("actual_disbursement_date")
		disbursement_doc.reference_date= d.get("scheduled_disbursement_date")
		disbursement_doc.disbursed_amount= d.get("disbursement_amount")
		disbursement_doc.bank_account = d.get("disbursement_account")
		disbursement_doc.customer_bank_account_number = d.get("customer_bank_account_number")
		disbursement_doc.customer_bank_ifsc_code = d.get("customer_bank_ifsc_code")
		disbursement_doc.customer_bank_name = d.get("customer_bank_name")
		disbursement_doc.customer_bank_branch_name = d.get("customer_bank_branch_name")
		disbursement_doc.customer_bank_account_holder_name = d.get("customer_bank_account_holder_name")
		disbursement_doc.disbursement_mode = d.get("disbursement_mode")
		disbursement_doc.save()

	loan_security_assignment = frappe.new_doc("Loan Security Assignment")
	loan_security_assignment.applicant_type = doc.get("applicant_type")
	loan_security_assignment.applicant = doc.get("applicant")

	for d in doc.get("collateral_details"):
		security = frappe.new_doc("Loan Security")
		security.loan_security_code = d.get("collateral_id")
		security.loan_security_name = d.get("collateral_id")
		security.unit_of_measure = "Nos",
		security.loan_security_type = "Property"
		security.save()

		loan_security_assignment.append("securities", {
			"loan_security": security.name,
			"amount": d.get("collateral_value")
		})

	loan_security_assignment.append("allocated_loans", {
		"loan": doc.name
	})

	loan_security_assignment.save()

def override_name(doc, method=None):
	doc.name = doc.get("loan_account_number")
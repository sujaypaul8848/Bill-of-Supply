import frappe

def created_loan_related_docs(doc, method=None):
	for d in doc.get("entities"):
		frappe.get_doc({
			"doctype": "Loan Entity Mapping",
			"loan": doc.name,
			"entity": d.get("entity"),
			"entity_relationship_type": d.get('entity_relationship_type')
		}).insert()
	
	for d in doc.get("loan_documents"):
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

	if doc.get("disbursement_details"):
		disbursement_details = frappe.new_doc("Loan Disbursement Tranche")
		disbursement_details.loan = doc.name
		for d in doc.get("disbursement_details"):
			disbursement_details.append("tranches", {
				"disbursement_date": d.get("disbursement_date"),
				"disbursement_amount": d.get("disbursement_amount"),
				"bank_account": d.get("bank_account")
			})
		disbursement_details.save()

def override_name(doc, method=None):
	doc.name = doc.get("loan_account_number")
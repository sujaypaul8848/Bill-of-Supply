from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def execute():
	create_custom_fields(
		{
			"Loan": [
			{
				"fieldname": "loan_id",
				"label": "Loan ID",
				"fieldtype": "Data",
				"unique": 1,
				"insert_after": "applicant"
			},
				{
				"fieldname": "loan_account_number",
				"label": "Loan Account Number",
				"fieldtype": "Data",
				"unique": 1,
				"insert_after": "loan_id"
			},
			{
				"fieldname": "loan_partner",
				"label": "Loan Partner",
				"fieldtype": "Link",
				"options": "Loan Partner",
				"insert_after": "company"
			},
			{
				"fieldname": "kinara_lms_details",
				"label": "Kinara LMS Details",
				"fieldtype": "Section Break",
				"insert_after": "is_term_loan",
				"collapsible": 1
			},
			{
				"fieldname": "hub",
				"label": "Hub",
				"fieldtype": "Data",
				"insert_after": "kinara_lms_details"
			},
			{
				"fieldname": "loan_officer",
				"label": "Loan Officer",
				"fieldtype": "Data",
				"insert_after": "hub"
			},
			{
				"default": 0,
				"fieldname": "her_vikas",
				"label": "Her Vikas",
				"fieldtype": "Check",
				"insert_after": "loan_officer"
			},
			{
				"fieldname": "channel",
				"label": "Channel",
				"fieldtype": "Data",
				"insert_after": "her_vikas"
			},
			{
				"fieldname": "lap_combo",
				"label": "LAP Combo",
				"fieldtype": "Check",
				"insert_after": "channel"
			},
			{
				"fieldname": "green_finance_flag",
				"label": "Green Finance Flag",
				"fieldtype": "Check",
				"insert_after": "lap_combo"
			},
			{
				"fieldname": "direct_assignment_tagging",
				"label": "Securitization/ Direct Assignment Tagging",
				"fieldtype": "Data",
				"insert_after": "green_finance_flag"
			},
			{
				"fieldname": "kinara_column_break",
				"fieldtype": "Column Break",
				"insert_after": "direct_assignment_tagging"
			},
			{
				"fieldname": "loan_purpose",
				"label": "Loan Purpose",
				"fieldtype": "Data",
				"insert_after": "kinara_column_break"
			},
			{
				"fieldname": "loan_sub_purpose",
				"label": "Loan Sub Purpose",
				"fieldtype": "Data",
				"insert_after": "loan_purpose"
			},
	]
		},
		ignore_validate=True,
	)

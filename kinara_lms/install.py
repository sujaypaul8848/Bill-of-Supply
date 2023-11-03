from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.desk.page.setup_wizard.setup_wizard import make_records
from frappe.custom.doctype.property_setter.property_setter import make_property_setter

from kinara_lms.constants.kinara_default_states import KINARA_DEFAULT_STATES


KINARA_CUSTOM_FIELDS = {
	"Customer": [
		{
			"fieldname": "customer_urn",
			"label": "Customer URN",
			"fieldtype": "Data",
			"insert_after": "customer_name",
			"unique": 1,
			"reqd": 1,
		},
		{
			"fieldname": "entity_type",
			"label": "Entity Type",
			"fieldtype": "Select",
			"insert_after": "customer_urn",
			"options": "Applicant\nCo-Applicant",
			"reqd": 1,
		},
	],
	"Loan Partner": [
		{
			"fieldname": "kinara_details_section",
			"label": "Kinara Details",
			"fieldtype": "Section Break",
			"insert_after": "partial_payment_mechanism"
		},
		{
			"fieldname": "processing_fee_billing",
			"label": "Processing Fee Billing (against partner share)",
			"fieldtype": "Percent",
			"insert_after": "kinara_details_section",
		},
		{
			"default": "0",
			"fieldname": "kinara_security_emi_shared",
			"label": "Security EMI shared",
			"fieldtype": "Check",
			"insert_after": "processing_fee_billing",
		},
		{
			"fieldname": "kinara_security_emi_partner_ratio",
			"fieldtype": "Percent",
			"label": "Security EMI Partner Ratio",
			"depends_on": "eval:doc.kinara_security_emi_shared;",
			"insert_after": "kinara_security_emi_shared",
		},
		{
			"fieldname": "kinara_security_emi_own_ratio",
			"fieldtype": "Percent",
			"label": "Security EMI Own Ratio",
			"depends_on": "eval:doc.kinara_security_emi_shared;",
			"insert_after": "kinara_security_emi_partner_ratio",
		},
	],
	"Item": [
		{
			"fieldname": "kinara_details_tab",
			"label": "Kinara Details",
			"fieldtype": "Tab Break",
			"insert_after": "total_projected_qty",
		},
		{
			"default": "0",
			"fieldname": "tax_inclusive",
			"label": "Tax Inclusive",
			"fieldtype": "Check",
			"insert_after": "kinara_details_tab",
		},
		{
			"default": "0",
			"fieldname": "is_processing_fee",
			"label": "Is Processing Fee",
			"fieldtype": "Check",
			"insert_after": "tax_inclusive",
		},
	],
	"Loan Disbursement": [
		{
			"fieldname": "kc_disbursement_section",
			"label": "Kinara Disbursement Details",
			"fieldtype": "Section Break",
			"insert_after": "reference_number"
		},
		{
			"fieldname": "disbursement_mode",
			"label": "Disbursement Mode",
			"fieldtype": "Data",
			"insert_after": "kc_disbursement_section"
		},
		{
			"fieldname": "customer_bank_account_number",
			"label": "Customer Bank Account Number",
			"fieldtype": "Data",
			"insert_after": "disbursement_mode"
		},
		{
			"fieldname": "customer_bank_ifsc_code",
			"label": "Customer Bank IFSC Code",
			"fieldtype": "Data",
			"insert_after": "customer_bank_account_number"
		},
		{
			"fieldname": "customer_bank_name",
			"label": "Customer Bank Name",
			"fieldtype": "Data",
			"insert_after": "customer_bank_ifsc_code"
		},
		{
			"fieldname": "customer_bank_branch_name",
			"label": "Customer Bank Branch Name",
			"fieldtype": "Data",
			"insert_after": "customer_bank_name"
		},
		{
			"fieldname": "customer_bank_account_holder_name",
			"label": "Customer Bank Account Holder Name",
			"fieldtype": "Data",
			"insert_after": "customer_bank_branch_name"
		},
	],
	"Loan": [
		{
			"fieldname": "loan_id",
			"label": "Loan ID",
			"fieldtype": "Data",
			"unique": 1,
			"insert_after": "applicant"
		},
		{
			"fieldname": "loan_application_id",
			"label": "Loan Application ID",
			"fieldtype": "Data",
			"unique": 1,
			"insert_after": "loan_id"
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
		{
			"fieldname": "effective_interest_rate",
			"label": "Annualized Percentage/Effective Interest Rate",
			"fieldtype": "Float",
			"insert_after": "green_finance_flag"
		},
	],
	"Company": [
		{
			"fieldname": "cin_number",
			"label": "CIN Number",
			"fieldtype": "Data",
			"insert_after": "default_holiday_list",
		},
	],
	"Loan Security": [
		{
			"fieldname": "section_break_kinara_details",
			"label": "Kinara Details",
   			"fieldtype": "Section Break",
			"insert_after": "disabled",
		},
		{
			"fieldname": "kinara_collateral_type",
			"label": "Kinara Collateral Type",
			"fieldtype": "Data",
			"insert_after": "section_break_kinara_details"
		},
		{
			"fieldname": "kinara_collateral_subtype",
			"label": "Kinara Collateral Subtype",
			"fieldtype": "Data",
			"insert_after": "kinara_collateral_type"
		},
		{
			"fieldname": "kinara_collateral_ltv_amount",
			"label": "Kinara LTV Amount",
			"fieldtype": "Currency",
			"options": "Company:company:default_currency",
			"insert_after": "kinara_collateral_subtype"
		},
		{
			"fieldname": "kinara_collateral_condition",
			"label": "Kinara Collateral Condition",
			"fieldtype": "Data",
			"insert_after": "kinara_collateral_ltv_amount"
		},
		{
			"fieldname": "column_break_dsfe",
			"fieldtype": "Column Break",
			"insert_after": "kinara_collateral_condition"
		},
		{
			"fieldname": "kinara_description",
			"label": "Kinara Description",
			"fieldtype": "Data",
			"insert_after": "column_break_dsfe"
		},
		{
			"fieldname": "kinara_manufacturer_name",
			"label": "Kinara Manufacturer Name",
			"fieldtype": "Data",
			"insert_after": "kinara_description"
		},
		{
			"fieldname": "kinara_model_number",
			"label": "Kinara Model Number",
			"fieldtype": "Data",
			"insert_after": "kinara_manufacturer_name"
		},
		{
			"fieldname": "kinara_serial_number",
			"label": "Kinara Serial Number",
			"fieldtype": "Data",
			"insert_after": "kinara_model_number"
		},
		{
			"fieldname": "kinara_entity_urn",
			"label": "Kinara Entity URN",
			"fieldtype": "Data",
			"insert_after": "kinara_serial_number"
		},
		{
			"fieldname": "kinara_cersai_charge_required",
			"label": "Kinara CERSAI Charge Required",
			"fieldtype": "Check",
			"insert_after": "kinara_entity_urn"
		},
	],
}


def after_install():
	create_custom_fields(KINARA_CUSTOM_FIELDS, ignore_validate=True)
	make_fixtures()
	add_property_setters()


def make_fixtures():
	records = [
		# Bank Account Types
		{"doctype": "Bank Account Type", "account_type": "Disbursement"},
		{"doctype": "Bank Account Type", "account_type": "Collections"},
		{"doctype": "Bank Account Type", "account_type": "Disbursement & Collections"},\
	] + KINARA_DEFAULT_STATES

	make_records(records)

def add_property_setters():
	make_property_setter(
		"Sales Invoice",
		"customer",
		"fetch_from",
		"loan.applicant",
		"Small Text",
		validate_fields_for_doctype=False,
	)

from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from kinara_lms.install import KINARA_CUSTOM_FIELDS

def execute():
	custom_fields = KINARA_CUSTOM_FIELDS["Loan Partner"]
	create_custom_fields(
		{
			"Loan Partner": custom_fields
		},
		ignore_validate=True,
	)

from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def execute():
	create_custom_fields(
		{
			"Company": [
				{
					"fieldname": "cin_number",
					"label": "CIN Number",
					"fieldtype": "Data",
					"insert_after": "default_holiday_list",
				},
			],
		},
		ignore_validate=True,
	)

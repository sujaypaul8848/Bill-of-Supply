from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def execute():
	create_custom_fields(
		{
			"Customer": [
				{
					"fieldname": "customer_urn",
					"label": "Customer URN",
					"fieldtype": "Data",
					"insert_after": "customer_name",
					"unique": 1,
					"reqd": 1,
				},
			],
		},
		ignore_validate=True,
	)

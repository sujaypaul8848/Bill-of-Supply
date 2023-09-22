from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


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
	],
}


def after_install():
	create_custom_fields(KINARA_CUSTOM_FIELDS, ignore_validate=True)

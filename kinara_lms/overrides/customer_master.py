# Copyright (c) 2023, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from erpnext.selling.doctype.customer.customer import Customer


class CustomerMaster(Customer):
	def autoname(self):
		self.name = self.customer_urn

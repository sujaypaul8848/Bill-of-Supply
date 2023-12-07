import frappe

@frappe.whitelist()
def get_loan_list(hub=None,loan_account_number=None,customer_urn=None,customer_name=None):
	filters = {}
	loan = ''
	if hub != None:
		filters["hub"] = hub
	if loan_account_number != None:
		filters["loan_account_number"] = loan_account_number
	if customer_name:
		customer_name = frappe.db.get_value('Customer',{'customer_name':customer_name},'customer_urn')
	if not customer_urn  and customer_name:
		filters["applicant"] = customer_name
	if customer_urn  and not customer_name:
		filters["applicant"] = customer_urn
	if (customer_urn and customer_name) and (customer_urn  == customer_name):
		filters["applicant"] = customer_urn
	if filters != {}:
		loan = frappe.db.get_list('Loan',filters = filters, pluck='name')
	if (customer_urn and customer_name) and (customer_urn  != customer_name):
		a = []
		loan_urn = frappe.db.get_list('Loan',filters = {'applicant':customer_urn}, pluck='name')
		a.extend(loan_urn)
		loan_name = frappe.db.get_list('Loan',filters = {'applicant':customer_name}, pluck='name')
		a.extend(loan_name)
		if loan:
			loan.extend(a)
		else:
			loan = a
	return loan

@frappe.whitelist()
def get_outstanding_principal(**kwargs):
	group_by = "branch"
	where_clause = ""
	if "branch" in kwargs:
		where_clause = f"""WHERE loan.branch = "{kwargs["branch"]}" """
	outstanding_principal = frappe.db.sql(f"""
    										SELECT
        										loan.branch, SUM(loan.total_payment - loan.total_interest_payable - loan.total_principal_paid) as outstanding_principal
    										FROM `tabLoan` as loan
    										{where_clause}
											GROUP BY {group_by}
											""", as_dict = True)
	return outstanding_principal
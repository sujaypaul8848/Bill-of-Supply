import frappe
import datetime



@frappe.whitelist()
def get_demand_data(**kwargs):
    response = []
    format_str = '%d/%m/%Y'
    date = datetime.datetime.strptime(kwargs["date"], format_str)
    repayment_schedule_list = get_repayment_schedule(date)
    for repayment_schedule in repayment_schedule_list:
        response_doc = {
            "partner_name": "",
            "Sponsor Bank Code": "",
            "Hub": "",
            "Spoke": "",
            "ClientID": "",
            "AccountID": "",
            "ProductName": "",
            "ClientName": "",
            "Proprietor Name": "",
            "InstallmentDueDate": "",
            "LoanAmount": "",
            "Cheque ID": "",
            "Current Due": "",
            "NoOfInstallment": "",
            "Term": "",
            "Repayment Mode": "",
            "Bank Name": "",
            "Branch Name": "",
            "Realization Status": "",
            "Realization Reason": "",
            "Realization Date": "",
            "Mobile No.": ""
        }
        response_doc["InstallmentDueDate"] = repayment_schedule["payment_date"]
        response_doc["Current Due"] = repayment_schedule["total_payment"]
        response_doc["NoOfInstallment"] = repayment_schedule["idx"]
        response.append(response_doc)
	
    return response

@frappe.whitelist()
def get_repayment_schedule(date):
    limit = ""
    print("hello")
    result = frappe.db.sql(f"""SELECT *
                                FROM `tabRepayment Schedule`
                                WHERE payment_date = "{date}"
                                {limit}""", as_dict = True)
    return result
	
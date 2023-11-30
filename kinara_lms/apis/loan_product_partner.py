import frappe

@frappe.whitelist()
def get_prod_attr(partner):
    if partner != None:
        values = {'partner': partner}
        data = frappe.db.sql("""
            SELECT
                lp.product_name,
                lp.company,
                lp.is_term_loan,
                lp.loan_category,
                lp.maximum_loan_amount,
                lp.rate_of_interest,
                lp.repayment_schedule_type,
                lp.penalty_interest_rate,
                lp.grace_period_in_days,
                lp.write_off_amount,
                lp.min_days_bw_disbursement_first_repayment,
                lp.min_auto_closure_tolerance_amount,
                lp.max_auto_closure_tolerance_amount,
                lp.cyclic_day_of_the_month,
                lp.days_past_due_threshold_for_npa,
                lp.custom_moratorium_types_allowed,
                lp.custom_moratorum_duration,
                lp.loan_account,
                lp.interest_income_account,
                lp.penalty_income_account,
                lp.write_off_account
            FROM `tabLoan Product` lp
                LEFT JOIN `tabLoan Product Loan Partner` lplp
                ON lp.name = lplp.parent
            WHERE lplp.loan_partner = %(partner)s
        """, values=values, as_dict=1)
        return data
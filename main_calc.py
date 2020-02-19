

import pandas as pd
import datetime as dt
from dateutil.relativedelta import relativedelta

# ASSUMPTIONS
# 0 credit card debt (paid in full on time every month)
# savings account APY compounds daily
# salary increases once annually

# input params
input_param_dict = {
    'salary_gross': 100000,
    'salary_growth': 3.5 / 100.,
    'tax_now': 25 / 100.,
    'SWR': 4 / 100.,
    'annual_spend': 80000,
    'tax_retirement': 10 / 100.,
    'market_return': 8 / 100.,  # input a range -- simulate based on it
    'inflation': 2 / 100.  # input a range -- simulate based on it
}

# assets
assets_dict = {
    'checking_accts_balance': 8500,
    'savings_acct_balance': 7900,
    'savings_acct_APR': 1.8 / 100.,
    'savings_contrib_monthly': 9 / 100.,  # enter as % of net (post-tax) income -- offer choice (% or value) as radio button?
    'retirement_accts_pretax_balance': 6000,  # traditional
    'retirement_accts_pretax_contrib_monthly': 10 / 100.,  # enter as % of net (post-tax) income -- offer choice (% or value) as radio button?
    'retirement_accts_posttax_balance': 3500,  # Roth
    'retirement_accts_posttax_contrib_monthly': 0 / 100.,  # enter as % of net (post-tax) income -- offer choice (% or value) as radio button?
    'home_equity': 0,
    # TODO: https://www.reddit.com/r/financialindependence/comments/f0kabc/how_to_calculate_your_fire_number_when_you_have_a/
    'car_value': 0
}

# liabilities
liabilities_dict = {
    'student_loans_principal': 25000 * -1,
    'student_loans_APR': 4.41 / 100.,
    'student_loans_monthly_payment': 185.,  # TODO: Make this variable (increase with time?)
    'mortgage_principal': 0,
    'mortgage_APR': 0 / 100.,
    'car_loan_principal': 0,
    'car_loan_APR': 0 / 100.,
    'car_depreciation': 0 / 100.
}

# TODO: Convert all input values to float


def main_calc():
    # generate df of dates (monthly or yearly depending on time scale selected, or radio button selected)
    # calculate assets, liabilities, NW for that month/year

    today = dt.datetime.now().strftime("%m/%d/%Y")

    # enter base info (from input) into dict, then df
    df_dict = {
        'date': [today],
        'Salary (Gross)': [input_param_dict['salary_gross']],
        'Checking Balance': [assets_dict['checking_accts_balance']],
        'Savings Balance': [assets_dict['savings_acct_balance']],
        'Retirement Accts (Pretax)': [assets_dict['retirement_accts_pretax_balance']],
        'Retirement Accts (Posttax)': [assets_dict['retirement_accts_posttax_balance']],
        # TODO: Add other assets
        'Student Loans': [liabilities_dict['student_loans_principal']]
        # TODO: Add other liabilities
    }

    df = pd.DataFrame.from_dict(df_dict)

    # iteratively add rows by creating a new df each time, then concat all dfs at the end
    def add_new_month_data(df):
        lastperiod_df = df.iloc[df.shape[0] - 1]

        lastperiod_date = dt.datetime.strptime(lastperiod_df['date'], '%m/%d/%Y')
        new_date_relative = lastperiod_date + relativedelta(months=1)
        new_date = dt.datetime(new_date_relative.year, new_date_relative.month, 1)

        gross_salary = input_param_dict['salary_gross'] #* (1 + input_param_dict['salary_growth'] ** (lastperiod_df['date'] - df.iloc[0]['date']))
        net_salary = gross_salary * (1 - input_param_dict['tax_now'])
        checking_bal = lastperiod_df['Checking Balance']
        savings_bal = assets_dict['savings_contrib_monthly']*(net_salary / 12.) + \
                      lastperiod_df['Savings Balance'] * (1 + (assets_dict['savings_acct_APR'] / 365.) ** (new_date - lastperiod_date).days)
        retirement_pretax_bal = assets_dict['retirement_accts_pretax_contrib_monthly']*(gross_salary / 12.) + \
                                lastperiod_df['Retirement Accts (Pretax)'] * (1 + (input_param_dict['market_return'] / 12.))
        retirement_posttax_bal = assets_dict['retirement_accts_posttax_contrib_monthly']*(net_salary / 12.) + \
                                 lastperiod_df['Retirement Accts (Posttax)'] * (1 + (input_param_dict['market_return'] / 12.))
        student_loan_bal = -1 * (abs((lastperiod_df['Student Loans']) * (1 + liabilities_dict['student_loans_APR'] / 12.)) \
                                 - liabilities_dict['student_loans_monthly_payment'])

        update_df_dict = {
            'date': [new_date.strftime("%m/%d/%Y")],
            'Salary (Gross)': [gross_salary],
            'Checking Balance': [checking_bal],
            'Savings Balance': [savings_bal],
            'Retirement Accts (Pretax)': [retirement_pretax_bal],
            'Retirement Accts (Posttax)': [retirement_posttax_bal],
            # TODO: Add other assets
            'Student Loans': [student_loan_bal]
            # TODO: Add other liabilities
        }

        update_df = pd.DataFrame.from_dict(update_df_dict)

        return update_df

    for i in range(500):
        df = pd.concat([df, add_new_month_data(df)])

    # TODO: Add remaining assets & liabilities
    df['Assets'] = df['Checking Balance'] + df['Savings Balance'] + df['Retirement Accts (Pretax)'] + df[
        'Retirement Accts (Posttax)']
    df['Liabilities'] = df['Student Loans']
    df['Net Worth'] = df['Assets'] + df['Liabilities']

    return df

df = main_calc()

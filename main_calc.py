import pandas as pd
import datetime as dt


# ASSUMPTIONS
# 0 credit card debt (paid in full on time every month)
# savings account APY compounds daily

# input params
input_param_dict = {
    'salary_gross': 65000,
    'salary_growth': 3.5,
    'tax_now': 25,
    'SWR': 4,
    'annual_spend': 80000,
    'tax_retirement': 10,
    'market_return': 8,  # input a range -- simulate based on it
    'inflation': 2  # input a range -- simulate based on it
}

# assets
assets_dict = {
    'checking_accts_balance': 10000,
    'savings_acct_balance': 8000,
    'savings_acct_APR': 1.8,
    'savings_contrib_monthly': 9,  # enter as % of net (post-tax) income -- offer choice (% or value) as radio button?
    'retirement_accts_pretax_balance': 6000,  # traditional
    'retirement_accts_pretax_contrib_monthly': 10,  # enter as % of net (post-tax) income -- offer choice (% or value) as radio button?
    'retirement_accts_posttax_balance': 3500,  # Roth
    'retirement_accts_posttax_contrib_monthly': 0,  # enter as % of net (post-tax) income -- offer choice (% or value) as radio button?
    'home_equity': 0,
    # TODO: https://www.reddit.com/r/financialindependence/comments/f0kabc/how_to_calculate_your_fire_number_when_you_have_a/
    'car_value': 0
}

# liabilities
liabilities_dict = {
    'student_loans_principal': 25000,
    'student_loans_APR': 4,
    'mortgage_principal': 0,
    'mortgage_APR': 0,
    'car_loan_principal': 0,
    'car_loan_APR': 0,
    'car_depreciation': 0
}


def convert_to_decimal():
    input_param_dict['salary_growth'] = input_param_dict['salary_growth'] / 100.
    input_param_dict['tax_now'] = input_param_dict['tax_now'] / 100.
    input_param_dict['SWR'] = input_param_dict['SWR'] / 100.
    input_param_dict['tax_retirement'] = input_param_dict['tax_retirement'] / 100.
    input_param_dict['inflation'] = input_param_dict['inflation'] / 100.

    assets_dict['savings_acct_APR'] = assets_dict['savings_acct_APR'] / 100.
    assets_dict['savings_contrib_monthly'] = assets_dict['savings_contrib_monthly'] / 100.
    'retirement_accts_pretax_contrib_monthly'
    'retirement_accts_posttax_contrib_monthly'

    liabilities_dict['student_loans_APR'] = liabilities_dict['student_loans_APR'] / 100.
    liabilities_dict['mortgage_APR'] = liabilities_dict['mortgage_APR'] / 100.
    liabilities_dict['car_loan_APR'] = liabilities_dict['car_loan_APR'] / 100.


def main_calc():
    monthly_net_income = (input_param_dict['salary_gross']*(1 - input_param_dict['tax_now'])) / 12.

    # generate df of dates (monthly or yearly depending on time scale selected, or radio button selected)
    # calculate assets, liabilities, NW for that month/year

    today = dt.datetime.now().strftime("%m/%d/%Y")

    df = pd.Series(pd.date_range(today, periods=60, freq=pd.offsets.MonthBegin(1)))

    print(df.head(10))

    #
    # savings_acct_daily_APY = assets_dict['savings_acct_APR'] / 365.
    # savings_acct_balance_lastperiod =
    # savings_balance_update = (savings_acct_balance_lastperiod * (1 + (assets_dict['savings_acct_APR'] / 365.))^30) + (assets_dict['savings_contrib_monthly'] * monthly_net_income)
    #
    # retirement_accts_pretax_balance_lastperiod =
    # retirement_accts_posttax_balance_lastperiod =
    # retirement_accts_pretax_balance_update = (retirement_accts_pretax_balance_lastperiod * \
    #                                           (1 + input_param_dict['market_return'])) + \
    #                                          (assets_dict['retirement_accts_pretax_contrib_monthly'] * \
    #                                           input_param_dict['salary_gross'] / 12.)
    # retirement_accts_posttax_balance_update =(retirement_accts_posttax_balance_lastperiod * (1 + input_param_dict['market_return'])) + assets_dict['retirement_accts_posttax_contrib_monthly']
    #
    # return df


main_calc()

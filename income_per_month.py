Annual_income=1000000
Monthly_income=Annual_income/12
health_insurance=5000
monthly_income=Monthly_income-health_insurance
tax=10
tax_amount=(monthly_income*tax)/100
final_monthly_income=monthly_income-tax_amount
print("Hand on cash per month:",final_monthly_income)
print(tax_amount)
#Problem Set 2 Problem 1
#Author:Siddhant Gokhale


#balance
balance=int(input('Please enter the credit card balance:'))

#annual interest rate as a decimal
annualInterestRate=float(input('Please enter the annual interest rate in decimals:'))

#minimum monthly payment rate as a decimal
monthlyPaymentRate=float(input('Please enter the monthly payment rate in decimals:'))

#monthly interest rate is the annual interest rate divided into the 12 months
monthlyInterestRate=annualInterestRate/12

for month in range(12):
    payment= balance*monthlyPaymentRate
    monthlyunpaidbalance= balance-payment
    balance = (1+monthlyInterestRate)*monthlyunpaidbalance

print('Remaining balance:',round(balance,2))

#-------------------------------------------------------------------------------


    

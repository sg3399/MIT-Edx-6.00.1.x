#Problem Set 2 Problem 3
#Author:Siddhant Gokhale

#balance
balance=int(input('Please enter the credit card balance:'))

#annual interest rate as a decimal
annualInterestRate=float(input('Please enter the annual interest rate in decimals:'))

b0=balance
monthlyInterestRate=annualInterestRate/12
lowerbound=b0/12
upperbound= b0*((1+monthlyInterestRate)**12)/12
payment_guess=(lowerbound+upperbound)/2

#using bisection method
while abs(balance)>0.01:
    for month in range(12):    
        monthlyunpaidbalance= balance-payment_guess
        balance = (1+monthlyInterestRate)*monthlyunpaidbalance
    if abs(balance)<0.01:
        print('Lowest Payment:',round(payment_guess,2)) 
    else:
        if balance>0:
            lowerbound=payment_guess
        else:
            upperbound=payment_guess
        payment_guess=(lowerbound+upperbound)/2
        balance = b0

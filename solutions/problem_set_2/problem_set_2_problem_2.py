#balance
balance=int(input('Please enter the credit card balance:'))

#annual interest rate as a decimal
annualInterestRate=float(input('Please enter the annual interest rate in decimals:'))

b0=balance
monthlyInterestRate=annualInterestRate/12
payment_guess=0

while balance>0:
    for month in range(12):    
        monthlyunpaidbalance= balance-payment_guess
        balance = (1+monthlyInterestRate)*monthlyunpaidbalance
    if balance > 0:
        payment_guess += 10
        balance = b0
    else:
        print('Lowest Payment:',round(payment_guess,2)) 
   
import math

print("Enter the loan principal:")
loan_principal = float(input())
print("What do you want to calculate?")
print('type "m" - for number of monthly payments,')
print('type "p" - for the monthly payment:')
action = input()

if action == 'm':
    print('Enter the monthly payment:')
    payment_amount = input()
    months_to_repay = loan_principal / float(payment_amount)
    months_to_repay = math.ceil(months_to_repay)
    if months_to_repay == 1:
        print('It will take ' + str(months_to_repay) + ' month to repay the loan')
    else:
        print('It will take ' + str(months_to_repay) + ' months to repay the loan')
else:
    print('Enter the number of months:')
    months = int(input())
    payment: int = math.ceil(loan_principal / months)
    last_payment: int = math.ceil(loan_principal - (months - 1) * payment)
    print('Your monthly payment = ' + str(payment) + ' and the last payment = ' + str(last_payment) + '.')

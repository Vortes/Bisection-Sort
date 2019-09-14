# Problem Set 3
# Name: alan weng
# Time Spent: 1:30
#

def start():
    balance = float(input('Enter the outstanding balance on your credit card:'))
    annual_interest = float(input('Enter the annual credit card interest rate as a decimal:'))
    monthlyInterestRate = annual_interest/12
    new_balance = balance
    
    lower_bound = new_balance / 12.0
    upper_bound = (balance * (1 + (annual_interest / 12.0)) ** 12.0) / 12.0
    tolerence = .1
    looking = True

    while(abs(balance) > tolerence and looking):
        in_between = (lower_bound+upper_bound) / 2.0
        balance = new_balance

        for i in range(12):
            balance = balance - in_between + ((balance - in_between) * monthlyInterestRate)
        
        if balance > tolerence:
            lower_bound = in_between
        elif balance < tolerence:
            upper_bound = in_between
        else:
            looking = False

    print('RESULT')
    print(f'Monthly payment to pay off debt in 1 year: {round(in_between,2)}')
    print(f'Number of months needed: 12')
    print(f'Balance: {round(balance,2)}')


start()
### 1st Appraoch:

balance = 999999
annualInterestRate = 0.18
monthly_interest_rate = annualInterestRate / 12.0


updated_balance = balance
payment_lower_bound = balance / 12.0
payment_upper_bound = (balance*(1+monthly_interest_rate)**12)/12.0
epsilon = 0.01

while updated_balance > epsilon:
    paid = (payment_upper_bound + payment_lower_bound) / 2.0
    updated_balance = balance
    for month in range(1,13):
        monthly_unpaid_balance = updated_balance - paid
        updated_balance = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)
    if updated_balance > 0:
        payment_lower_bound = paid
    else:
        payment_upper_bound = paid
        updated_balance = balance
print 'Lowest Payment: ' + str(round(paid,2))


--------------------------------------------------------------------------------------------------------


###### 2nd Appraoch:

balance = 999999
annualInterestRate = 0.18
monthly_interest_rate = annualInterestRate / 12.0


def run(balance, annualInterestRate):
    lowerBound = balance / 12.0
    upperBound = (balance * (1 + (annualInterestRate / 12.0)) ** 12) / 12.0

    E = 0.01
    while(True):
        newBalance = balance
        monthlyPayout = (lowerBound + upperBound) / 2.0
        for month in range(12):
            newBalance = (newBalance - monthlyPayout) * (1 + (annualInterestRate / 12))
        if round(newBalance, 2) < E:
            upperBound = monthlyPayout
        elif round(newBalance, 2) > E:
            lowerBound = monthlyPayout
        else:
            return round(monthlyPayout, 2)
print "Lowest Payment: %s" % (run(balance, annualInterestRate))







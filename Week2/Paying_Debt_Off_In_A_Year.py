#### 1st Appraoch:

balance = 4213; annualInterestRate = 0.2; monthlyPaymentRate = 0.04
payment_base = 0
balance_new = balance
while balance_new > 0:
    balance_new = balance
    payment_base += 10
    if payment_base > (balance_new * annualInterestRate / 12):
        for i in range(12):
            balance_new -= payment_base
            balance_new += (balance_new * annualInterestRate / 12)
print 'Lowest Payment: %s' % (payment_base)



# 2nd Appraoch:

balance = 4213; annualInterestRate = 0.2; monthlyPaymentRate = 0.04
finished = False;
pay = 0;
def year(pay,myBalance) :
    totalPaid = 0;
    for i in range(1,13):
        totalPaid += pay;
        myBalance = myBalance - pay;
        myBalance = myBalance + ((annualInterestRate/12.0) * myBalance);
        if myBalance<=0 :
            break;
    return myBalance;


while finished == False :
    pay += 10;
    z = year(pay,balance);
    if z <= 0 :
        finished = True;
        print("Lowest Payment: " + str(pay)); 







##### 3rd Appraoch:

balance = 4213; annualInterestRate = 0.2; 
monthly_interest_rate = annualInterestRate / 12.0
updated_balance = balance
paid = 0

while updated_balance > 0:
    paid += 10
    updated_balance = balance
    for month in range(1,13):
        monthly_unpaid_balance = updated_balance - paid
        updated_balance = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)
print 'Lowest Payment: ' + str(paid)




















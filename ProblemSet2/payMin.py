balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
totalPaid = 0
for i in range(12):
    print "Month: %d" % (i+1)
    print "Minimum monthly payment: %r" % round(monthlyPaymentRate * balance,2)
    print "Remaining balance: %r" % round((balance-monthlyPaymentRate*balance)*(1+annualInterestRate/12),2)
    totalPaid += monthlyPaymentRate * balance
    balance = (balance-monthlyPaymentRate*balance)*(1+annualInterestRate/12)
print "Total paid: %r" % round(totalPaid,2)
print "Remaining balance: %r" % round(balance,2)
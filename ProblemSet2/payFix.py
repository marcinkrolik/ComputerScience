def calcBalance(startBalance,fixedPay):
    balance = startBalance
    for i in range(12):
        balance = (balance-fixedPay)*(1+annualInterestRate/12)
    return balance
def calcb(i,fPay,sbalance):
    balance = (sbalance-fPay)*(1+annualInterestRate/12)
    if i != 0:
        i -= 1
        return calcb(i,fPay,balance)
    return balance

annualInterestRate = 0.2
balance = 3329
startBalance = balance
fixedPay = 0
while balance>0:
    fixedPay += 10
    balance = calcb(11,fixedPay,startBalance)
print "Lowest Payment: %d" % fixedPay
def calcBalance(startBalance,fixedPay):
    balance = startBalance
    for i in range(12):
        balance = (balance-fixedPay)*(1+annualInterestRate/12)
    return balance
annualInterestRate = 0.2
startBalance = 320000.0
fixedPay = 0
upperBound = startBalance*((1+annualInterestRate)**12)/12
lowerBound = startBalance/12
balance = 0
while abs(startBalance-balance)>=0.01:
    mid = (upperBound+lowerBound)/2
        
    return mid
# -*- coding: utf-8 -*-
"""
Computes lowest monthly payment in order to pay off a given loan with a given annual interest rate in a given amount of time

Monthly interest rate = (Annual interest rate) / 12.0
Monthly payment lower bound = Balance / 12
Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0

term = length of loan -> int
annualInterestRate = rate as a decimal. i.e 2% -> 0.02
balance = float or int without commas i.e. 12000
"""
def loanCalculator(balance, annualInterestRate, term):
        calc_balance = 1
        low = balance/12
        high = (balance * (1 +(annualInterestRate/12.0))**12)/12
        epsilon = 0.2
        calculating = True
        while calculating:
            minimumMonthlyPayment = (high + low)/2
            calc_balance = balance
            for i in range(term):
                monthlyUnpaidBalance = calc_balance - minimumMonthlyPayment
                updatedBalance = monthlyUnpaidBalance + ((annualInterestRate/12.0) * monthlyUnpaidBalance)
                calc_balance = round(updatedBalance,3)
            if abs(calc_balance) <= epsilon:
                calculating = False
            elif calc_balance > 0:
                low = minimumMonthlyPayment
            else:
                high = minimumMonthlyPayment
        return print('Lowest payment: ' + str(round(minimumMonthlyPayment,2)))




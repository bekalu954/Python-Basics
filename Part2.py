#Assignment 1-2

#add two numbers 
print (50 + 50) 
print (100 - 10)
'print (30 +* 6)' #invalid syntax operator
print (6 ^ 6)
print (6 ** 6)
print (6 + 6 + 6 + 6 + 6 + 6)

#Print output “Hello World : 10”
txt = "Hello World:{}"
num = 10
print(txt.format(num))

#Input loan amount. Then converts to float
loanAmount = input('Enter loan amount \n')
loanAmount = float(loanAmount)

# Input interest rate. Then converts to float and input interest rate is /100/12
interestRate = input('Enter Interest Rate \n')
interestRate = float(interestRate) / 100 / 12

#Total number of months
months = input('How many months will you have the loan? \n')
months = float(months)

# Formula to calculate monthly payments
mortgagePayment = loanAmount * ((interestRate * ((1 + interestRate) ** months)) / ((1 + interestRate) ** months - 1))
print("Answer: \n")
# Prints monthly payment on next line and reformat the string to a float using 2 decimal places
print(round(mortgagePayment))
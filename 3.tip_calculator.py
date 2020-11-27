pre_start = 'Welcome to the tip calculator'

total_bill = float(input("What was your total bill? $"))
percentage = int(input('What percentage tip would you like to give? 10, 12 or 15?'))
people = int(input('How many people to split the bill?'))

result = (total_bill / people) * float(1 + (percentage / 100))

message = f"each person should pay: ${round(result, 2)}"

print(message)


print("Welcome to love calculator")
name1 = input("What is your name?")
name2 = input("What is her name?")

name = (name1 + name2).lower()

tens = 0
ones = 0

true = 'true'
love = 'love'

for i in range(len(true)):
    tens += name.count(true[i])
    ones += name.count(love[i])

result = tens * 10 + ones
message = ""
if (result < 10) or (result > 90):
    message = f"Your score is {result}, you go together like coke and mentos."
elif (result >= 40) and (result <= 50):
    message = f"Your score is {result}, you are alright together"
else:
    message = f"Your socre is {result}"

print(message)
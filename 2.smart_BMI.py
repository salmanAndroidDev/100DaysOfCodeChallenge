pre_start = "****************** Welcome to Samrt BMI!!! ************************"

print(pre_start)
height = float(input("Insert Your Height In Meter: "))
weight = float(input("Insert Your Weight In kilogram: "))

BMI = weight / height ** 2
ideal_weight = 25 * (height ** 2)
bmi_state = ''

if BMI < 18.5:
    bmi_state = 'under weight'

elif 18.5 <= BMI and BMI < 25 :
    bmi_state = 'normal'

elif 25 <= BMI and BMI <= 30:
    bmi_state = 'over weight'

elif BMI < 30:
    bmi_state = 'obese'


pre_result = """
******************************************************************
******************* Result ***************************************
"""
print(pre_result)

if bmi_state is 'normal':
    print("your BMI is ", BMI , ' which means you are in the best shape!')
elif BMI > 25:
    print('Your state is ', bmi_state, 'Your ideal weight is ', ideal_weight, ' try to lose ', weight - ideal_weight, 'killos')
else:
    print('Your state is ', bmi_state, 'Your ideal weight is ', ideal_weight, ' try to gain ', (ideal_weight - weight), 'killos')

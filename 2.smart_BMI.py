pre_start = """"
****************** Welcome to Samrt BMI!!! ************************
                    *********       **                   **    ************
                    *       *       *  *                * *         *  
                    *        *      *   *              *  *         *
                    *      *        *    *            *   *         *
                    *   *           *     *          *    *         *
                    * *             *      *        *     *         *
                    *   *           *       *      *      *         *  
                    *     *         *        *    *       *         *
                    *       *       *         *  *        *         *
                    *        *      *           *         *         *
                    **********      *                     *    ************
"""

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

elif BMI > 30:
    bmi_state = 'obese'


pre_result = """
******************************************************************
******************* Result ***************************************
"""
message = ""
if bmi_state is 'normal':
    message = f"your BMI is {round(BMI, 2)} which means you are in the best shape!"
elif BMI > 25:
    message = f'Your state is {bmi_state} Your ideal weight is {round(ideal_weight, 2)} try to lose {round(weight - ideal_weight, 2)} killos'
else:
    message = f'Your state is  {bmi_state} Your ideal weight is  {round(ideal_weight, 2)} try to gain {round(ideal_weight - weight, 2)} killos'

print(pre_result, message)
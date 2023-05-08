# Constants for calculation
WATER_PER_KG = 0.033 # liters of water per kilogram of body weight
MALE_MULTIPLIER = 5
FEMALE_MULTIPLIER = -161
PREGNANCY_ADDITION = 300 # additional ml of water per day for pregnant women

# User input
while True:
    sex = input("Enter your sex (male/female): ").lower()
    if sex not in ['male', 'female']:
        print("Invalid input for sex. Please enter 'male' or 'female'.")
    else:
        if sex == 'female':
            while True:
                is_pregnant = input("Are you pregnant? (yes/no): ").lower()
                if is_pregnant not in ['yes', 'no']:
                    print("Invalid input for pregnancy status. Please enter 'yes' or 'no'.")
                else:
                    break
        break

while True:
    try:
        age = int(input("Enter your age (in years): "))
        if age < 0 or age > 120:
            print("Invalid input for age. Please enter an age between 0 and 120.")
        else:
            break
    except ValueError:
        print("Invalid input for age. Please enter a valid integer.")

while True:
    try:
        height = int(input("Enter your height (in cm): "))
        if height < 50 or height > 300:
            print("Invalid input for height. Please enter a height between 50 and 300 cm.")
        else:
            break
    except ValueError:
        print("Invalid input for height. Please enter a valid integer.")

while True:
    try:
        weight = int(input("Enter your weight (in kg): "))
        if weight < 10 or weight > 500:
            print("Invalid input for weight. Please enter a weight between 10 and 500 kg.")
        else:
            break
    except ValueError:
        print("Invalid input for weight. Please enter a valid integer.")



# Calculate BMR using Harris-Benedict equation
if sex == 'male':
    bmr = (MALE_MULTIPLIER * weight) + (6.25 * height) - (5 * age) + 5
else:
    bmr = (FEMALE_MULTIPLIER * weight) + (6.25 * height) - (5 * age) - 161

# Calculate daily water intake
water_intake = bmr * WATER_PER_KG
if sex == 'female' and is_pregnant == 'yes':
    water_intake += PREGNANCY_ADDITION
mL_a_day = water_intake * 1000 

'''
250mL = a cup 
nums = mL_a_day / 250 = # intervals
drink each 16/nums hour assuming the user is awake 16 hours a day
'''
time_interval = 16// (mL_a_day / 250)

# Print result
print("Your recommended daily water intake is {:.2f} liters.".format(water_intake))

# Constants for calculation
WATER_PER_KG = 0.033 # liters of water per kilogram of body weight
MALE_MULTIPLIER = 5
FEMALE_MULTIPLIER = -161
PREGNANCY_ADDITION = 300 # additional ml of water per day for pregnant women

def calculate_intake(sex, is_pregnant, height, weight, age):
    # Calculate BMR using Harris-Benedict equation
    if sex == 'male':
        bmr = (MALE_MULTIPLIER * weight) + (6.25 * height) - (5 * age) + 5
    else:
        bmr = (FEMALE_MULTIPLIER * weight) + (6.25 * height) - (5 * age) - 161
    # Calculate daily water intake
    water_intake = bmr * WATER_PER_KG
    if sex == 'female' and is_pregnant == 'yes':
        water_intake += PREGNANCY_ADDITION
    return water_intake


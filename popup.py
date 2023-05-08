import tkinter as tk
from tkinter import messagebox
from functools import partial
import water

# Function to handle submit button click
def on_submit_click(sex_var, is_pregnant_var, height_var, weight_var, age_var):
    sex = sex_var.get()
    is_pregnant = is_pregnant_var.get()
    height = height_var.get()
    weight = weight_var.get()
    age = age_var.get()
    
    # Check for invalid input
    if height <= 0 or weight <= 0 or age <= 0:
        messagebox.showerror("Error", "Invalid input")
        return
    
    # Calculate recommended water intake
    intake = calculate_intake(sex, is_pregnant, height, weight, age)

    '''
    250mL = a cup 
    nums = mL_a_day / 250 = # intervals
    drink each 16/nums hour assuming the user is awake 16 hours a day
    '''
    time_interval = 16// (intake * 1000 // 250)



    # Print result
    print("Your recommended daily water intake is {:.2f} liters.".format(water_intake))

    # Show message with recommended water intake
    message = f"Your recommended daily water intake is {intake} ml"
    messagebox.showinfo("Result", message)
    

# Create GUI window
window = tk.Tk()
window.title("Water Intake Calculator")

# Add sex selection buttons
sex_var = tk.StringVar(value="M")
male_button = tk.Radiobutton(window, text="Male", variable=sex_var, value="M")
female_button = tk.Radiobutton(window, text="Female", variable=sex_var, value="F")
male_button.pack()
female_button.pack()

# Add pregnancy selection buttons
is_pregnant_var = tk.BooleanVar(value=False)
pregnant_button = tk.Checkbutton(window, text="Pregnant", variable=is_pregnant_var, onvalue=True, offvalue=False)
pregnant_button.pack()

# Add height slider
height_var = tk.IntVar(value=160)
height_label = tk.Label(window, text="Height (cm):")
height_label.pack()
height_slider = tk.Scale(window, from_=50, to=250, orient=tk.HORIZONTAL, variable=height_var)
height_slider.pack()

# Add weight slider
weight_var = tk.IntVar(value=60)
weight_label = tk.Label(window, text="Weight (kg):")
weight_label.pack()
weight_slider = tk.Scale(window, from_=10, to=200, orient=tk.HORIZONTAL, variable=weight_var)
weight_slider.pack()

# Add age slider
age_var = tk.IntVar(value=30)
age_label = tk.Label(window, text="Age (years):")
age_label.pack()
age_slider = tk.Scale(window, from_=1, to=120, orient=tk.HORIZONTAL, variable=age_var)
age_slider.pack()

# Add submit button
submit_button = tk.Button(window, text="Submit", command=partial(on_submit_click, sex_var, is_pregnant_var, height_var, weight_var, age_var))
submit_button.pack()

# Start GUI event loop
window.mainloop()

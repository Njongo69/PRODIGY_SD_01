import tkinter as tk
from tkinter import messagebox

#Conversion Functions
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return fahrenheit_to_celsius(fahrenheit) + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))

# Conversion Logic
def convert_temperature():
    try:
        value = float(entry_temperature.get())
        unit = unit_var.get()
        
        if unit == 'Celsius':
            fahrenheit = celsius_to_fahrenheit(value)
            kelvin = celsius_to_kelvin(value)
            result = f"{value}°C is {fahrenheit:.2f}°F and {kelvin:.2f}K."
        elif unit == 'Fahrenheit':
            celsius = fahrenheit_to_celsius(value)
            kelvin = fahrenheit_to_kelvin(value)
            result = f"{value}°F is {celsius:.2f}°C and {kelvin:.2f}K."
        elif unit == 'Kelvin':
            celsius = kelvin_to_celsius(value)
            fahrenheit = kelvin_to_fahrenheit(value)
            result = f"{value}K is {celsius:.2f}°C and {fahrenheit:.2f}°F."
        else:
            result = "Invalid unit selected."
        
        messagebox.showinfo("Conversion Result", result)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid numerical temperature.")

# GUI Setup
root = tk.Tk()
root.title(" NJONGO Temperature Converter")

# Input Frame
frame_input = tk.Frame(root)
frame_input.pack(pady=10)

tk.Label(frame_input, text="Enter Temperature:").grid(row=0, column=0, padx=5, pady=5)
entry_temperature = tk.Entry(frame_input)
entry_temperature.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Select Unit:").grid(row=1, column=0, padx=5, pady=5)

unit_var = tk.StringVar(value="Celsius")
unit_menu = tk.OptionMenu(frame_input, unit_var, "Celsius", "Fahrenheit", "Kelvin")
unit_menu.grid(row=1, column=1, padx=5, pady=5)

# Convert Button
button_convert = tk.Button(root, text="Convert", command=convert_temperature)
button_convert.pack(pady=10)

# Run the GUI Loop
root.mainloop()

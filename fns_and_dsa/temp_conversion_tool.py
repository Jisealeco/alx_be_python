# define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACOTR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

#implement conversion functions
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACOTR
def convert_to_fahrenheit(celsius):
    return (CELSIUS_TO_FAHRENHEIT_FACTOR * celsius) + 32

# user interface
def main():

    temp = float(input("Enter the temperature to convert: "))
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

    if unit == "F":
     converted = convert_to_celsius(temp)
     print(f"{temp}F is equal to {converted:} C")
    elif unit == "C":
     converted = convert_to_fahrenheit(temp)
     print(f"{temp}C is equal to {converted:}F")
    else:
     print(f"Invalid temperature")
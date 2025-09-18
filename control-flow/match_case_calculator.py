# Prompt for User Input
num1 = float(input("Enter the firt number: "))
num2 = float(input("Enter the second number: "))

# prompt user for operation:
operation = "Choose the operation (+, -, *, /):"

# Perform the Calculation Using Match Case:
match operation:
 case "+":
    result = num1 + num2
    print(f"The result is {result}")
 case "-":
    result = num1 - num2
    print(f"The result is {result}")
 case "*":
    result = num1 * num2
    print(f"The result is {result}")
 case "/":
  if num2 != 0:
    result = num1 / num2
    print(f"The result is {result}")
  else:
    print("Error: Division by zero is not allowed.")
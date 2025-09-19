# Prompt user for inputs
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Process the Task Based on Priority and Time Sensitivity
match priority:
    case "high":
        print(f"Reminder: '{task}' is a high priority task.")
        if time_bound == "yes":
            print("that requires immediate attention today!")
    case "medium":
        print(f"Reminder: '{task}' is a medium priority task.")
        if time_bound == "yes":
            print("that requires immediate attention today!")
    case "low":
        print(f"Reminder: '{task}' is a low priority task.")
        if time_bound == "yes":
            print("that requires immediate attention today!")
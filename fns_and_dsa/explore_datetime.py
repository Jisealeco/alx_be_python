from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time:", formatted_date)


def calculate_future_date():
    number_of_days = int(input("Enter number of days to add to current date: "))
    future_date =  datetime.now() + timedelta(days=number_of_days)
    formatted_future = future_date.strftime("%Y-%m-%d")
    print(f"Future date:", formatted_future)
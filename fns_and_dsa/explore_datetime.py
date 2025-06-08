import datetime
def display_current_datetime():
    now = datetime.datetime.now()
    formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_now}")
    return formatted_now
def calculate_future_date(days_to_add):
    now = datetime.datetime.now()
    future_date = now + datetime.timedelta(days=days_to_add)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")
    return formatted_future_date
if __name__ == "__main__":
    display_current_datetime()
    days = int(input("Enter the number of days to add to the current date: "))
    calculate_future_date(days)
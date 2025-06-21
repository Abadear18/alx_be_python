from datetime import datetime, timedelta

def display_current_datetime():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

def calculate_future_date(days_to_add):
    future_date = datetime.now() + timedelta(days=days_to_add)
    return future_date.strftime("%Y-%m-%d")

def main():
    print("Current date and time:", display_current_datetime())
    days = int(input("Enter the number of days to add to the current date: "))
    print("Future date:", calculate_future_date(days))

if __name__ == "__main__":
    main()

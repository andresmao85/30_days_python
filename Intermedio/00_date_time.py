# Get the current day, month, year, hour, minute and timestamp from datetime module
from datetime import datetime

now = datetime.now()
print("Day:", now.day)
print("Month:", now.month)
print("Year:", now.year)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Timestamp:", now.timestamp())

# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print(formatted_date)

# Today is 5 December, 2019. Change this time string to time.
date_string = "5 December, 2019"
date_object = datetime.strptime(date_string, "%d %B, %Y")
print(date_object)

# Calculate the time difference between now and new year.
new_year = datetime(2026,1,1)
time_difference = new_year - now
print(time_difference)
days = time_difference.days
seconds = time_difference.seconds
hours = seconds // 3600
minutes = (seconds % 3600) // 60
print(f"{days} days, {hours} hours, {minutes} minutes left until New Year!")

# Calculate the time difference between 1 January 1970 and now.
old_date = datetime(1970,1,1)
time_difference = now - old_date
print(time_difference)


import datetime

my_time = "Jan 15, 2023 - 12:05:33"

python_date = datetime.datetime.strptime(my_time, '%b %d, %Y - %H:%M:%S')

full_name_month = python_date.strftime('month: %B')

print(full_name_month)

new_data = python_date.strftime("%d.%m.%Y, %H:%M")
print(new_data)

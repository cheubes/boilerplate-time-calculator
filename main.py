# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main

# print('\nadd_time("3:30 PM", "2:12")\t|' + add_time("3:30 PM", "2:12") + '|\n')
# print('\nadd_time("3:30 PM", "2:12")\t|' + add_time("3:30 PM", "2:12") + '|\n')
# print('\nadd_time("11:55 AM", "3:12")\t|' + add_time("11:55 AM", "3:12") + '|\n')
# print('\nadd_time("9:15 PM", "5:30")\t|' + add_time("9:15 PM", "5:30") + '|\n')
# print('\nadd_time("11:40 AM", "0:25")\t|' + add_time("11:40 AM", "0:25") + '|\n')
# print('\nadd_time("2:59 AM", "24:00")\t|' + add_time("2:59 AM", "24:00") + '|\n')
# print('\nadd_time("11:59 PM", "24:05")\t|' + add_time("11:59 PM", "24:05") + '|\n')
# print('\nadd_time("8:16 PM", "466:02")\t|' + add_time("8:16 PM", "466:02") + '|\n')
# print('\nadd_time("5:01 AM", "0:00")\t|' + add_time("5:01 AM", "0:00") + '|\n')
# print('\nadd_time("3:30 PM", "2:12", "Monday")\t|' + add_time("3:30 PM", "2:12", "Monday") + '|\t5:42 PM, Monday\n')
# print('\nadd_time("2:59 AM", "24:00", "saturDay")\t|' + add_time("2:59 AM", "24:00", "saturDay") + '|\t2:59 AM, Sunday (next day)\n')
# print('\nadd_time("11:59 PM", "24:05", "Wednesday")\t|' + add_time("11:59 PM", "24:05", "Wednesday") + '|\t12:04 AM, Friday (2 days later)\n')
# print('\nadd_time("8:16 PM", "466:02", "tuesday")\t|' + add_time("8:16 PM", "466:02", "tuesday") + '|\t6:18 AM, Monday (20 days later)\n')

# Run unit tests automatically
main(module='test_module', exit=False)

# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main


# add_time("3:30 PM", "2:12")
# add_time("11:55 AM", "3:12")
# add_time("9:15 PM", "5:30")
# add_time("11:40 AM", "0:25")
# add_time("2:59 AM", "24:00")

# Run unit tests automatically
main(module='test_module', exit=False)

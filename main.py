import helper
import functions
from art import tprint

tprint("deadline dude")

user_input = input("Enter your goal with a deadline separated by a colon.\n")

goal = functions.return_goal(user_input)
deadline = functions.return_deadline(user_input)

validate_deadline = helper.validate_date_input(deadline)

if validate_deadline == False:
    print("\n You suck! Game over..\n")
    SystemExit
else:
    days_till = functions.calculate_days(deadline)
    hours_till = functions.calculate_hours(deadline)
    print(f"\n hi there! Time remaining for your goal: {goal} is {days_till.days} days, or {hours_till} hours.\n")

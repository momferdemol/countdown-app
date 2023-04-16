from datetime import datetime


def return_goal(user_input):
    input_list = user_input.split(":")
    goal = input_list[0]
    return goal


def return_deadline(user_input):
    input_list = user_input.split(":")
    deadline = input_list[1]
    return deadline


def calculate_days(deadline):
    deadline = datetime.strptime(deadline, "%d-%m-%Y")
    today_date = datetime.today()
    days_till = deadline - today_date
    return days_till


def calculate_hours(deadline):
    deadline = datetime.strptime(deadline, "%d-%m-%Y")
    today_date = datetime.today()
    time_till = deadline - today_date
    hours_till = int(time_till.total_seconds() / 60 / 60)
    return hours_till


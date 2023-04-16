from dateutil.parser import parse


def validate_date_input(deadline):

    isValidDate = True
    try:
        parse(deadline)
    except ValueError:
        isValidDate = False
        SystemExit

    return isValidDate

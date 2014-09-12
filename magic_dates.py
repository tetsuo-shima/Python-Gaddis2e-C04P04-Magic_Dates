__author__ = 'dwight'

# The date June 10, 1960, is special because when it is written in the following format, the month times the day equals
# the year: 6/10/60. Design a program that asks the user to enter a month (in numeric form), a day, and a two-digit
# year. The program should then determine whether the month times the day equals the year. If so, it should display a
# message saying the date is magic. Otherwise, it should display a message saying the date is not magic.


def main():
    month = (int(input('Enter month (num): ')))
    day = (int(input('Enter day of month: ')))

    # truncate century
    year = (int(input("Enter year: "))) % 100

    if not is_date_valid(month,day,year):
        print('Error: Date is invalid.')
    elif is_date_magic(month, day, year):
        print('Date is magic!')
    else:
        print('Date is not magic.')


def is_date_valid(month, day, year):
    if is_date_boundary_invalid(month, day, year):
        return False

    if is_february_invalid(month, day, year):
        return False

    if is_30_day_month_invalid(month, day):
        return False

    return True


def is_date_boundary_invalid(month, day, year):
    if month < 1 or month > 12:
        return False

    if day < 1 or day > 31:
        return False

    if year < 1:
        return False

    return True


def is_february_invalid(month, day, year):
    if month == 2 and day > 29:
        return False

    if month == 2 and (year % 4 != 0) and day > 28:
        return False

    return True


def is_30_day_month_invalid(month, day):
    if (month == 4 or month == 6 or month == 9 or month == 11) and day > 30:
        return False

    return True


def is_date_magic(month, date, year):
    if (month * date) == year:
        return True
    else:
        return False


main()
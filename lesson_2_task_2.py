def is_year_leap(year):
    if (year % 4 == 0):
        return True
    else:
        return False


my_year = 2021
result = is_year_leap(my_year)
print("Год " + str(my_year) + ":" + str(result))

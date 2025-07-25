def month_to_season(n):
    if (3 <= n <= 5):
        print("Весна")
    elif (6 <= n <= 8):
        print("Лето")
    elif (9 <= n <= 11):
        print("Осень")
    else:
        if (n > 12):
            print("Номер месяца указан неверно")
        else:
            print("Зима")


month_to_season(12)

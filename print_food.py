FOOD_DICT = {"Carrot": 0.2, "Grass": 0.4, "Celery": 0.1, "Spinach": 0.3}

number = 1

for food in FOOD_DICT:
        print("{}.  {} - {} point/s".format(number, food.title(), FOOD_DICT.get(food)))
        number += 1


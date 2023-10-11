# request user input, record time it took to input the city (for word chain game)

import time

# import regex
import re

def get_city():
    start_time = time.time()
    city = input("Введите следующий город: ")
    # check for validity - only russian letters or spaces, dashes
    # 
    while not re.match(r'^[а-яА-ЯёЁ\s-]+$', city):
        print("Некорректный ввод. ")
        city = input("Введите следующий город: ")

    end_time = time.time()

    return city, end_time - start_time
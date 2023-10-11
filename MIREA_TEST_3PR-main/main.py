from loader import load_cities

from input import get_city

from random_city import choose_random_city

from previous_letter import check_letters

from city_adder import add_city_to_used

from city_already_used_checker import is_city_used

# write a word chain game on cities

path = "cities.txt"
time_limit = 10

cities = load_cities(path)

used_cities = []

# choose initial city
city = choose_random_city(cities, used_cities)

used_cities = add_city_to_used(used_cities, city)

print(f"Начнем с {city}.")

players = ["Игрок 1", "Игрок 2"]
current_player = 0

turn_time = 0

while True:
    
    print()
    print(f"Ходит {players[current_player]}. Осталось {(time_limit - turn_time):.2f} секунд.")

    city, time = get_city()

    turn_time += time

    if turn_time > time_limit:
        print("Время вышло, вы проиграли.")
        break

    if city not in cities:
        print("Я не знаю такого города")
        continue

    if is_city_used(used_cities, city):
        print("Этот город уже был")
        continue

    if not check_letters(used_cities[-1], city):
        print("Город должен начинаться на последнюю букву предыдущего")
        continue

    used_cities = add_city_to_used(used_cities, city)

    print(f"Вы ввели {city}")

    current_player = (current_player + 1) % 2

    turn_time = 0


from random_city import choose_random_city


def test_from_list():
    cities = ["Москва", "Архангельск"]
    used_cities = ["Москва"]

    result = choose_random_city(cities, used_cities)

    assert result in cities

def test_not_from_used():
    cities = ["Москва", "Архангельск"]
    used_cities = ["Москва"]
    
    result = choose_random_city(cities, used_cities)

    assert result not in used_cities

def test_last_letter():
    cities = ["Москва", "Архангельск"]
    used_cities = ["Москва"]

    result = choose_random_city(cities, used_cities)

    assert used_cities[-1][-1].upper() == result[0]

def test_no_answers():
    cities = ["Москва", "Пермь"]
    used_cities = ["Москва"]

    result = choose_random_city(cities, used_cities)

    assert result is None

def test_last_letter_exclusive():
    cities = ["Москва", "Пермь"]
    used_cities = ["Пермь"]

    result = choose_random_city(cities, used_cities)

    assert result == "Москва"

def test_no_used_cities():
    cities = ["Москва", "Пермь"]
    used_cities = []

    result = choose_random_city(cities, used_cities)

    assert result in cities
from city_adder import add_city_to_used

def test_add_city_to_used_correct():
    city_list = ["Москва", "Нижний Новгород"]
    city = "Пермь"

    result = add_city_to_used(city_list, city)

    assert result == ["Москва", "Нижний Новгород", "Пермь"]

def test_add_city_to_used_list_type_error():
    city_list = "Москва"
    city = "Пермь"

    result = add_city_to_used(city_list, city)

    assert result == None

def test_add_city_to_used_city_type_error_list():
    city_list = ["Москва", "Нижний Новгород"]
    city = ["Пермь"]

    result = add_city_to_used(city_list, city)

    assert result == None

def test_add_city_to_used_city_type_error_int():
    city_list = ["Москва", "Нижний Новгород"]
    city = 1

    result = add_city_to_used(city_list, city)

    assert result == None
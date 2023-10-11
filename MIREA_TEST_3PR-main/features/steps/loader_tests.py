# using behave, test that cities are loaded from file

from behave import given, when, then

from loader import load_cities

import re

@given('a file with cities')
def step_impl(context):
    context.path = 'cities.txt'

@when('I load cities from file')
def step_impl(context):
    context.cities = load_cities(context.path)

@then('I get a list of cities')
def step_impl(context):
    assert type(context.cities) == list

@then('the list is not empty')
def step_impl(context):
    assert len(context.cities) > 0

@then('the list contains only strings')
def step_impl(context):
    for city in context.cities:
        assert type(city) == str

@then('the list contains only russian letters, spaces and dashes')
def step_impl(context):
    for city in context.cities:
        assert re.match(r'^[а-яА-ЯёЁ\s-]+$', city)

@then('the list contains Москва, Санкт-Петербург, Казань')
def step_impl(context):
    print(context.cities)
    assert 'Москва' in context.cities
    assert 'Санкт-Петербург' in context.cities
    assert 'Казань' in context.cities

@then("the list doesn't contain Алмата, Пекин, Токио")
def step_impl(context):
    assert 'Алмата' not in context.cities
    assert 'Пекин' not in context.cities
    assert 'Токио' not in context.cities



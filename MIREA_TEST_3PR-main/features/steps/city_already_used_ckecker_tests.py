from behave import given, when, then

from city_already_used_checker import is_city_used

import re


@given('a list of city`s')
def step_impl(context):
    context.city_list = ['Москва', "Нижний Новгород"]


@given('a city')
def step_impl(context):
    context.city = 'Москва'


@given('a one city`s (string)')
def step_impl(context):
    context.city_list = 'Москва'


@given('a city that`s doesn`t used')
def step_impl(context):
    context.city = 'Сызрань'


@when("I check the city's entry in the list")
def step_impl(context):
    context.is_aready_used = is_city_used(context.city_list, context.city)


@then("I get a True")
def step_impl(context):
    assert context.is_aready_used == True


@then("I get a None")
def step_impl(context):
    assert context.is_aready_used == None


@then("I get a False")
def step_impl(context):
    assert context.is_aready_used == False

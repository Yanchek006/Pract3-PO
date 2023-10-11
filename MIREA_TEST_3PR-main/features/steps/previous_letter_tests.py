from behave import given, when, then

from previous_letter import check_letters

@given("a previous city")
def step_impl(context):
    context.previous_city = "Артём"

@given("a previous city — case")
def step_impl(context):
    context.previous_city = "Пермь"

@given("a new city")
def step_impl(context):
    context.new_city = "Москва"

@given("a new city — wrong")
def step_impl(context):
    context.new_city = "Санкт-Петербург"

@when("I check letters equality")
def step_impl(context):
    context.check = check_letters(context.previous_city, context.new_city)

@then("I get True")
def step_impl(context):
    assert context.check == True

@then("I get False")
def step_impl(context):
    assert context.check == False
Feature: check the city's entry in the list

    Scenario: check the city's entry in the list type correct (True)
        Given a list of city`s
        Given a city
        When I check the city's entry in the list
        Then I get a True
    
    Scenario: check the city's entry in the list type incorrect (None)
        Given a one city`s (string)
        Given a city
        When I check the city's entry in the list
        Then I get a None

    Scenario: check the city's entry in the list type (False)
        Given a list of city`s
        Given a city that`s doesn`t used
        When I check the city's entry in the list
        Then I get a False
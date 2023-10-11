Feature: Loading cities from file

    Scenario: Loading cities from file
        Given a file with cities
        When I load cities from file
        Then I get a list of cities
        Then the list is not empty
        Then the list contains only strings
        Then the list contains only russian letters, spaces and dashes
        Then the list contains Москва, Санкт-Петербург, Казань
        Then the list doesn't contain Алмата, Пекин, Токио

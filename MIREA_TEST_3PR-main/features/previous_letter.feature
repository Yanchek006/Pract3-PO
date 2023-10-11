Feature: check letters equality

    Scenario: last letter equal first letter (True)
        Given a previous city
        Given a new city
        When I check letters equality
        Then I get True

    Scenario: last letter equal first letter (False)
        Given a previous city
        Given a new city — wrong
        When I check letters equality
        Then I get False
    
    Scenario: last letter equal first letter (ъ, ь, ы, й cases) (True)
        Given a previous city — case
        Given a new city
        When I check letters equality
        Then I get True

    Scenario: last letter equal first letter (ъ, ь, ы, й cases) (False)
        Given a previous city — case
        Given a new city — wrong
        When I check letters equality
        Then I get False
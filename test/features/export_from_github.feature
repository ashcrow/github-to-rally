Feature: Export tasks from Github
    In order to get issues from Github
    As any user
    I want to export issues from Github

    Scenario: Export issues from Github
        Given I have the user ashcrow
        And I have the repo github-to-rally
        And I look up to 5 days back
        When I execute the Github export
        Then I get a list of results

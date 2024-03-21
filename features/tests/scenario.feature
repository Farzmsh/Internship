Feature: Testing Reelly.io

  Scenario: User can filter the Secondary deals by “want to buy” option
    Given Open the main page
    And Log in to the page
    When Click on Secondary option at the left side menu
    And Verify the Secondary page opens
    Then Filter the products by want to buy
    And Verify all cards have “want to buy” tag

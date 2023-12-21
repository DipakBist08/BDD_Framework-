Feature: Shopping Cart Swag Lab
   Scenario: Add item to cart

    Given Launch Chrome Browser

    When Open the Login Page
    And Input User Name "standard_user" and User Password "secret_sauce"
    Then Click on Login Button
    Then I am at Product Page
    Then I add an item to the cart
    Then Check the Cart if there are added items







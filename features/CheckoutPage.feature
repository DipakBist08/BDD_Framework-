Feature: Checkout Process

  Scenario: Verify the Standard_user user can perform a checkout
    Given Open Chrome Browser
    When I Open Swag Lab WebPage
    And Provide User Name "standard_user" and Password "secret_sauce"
    And Click on Login Button
    And Add Items to the cart
    And Go to the Cart
    And Click on Checkout Button
    And Fill Shipping Details
    And Click on Continue Button
    Then Check out OverView and Click on Finish


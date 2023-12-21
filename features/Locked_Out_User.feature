Feature: Locked Out User

  Scenario: Verify you cannot log in with user: locked_out_user
    Given Launch Chrome Browser
    When Open Swag Lab Login Page
    And Input Locked_Out  User Name "locked_out_user" and Password "secret_sauce"
    Then Click on Login Button
    Then The Locked_out_User Should not able to get Login into Swag Lab WebPage
    Then Close Browser

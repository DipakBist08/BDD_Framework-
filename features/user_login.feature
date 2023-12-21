Feature: Login to Swag Lab Web

  Scenario: verify that User Login to Swag Lab and and Navigate to Products Page
    Given Launch Chrome Browser
    When Open Swag Lab Login Page
    And Input valid User Name "standard_user" and Password "secret_sauce"
    And Click on Login Button
    Then User Should have redirected into Product page
    Then Close Browser


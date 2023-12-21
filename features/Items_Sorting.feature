Feature: Sorting Functionality

  Scenario: Verify sorting by Name (A to Z)
    Given Launch Chrome Browser
    When Open Swag Lab Login Page
    And Input User Name "standard_user" and Password "secret_sauce"
    And Click on Login Button
    And Open Swag Lab Product Page
    And Select "Name (A to Z)" sorting option
    Then Verify Products are sorted by Name (A to Z)

  Scenario: Verify sorting by Name (Z to A)
    Given Launch Chrome Browser
    When Open Swag Lab Login Page
    And Input User Name "standard_user" and Password "secret_sauce"
    And Click on Login Button
    And Open Swag Lab Product Page
    And Select "Name (Z to A)" sorting option
    Then Verify Products are sorted by Name (Z to A)

  Scenario: Verify sorting by Price(Low to High)
    Given Launch Chrome Browser
    When Open Swag Lab Login Page
    And Input User Name "standard_user" and Password "secret_sauce"
    And Click on Login Button
    And Open Swag Lab Product Page
    And Select "Price (Low to High)" sorting option
    Then Verify Products are sorted by Price (Low to High)

  Scenario: Verify sorting by Price( High to Low)
    Given Launch Chrome Browser
    When Open Swag Lab Login Page
    And Input User Name "standard_user" and Password "secret_sauce"
    And Click on Login Button
    And Open Swag Lab Product Page
    And Select "Price (High to Low)" sorting option
    Then Verify Products are sorted by Price (High to Low)




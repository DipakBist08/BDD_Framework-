Feature: Scenario Outline
Scenario Outline: Verify that set of login user can able to get login to Swag Lab
    Given I Launch Chrome Browser
    When I Open Swag Lab Login Page
    And Enter userName "<userName>" and password "<password>"
    And I Click on Login Button
    Then User Must Successfully get login with valid credentials
    Examples:
      |userName               | password   |
      |standard_user          |secret_sauce|
      |locked_out_user        |secret_sauce|
      |problem_user           |secret_sauce|
      |performance_glitch_user|secret_sauce|
      |error_user             |secret_sauce|
      |error_user             |secret_sauce|

#This will execute 6 times with different set of data

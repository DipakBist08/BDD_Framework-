from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@given('Launch Chrome Browser')
def LaunchBrowser(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


@when('Open Swag Lab Login Page')
def OpenLoginPage(context):
    context.driver.get('https://www.saucedemo.com/')


@when(u'Input Locked_Out  User Name "{userName}" and Password "{userPass}"')
def step_impl(context,userName,userPass):
    user_input = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.ID, 'user-name')))
    password_input = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.ID, 'password')))

    user_input.clear()
    user_input.send_keys(userName)
    password_input.clear()
    password_input.send_keys(userPass)
    time.sleep(3)


@when('Click on Login Button')
def ClickOnLoginButton(context):
    login_button = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.ID, 'login-button')))
    login_button.click()
    time.sleep(5)

@then('The Locked_out_User Should not able to get Login into Swag Lab WebPage')
def ErrorMessage(context):
    error_message = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@data-test="error"]')))
    assert error_message.is_displayed(), "Expected error message for invalid credentials"
    time.sleep(5)

@then('Close Browser')
def CloseBrowser(context):
    context.driver.quit()

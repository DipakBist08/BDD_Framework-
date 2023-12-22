from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import time


@given(u'I Launch Chrome Browser')
def LaunchBrowser(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    time.sleep(5)


@when(u'I Open Swag Lab Login Page')
def LoginPage(context):
    context.driver.get('https://www.saucedemo.com/')


@when('Enter userName {"userName"} and password {"userPass"}')
def LoginCredentials(context, userName, userPass):
    u_Name = context.driver.find_element(By.ID, 'user-name')
    u_pass = context.driver.find_element(By.ID, 'password')
    u_Name.send_keys(userName)
    u_pass.send_keys(userPass)


@then('I Click on Login Button')
def LoginButton(context):
    login_btn = context.driver.find_element(By.ID, 'login-button')
    login_btn.click()
    time.sleep(10)


@when('User Must Successfully get login with valid credentials')
def SuccessfulLogin(context):
    try:
        txt=context.driver.find_element(By.XPATH,'//*[@id="header_container"]/div[2]/span').text
    except:
        context.driver.close()
        assert False,"Test Failled"
    if txt=="Products":
        assert True,"Test Passed"




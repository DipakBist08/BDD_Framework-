from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@when('Input valid User Name "{userName}" and Password "{userPass}"')
def UserLoginDetails(context, userName, userPass):
    user_input = context.driver.find_element(By.ID, 'user-name')
    password_input = context.driver.find_element(By.ID, 'password')

    user_input.send_keys(userName)
    password_input.send_keys(userPass)
    time.sleep(5)


@then('User Should have redirected into Product page')
def ProductPage(context):
    product_page = context.driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span').text
    assert product_page == "Products", "You are not in Product Page.|Passed|"

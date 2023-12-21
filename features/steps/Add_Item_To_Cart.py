from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@when('Open the Login Page')
def LoginPage(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://www.saucedemo.com/')
    assert True


@when('Input User Name "{userName}" and User Password "{userPass}"')
def UserLogin(context, userName, userPass):
    user_input = context.driver.find_element(By.ID, 'user-name')
    password_input = context.driver.find_element(By.ID, 'password')

    user_input.send_keys(userName)
    password_input.send_keys(userPass)


@then('Click on Login Button')
def Login(context):
    loginButton = context.driver.find_element(By.XPATH, '//*[@id="login-button"]')
    loginButton.click()


@then(u'I am at Product Page')
def ProductPage(context):
    page_title = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="header_container"]/div[2]/span')))
    assert page_title.text == 'Products', "You are  on the product page"


@then(u'I add an item to the cart')
def CheckCart(context):
    item_to_add = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')))
    item_to_add.click()
    remove_button = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="remove-sauce-labs-backpack"]')))
    assert remove_button.is_displayed(), "Item not added to cart"


@then('Check the Cart if there are added items')
def CheckCart(context):
    cart_icon = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="shopping_cart_container"]/a')))
    cart_icon.click()

    added_item = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="remove-sauce-labs-backpack"]')))
    assert added_item.is_displayed(), "Item not found in the cart"

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select


@given(u'Open Chrome Browser')
def LaunchBrowser(context):
    context.driver = webdriver.Chrome()


@when('I Open Swag Lab WebPage')
def LoginPage(context):
    context.driver.get('https://www.saucedemo.com/')


@when('Provide User Name "{Name}" and Password "{PWD}"')
def LoginCredentials(context, Name, PWD):
    user_input = context.driver.find_element(By.ID, 'user-name')
    password_input = context.driver.find_element(By.ID, 'password')

    user_input.send_keys(Name)
    password_input.send_keys(PWD)


@when('Add Items to the cart')
def AddItems(context):
    add_item1 = context.driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack')
    add_item1.click()
    add_item2 = context.driver.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light')
    add_item2.click()


@when('Go to the Cart')
def GotoCart(context):
    go_cart = context.driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
    go_cart.click()


@when('Click on Checkout Button')
def CheckOutButton(context):
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    checkout_button = context.driver.find_element(By.ID, 'checkout')
    checkout_button.click()


@when('Fill Shipping Details')
def ShippingDetails(context):
    First_Name = context.driver.find_element(By.ID, 'first-name')
    Last_Name = context.driver.find_element(By.ID, 'last-name')
    Postal_Code = context.driver.find_element(By.ID, 'postal-code')
    First_Name.send_keys('Deepak')
    Last_Name.send_keys('Bista')
    Postal_Code.send_keys('14600')
    context.driver.execute_script("window.scrollBy(0, 500);")


@when('Click on Continue Button')
def ContinueButton(context):
    click_on_countinue_btn = context.driver.find_element(By.ID, 'continue')
    click_on_countinue_btn.click()


@then(u'Check out OverView and Click on Finish')
def FinishButton(context):
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    Finish_Button = context.driver.find_element(By.ID, 'finish')
    Finish_Button.click()

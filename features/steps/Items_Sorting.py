from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select


@when('Input User Name "{userName}" and Password "{userPass}"')
def step_impl(context, userName, userPass):
    user_input = context.driver.find_element(By.ID, 'user-name')
    password_input = context.driver.find_element(By.ID, 'password')

    user_input.send_keys(userName)
    password_input.send_keys(userPass)
    time.sleep(5)


@when('Open Swag Lab Product Page')
def ProductPage(context):
    page_title = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="header_container"]/div[2]/span')))
    assert page_title.text == 'Products', "You are  on the product page"


@when('Select "Name (A to Z)" sorting option')
def SelectAtoZ(context):
    sort_dropdown = context.driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select')
    select = Select(sort_dropdown)
    select.select_by_visible_text('Name (A to Z)')


@then('Verify Products are sorted by Name (A to Z)')
def VerifyAtoZ(context):
    sorted_elements = context.driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
    sorted_values = [element.text for element in sorted_elements]
    is_sorted = all(sorted_values[i] <= sorted_values[i + 1] for i in range(len(sorted_values) - 1))
    assert is_sorted, "Sorting by Name (A to Z) is not working correctly"
    print("Products are sorted by Name (A to Z)")


@when('Select "Name (Z to A)" sorting option')
def SelectZtoA(context):
    sort_dropdown = context.driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select')
    select = Select(sort_dropdown)
    select.select_by_visible_text('Name (Z to A)')


@then('Verify Products are sorted by Name (Z to A)')
def VerifyZtoA(context):
    sorted_elements = context.driver.find_element(By.XPATH, '//*[@id="item_3_title_link"]/div')
    sorted_values = [element.text for element in sorted_elements]
    is_sorted = all(sorted_values[i] <= sorted_values[i + 1] for i in range(len(sorted_values) - 1))
    assert is_sorted, "Sorting by Name (Z to A) is not working correctly"
    print("Products are sorted by Name (Z to A)")


@when('Select "Price (Low to High)" sorting option')
def SelectLowtoHigh(context):
    sort_dropdown = context.driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select')
    select = Select(sort_dropdown)
    select.select_by_visible_text('Name (low to high)')


@then('Verify Products are sorted by Price (low to high)')
def VerifyLowtoHigh(context):
    sorted_elements = context.driver.find_element(By.XPATH,
                                                  '//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div')
    sorted_values = [element.text for element in sorted_elements]
    is_sorted = all(sorted_values[i] <= sorted_values[i + 1] for i in range(len(sorted_values) - 1))
    assert is_sorted, "Sorting by Name (Low to High) is  working correctly"
    print("Products are sorted by Name (Low to High)")


@when('Select "Price (High to Low)" sorting option')
def SelectHightoLow(context):
    sort_dropdown = context.driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select')
    select = Select(sort_dropdown)
    select.select_by_visible_text('Name (High to Low)')


@then(u'Verify Products are sorted by Price (High to Low)')
def VerifyHightoLow(context):
    sorted_elements = context.driver.find_element(By.XPATH,
                                                  '//*[@id="inventory_container"]/div/div[3]/div[2]/div[2]/div')
    sorted_values = [element.text for element in sorted_elements]
    is_sorted = all(sorted_values[i] <= sorted_values[i + 1] for i in range(len(sorted_values) - 1))
    assert is_sorted, "Sorting by Name (High to Low) is  working correctly"
    print("Products are sorted by Name (High to Low)")

from behave import *
from selenium import webdriver

@when('я ya.ru')
def step_impl(context):
    driver = webdriver.Firefox()
    driver.get("https://ya.ru")

@when('я смотрю на картику')
def step_impl(context):
    pass
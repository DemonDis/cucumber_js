from splinter import Browser
from pytest_bdd import given, scenario, then, when
import time
# from selenium.webdriver.common.keys import Keys

browser = Browser('firefox')
# l = browser.find_element_by_class_name("search3__input mini-suggest__input")

@scenario('ya.feature', 'посещаю фронт')
def test_посещаю_фронт():
    """посещаю фронт."""
    pass


@when('я ya.ru')
def _():
    """я ya.ru."""
    browser.visit("http://www.ya.ru")
    print("No, it wasn't found... We need to improve our SEO techniques") 
    # browser.find_by_css('div[class="medium-widget success-story-category last"]:nth-child(2)').fill('splinter - python acceptance testing for web applications')
    browser.find_by_css('input[class="search3__input mini-suggest__input"]').fill('splinter - python acceptance testing for web applications')
    
    time.sleep(10) #sleep for 10 sec
    # browser.screenshot()
    # l.send_keys("Selenium")
    print("Yes, found it! :)")
    browser.quit()


# @when('я смотрю на картику')
# def _():
#     """я смотрю на картику."""
#     # raise NotImplementedError
#     pass


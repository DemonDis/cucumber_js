from splinter import Browser
from pytest_bdd import given, scenario, then, when
import time
# import logging

browser = Browser('firefox')

@scenario('ya.feature', 'посещаю фронт')
def test_посещаю_фронт():
    """посещаю фронт."""
    pass


@when('я ya.ru')
def _():
    """я ya.ru."""
    browser.visit("http://www.ya.ru")
    print("No, it wasn't found... We need to improve our SEO techniques")
    time.sleep(10) #sleep for 10 sec
    # browser.screenshot()
    print("Yes, found it! :)")
    browser.quit()

# @when('я смотрю на картику')
# def _():
#     """я смотрю на картику."""
#     # raise NotImplementedError
#     pass


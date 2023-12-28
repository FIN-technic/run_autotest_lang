import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-cathedral-the-bazaar_190/" #без кнопки

def test_check_button_basket(browser):
    button_basket = False
    try:
        browser.get(link)
        #time.sleep(10)
        browser.find_element(By.CSS_SELECTOR, ".btn-primary.btn-add-to-basket")
        button_basket = True
        print("button found")
    finally:
        assert button_basket is True, 'button not found'
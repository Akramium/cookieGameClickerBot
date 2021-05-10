from selenium import webdriver
import time

URL = "/Development/chromedriver.exe"
GAME_URL = "http://orteil.dashnet.org/experiments/cookie/"
driver = webdriver.Chrome(executable_path=URL)
driver.get(url=GAME_URL)

game_is_on = True
five_minutes = time.time() + 5 * 60


def clicking():
    cookie = driver.find_element_by_id("cookie")
    timeout = time.time() + 5
    while True:
        cookie.click()
        if time.time() > timeout:
            break


def buy():
    list_element = [
        driver.find_element_by_css_selector("#buyCursor b"),
        driver.find_element_by_css_selector("#buyGrandma b"),
        driver.find_element_by_css_selector("#buyFactory b"),
        driver.find_element_by_css_selector("#buyMine b"),
        driver.find_element_by_css_selector("#buyShipment b"),
        driver.find_element_by_xpath('//*[@id="buyAlchemy lab"]/b'),
        driver.find_element_by_css_selector("#buyPortal b"),
        driver.find_element_by_xpath('//*[@id="buyTime machine"]/b'),
    ]

    money = int(driver.find_element_by_id("money").text.replace(',', ''))

    store = [int(item.text.split("-")[1].strip().replace(',', '')) for item in list_element]
    can_buy = [money - item for item in store]

    list_element[can_buy.index(min([item for item in can_buy if item >= 0]))].click()


while game_is_on:
    clicking()
    buy()
    if time.time() > five_minutes:
        cookies_per_second = driver.find_element_by_id("cps").text
        print(cookies_per_second)
        break

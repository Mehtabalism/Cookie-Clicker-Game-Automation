from selenium import webdriver
import time

chrome_driver_path = "D:/Pycharm Projects/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element_by_id("cookie")

timeout = time.time() + 5
five_min = time.time() + 5*60

buy = {
    7: "buyTime machine",
    6: "buyPortal",
    5: "buyAlchemy lab",
    4: "buyShipment",
    3: "buyMine",
    2: "buyFactory",
    1: "buyGrandma",
    0: "buyCursor"
}

while True:
    cookie.click()

    if time.time() > timeout:
        money = int(driver.find_element_by_id("money").text.replace(",", ""))
        store = driver.find_elements_by_css_selector("#store b")
        prices = []
        for item in store:
            try:
                prices.append(int(item.text.split(" - ")[1].replace(",", "")))
            except IndexError:
                continue

        highest_price = 0
        for num in range(len(prices)):
            if money > prices[num] > highest_price:
                index = num
                highest_price = prices[num]

        driver.find_element_by_id(buy[index]).click()

        timeout += 5

    if time.time() > five_min:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        break

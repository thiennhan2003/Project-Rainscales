from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

def scrape_saucedemo():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.saucedemo.com")
    time.sleep(2)

    usernames = ["standard_user", "locked_out_user", "problem_user", "performance_glitch_user", "error_user", "visual_user"]
    password = "secret_sauce"
    product_data = []

    for username in usernames:
        driver.get("https://www.saucedemo.com")
        time.sleep(1)
        driver.find_element(By.ID, "user-name").clear()
        driver.find_element(By.ID, "password").clear()
        driver.find_element(By.ID, "user-name").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

        if "inventory" in driver.current_url:
            names = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
            prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
            for name, price in zip(names, prices):
                product_data.append({
                    "Username": username,
                    "Product Name": name.text,
                    "Price": price.text
                })

    driver.quit()

    df = pd.DataFrame(product_data)
    df.to_excel("saucedemo_products.xlsx", index=False)
    print("Đã lưu dữ liệu vào 'saucedemo_products.xlsx'")


if __name__ == "__main__":
    scrape_saucedemo()

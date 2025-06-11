from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

def scrape_masothue():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://thuvienphapluat.vn/ma-so-thue/tra-cuu-ma-so-thue-doanh-nghiep")
    time.sleep(3)

    all_data = {}
    page = 1

    while True:
        try:
            rows = driver.find_elements(By.CSS_SELECTOR, "table.table tbody tr")
            page_data = []

            for row in rows:
                cols = row.find_elements(By.TAG_NAME, "td")
                if len(cols) >= 3:
                    page_data.append({
                        "Tên Doanh Nghiệp": cols[0].text,
                        "Mã Số Thuế": cols[1].text,
                        "Ngày Cấp": cols[2].text
                    })

            all_data[f"Trang_{page}"] = pd.DataFrame(page_data)

            next_button = driver.find_elements(By.CSS_SELECTOR, "a.page-link")[-1]
            if "»" in next_button.text and "disabled" not in next_button.get_attribute("class"):
                next_button.click()
                page += 1
                time.sleep(2)
            else:
                break
        except Exception as e:
            print(f"Lỗi trang {page}: {e}")
            break

    driver.quit()

    with pd.ExcelWriter("masothue_data.xlsx") as writer:
        for sheet_name, df in all_data.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)

    print("Đã lưu dữ liệu vào 'masothue_data.xlsx'")


if __name__ == "__main__":
    scrape_masothue()

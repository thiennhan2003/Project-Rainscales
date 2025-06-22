from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from datetime import datetime
import time
import os

# Cấu hình trình duyệt
options = Options()
options.add_argument("--start-maximized")
prefs = {
    "download.default_directory": os.getcwd(),
    "plugins.always_open_pdf_externally": True,
    "download.prompt_for_download": False
}
options.add_experimental_option("prefs", prefs)

# Khởi động trình duyệt
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10)

# Danh sách mã tra cứu
ma_tra_cuu_list = ["B1HEIRR8N0WP"]

# Danh sách kết quả
ket_qua = []

for ma in ma_tra_cuu_list:
    try:
        driver.get("https://www.meinvoice.vn/tra-cuu")
        time.sleep(1)

        input_box = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[placeholder='Nhập mã tra cứu hóa đơn']")))
        input_box.clear()
        input_box.send_keys(ma)

        btn_tra_cuu = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(., 'Tra cứu')]")))
        btn_tra_cuu.click()

        time.sleep(3)
        try:
            btn_tai = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//a[contains(@href, '.pdf') or contains(., 'Tải')]")))
            btn_tai.click()
            ket_qua.append({
                "Mã tra cứu": ma,
                "Kết quả": "Đã tải hóa đơn",
                "Thời gian": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
        except:
            ket_qua.append({
                "Mã tra cứu": ma,
                "Kết quả": "Không tìm thấy hóa đơn",
                "Thời gian": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })

    except Exception as e:
        ket_qua.append({
            "Mã tra cứu": ma,
            "Kết quả": f"Lỗi: {e}",
            "Thời gian": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

driver.quit()

df = pd.DataFrame(ket_qua)
file_out = f"ket_qua_hoadon_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
df.to_excel(file_out, index=False)
print(f"Đã ghi kết quả vào file: {file_out}")

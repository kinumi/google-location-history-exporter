import os
import time
from subprocess import CREATE_NO_WINDOW

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class LocationHistoryDriver:
    def __init__(self, headless=True, user_data_dir=None, profile_directory=None):
        # ドライバ取得
        chrome_ver = chromedriver_autoinstaller.get_chrome_version().split(".")[0]
        driver_path = f"./{chrome_ver}/chromedriver.exe"
        if not os.path.exists(driver_path):
            chromedriver_autoinstaller.install(True)
        # オプション設定
        options = Options()
        options.headless = headless
        if user_data_dir is not None:
            options.add_argument(f"--user-data-dir={user_data_dir}")
        if profile_directory is not None:
            options.add_argument(f"--profile-directory={profile_directory}")
        service = Service(driver_path)
        service.creationflags = CREATE_NO_WINDOW
        # ドライバインスタンス作成
        self.driver = webdriver.Chrome(driver_path, options=options, service=service)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def download(self):
        # ダウンロードページを開く
        self.driver.get("https://takeout.google.com/settings/takeout/custom/location_history")

        # 「次のステップ」をクリック
        link = self.driver.find_element(By.XPATH, '//*[@id="i7"]/div/div[2]/div[2]/div/button')
        link.click()
        time.sleep(1)

        # 「Google Drive」を選択する
        link = self.driver.find_element(By.XPATH, '//*[@id="i10"]/div/div[1]/div/div[2]/div[1]/div')
        link.click()
        time.sleep(1)
        link = self.driver.find_element(By.XPATH, '//*[@id="i10"]/div/div[1]/div/div[2]/div[1]/div/div[2]/div[2]')
        link.click()
        time.sleep(1)

        # 「エクスポートを作成」をクリック
        link = self.driver.find_element(By.XPATH, '//*[@id="i10"]/div/div[2]/div/div/button')
        link.click()
        time.sleep(5)

        # パスワードを聞かれたかチェックして、
        # 聞かれている場合は保存されているものでそのままOKする
        link = self.driver.find_elements(By.XPATH, '//*[@id="passwordNext"]/div/button')
        if len(link) > 0:
            link[0].click()
            time.sleep(10)

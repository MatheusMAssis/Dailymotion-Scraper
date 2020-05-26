### importing libraries
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
import time

class AIOScraper:
    def __init__(self, driver_path, downloader_url):
        self.driver_path = driver_path
        self.driver = webdriver.Chrome(self.driver_path)
        self.downloader_url = downloader_url


    ################
    # ACCESS ZONE
    ################

    def access_videodownloader_page(self):
        self.driver.implicitly_wait(60)
        self.driver.get(self.downloader_url)

    def end_process(self):
        self.driver.close()


    ################
    # AUXILIAR ZONE
    ################

    def open_new_tab(self):
        self.driver.implicitly_wait(60)
        self.driver.execute_script('''window.open("http://google.com","_blank");''')
        self.driver.switch_to_window(self.driver.window_handles[1])

    def go_to_main_tab(self):
        self.driver.implicitly_wait(60)
        self.driver.close()
        self.driver.switch_to_window(self.driver.window_handles[0])


    ################
    # SCRAPING ZONE
    ################

    def insert_link(self, link):
        self.access_videodownloader_page()
        self.driver.implicitly_wait(60)
        input_box = self.driver.find_element_by_xpath("//input[@class='form-control']")
        input_box.send_keys(link)
        
    def generate_videos(self):
        self.driver.implicitly_wait(60)
        confirm_button = self.driver.find_element_by_xpath("//button[@class='btn btn-download text-white']")
        confirm_button.click()

    def get_download_video_link(self, index):
        time.sleep(20)
        self.driver.implicitly_wait(60)
        buttons_list = self.driver.find_elements_by_xpath("//a[@class='btn btn-sm btn-success']")
        download_link = buttons_list[index].get_attribute('href')
        return download_link
    
    def download_video(self, download_link):
        self.open_new_tab()
        time.sleep(1)
        self.driver.get(download_link)
        time.sleep(5)
        self.go_to_main_tab()

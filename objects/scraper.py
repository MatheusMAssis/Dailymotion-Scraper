### importing libraries
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import time

class DailymotionScraper:
    def __init__(self, driver_path, videos_url):
        self.driver_path = driver_path
        self.driver = webdriver.Chrome(self.driver_path)
        self.videos_url = videos_url


    ################
    # ACCESS ZONE
    ################

    def access_dailymotion_page(self):
        self.driver.implicitly_wait(60)
        self.driver.get(self.videos_url)

    def end_process(self):
        self.driver.close()


    ################
    # AUXILIAR ZONE
    ################

    def go_to_page_bottom(self):
        # TODO make it for as many scrolls as needed for any page
        time.sleep(8)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


    ################
    # SCRAPING ZONE
    ################

    def get_all_video_links(self):
        # TODO make it find that tag automatically and use it
        self.driver.implicitly_wait(60)
        self.go_to_page_bottom()
        elements_list = self.driver.find_elements_by_xpath("//a[@class='Video__details___1Knex']")
        return [element.get_attribute('href') for element in elements_list]

    

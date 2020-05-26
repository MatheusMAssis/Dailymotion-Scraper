### importing libraries
import objects.scraper as scraper
import objects.downloader as downloader

################
# VARIABLES ZONE
################

driver_path = "C:/Users/Matheus/Desktop/Matheus/Code/Drivers/chromedriver.exe"
aio_url = "https://allinonedownloader.com/"
dailymotion_url = "https://www.dailymotion.com/SilverTiggy/videos"


################
# SCRIPTS ZONE
################

def dailymotion_script():
    ### OBJECT
    DM = scraper.DailymotionScraper(driver_path, dailymotion_url)

    ### SCRIPT
    DM.access_dailymotion_page()
    DM.go_to_page_bottom()
    result_list = DM.get_all_video_links()
    DM.end_process()
    return result_list

def aio_script(link_list):
    ### OBJECT
    AIO = downloader.AIOScraper(driver_path, aio_url)

    ### SCRIPT
    AIO.access_videodownloader_page()
    for link in link_list:
        AIO.insert_link(link)
        AIO.generate_videos()
        download_link = AIO.get_download_video_link(4)
        AIO.download_video(download_link)
    AIO.end_process()


################
# MAIN ZONE
################

if __name__ == "__main__":
    link_list = dailymotion_script()
    aio_script(link_list)
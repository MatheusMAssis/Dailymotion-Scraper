### importing libraries
import objects.scraper as scraper
import objects.downloader as downloader
import objects.directory as directory

################
# VARIABLES ZONE
################

driver_path = "C:/Users/Matheus/Desktop/Matheus/Code/Drivers/chromedriver.exe"
aio_url = "https://allinonedownloader.com/"
dailymotion_url = "https://www.dailymotion.com/SilverTiggy/videos"
files_path = "C:/Users/Matheus/Downloads/*"
final_destination = "C:/Users/Matheus/Desktop/Xiaolin_Showdown"

################
# AUXILIAR ZONE
################

def fix_title(title):
    title = title.replace(':', '') #removing : from string
    title = title.replace('- ', '') #removing - from string
    final_title = title.replace(' ', '_') #binding it with _ instead of space
    return final_title


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
    titles_list = DM.get_all_video_titles()
    DM.end_process()
    return result_list, titles_list

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

def directory_script(title_list, n_files):
    ### OBJECT
    DIR = directory.FixDirectory(files_path, final_destination, n_files)

    ### SCRIPT
    recent_files = DIR.get_recent_files()
    desired_files = DIR.get_main_files(recent_files)
    DIR.change_directory_and_title(desired_files, title_list)


################
# MAIN ZONE
################

if __name__ == "__main__":
    link_list, title_list = dailymotion_script()
    aio_script(link_list)
    directory_script(title_list, 52)
import shutil, os
import glob

class FixDirectory:
    def __init__(self, files_path, final_destination, n_files):
        self.files_path = files_path
        self.final_destination = final_destination
        self.n_files = n_files

    
    ################
    # AUXILIAR ZONE
    ################

    def fix_title(self, title):
        title = title.replace(':', '') #removing : from string
        title = title.replace('- ', '') #removing - from string
        final_title = title.replace(' ', '_') #binding it with _ instead of space
        return final_title


    ################
    # FIXING ZONE
    ################

    def get_recent_files(self):
        list_recent_files = glob.glob(self.files_path)
        list_recent_files.sort(key=os.path.getctime)
        return list_recent_files

    def get_main_files(self, list_recent_files):
        desired_files = list_recent_files[-self.n_files:]
        desired_files.sort(reverse=True)
        return desired_files

    def change_directory_and_title(self, desired_files, title_list):
        for i in range(len(desired_files)):
            ith_file, new_name = desired_files[i], self.fix_title(title_list[i])
            shutil.move(ith_file, self.final_destination + "\\" + new_name + ".mp4")
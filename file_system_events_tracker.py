import sys
import time
import random

import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/AADYA/Downloads"
#to_dir = "C:/Users/AADYA/Downloaded_Images"
#----------------------------------------><--------------------------------------------------#
dir_tree={
     "Image_Files":['.jpg','.jpeg','.png','.webp','.gif','.jfif'],
     "Video_Files":['.mp2','.m3p','.mp3','mp4','.m4p','.mpe','.mpeg','.mov','.avi','.m4v'],
     "Document_Files":['.ppt','.xls','.pdf','.txt','.csv','xlsx'],
     "Set-up_Files":['.bin','.exe','.cmd','.msi','.dmg']}
#----------------------------------------><--------------------------------------------------#

# Event Hanlder Class
class FileEventHandler(FileSystemEventHandler):
   
    #1_on_created
    def on_created(self, event):
        print("hey, (event.src_path) has been created")  
        time.sleep(1)

        
    
    #2_on_deleted
    def on_deleted(self, event):
        print("opps, someone deleted (event.src_path)")
    #3_on_modified
    def on_modified(self, event):
        print("hey, (event.src_path) has been modified")
    #4_on_moved
    def on_moved(self, event):
        print("(event.src_path) has been moved")
        


# Initialize Event Handler Class
event_handler = FileEventHandler()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()


#5_Write a exception for keyboardInterrupt
try:
      while True:
          time.sleep(2)
          print("running...")
except KeyboardInterrupt:  
    print("stopped")
    observer.stop()





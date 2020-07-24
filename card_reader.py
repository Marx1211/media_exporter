from string import ascii_uppercase
import os
import shutil
from datetime import datetime

def get_card():
    for sd_path in ascii_uppercase:
        if os.path.exists('%s:\\Fuji.ID' % sd_path):
            sd_path='%s:\\' % sd_path
            print('SD card mounted to ', sd_path)
            return sd_path + "DCIM\\741_FUJI\\"
    return ""

def set_destination():
    destination_path = ""
    while destination_path == "":
        destination_path = input('Write the folder name where you want the files to go: ')
        return "D:\\" + destination_path + ""

def move_by_date(origin):
    pics = os.listdir(origin)
    for picture in pics:
        if(picture.endswith('.RAF')):
            pic_date = os.path.getctime(origin + picture)
            print(datetime.fromtimestamp(pic_date))

sd_card = get_card()
while sd_card == "":
    print('Please plug in SD card and press any key to continue...', end="")
    input()
    sd_card = get_card()
dest = set_destination()
move_by_date(sd_card)

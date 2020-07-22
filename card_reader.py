from string import ascii_uppercase
import os

def get_card():
    for sd_path in ascii_uppercase:
        if os.path.exists('%s:\\Fuji.ID' % sd_path):
            sd_path='%s:\\' % sd_path
            print('SD card mounted to ', sd_path)
            return sd_path + ""
    return ""

sd_card = get_card()
while sd_card == "":
    print('Please plug in SD card and press any key to continue...', end="")
    input()
    sd_card = get_card()

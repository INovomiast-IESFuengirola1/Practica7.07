import configparser
import os
import platform

from colorama import Back, Fore, Style

config = configparser.ConfigParser()

config.read('./config.ini')

if platform.system() == config['DEFAULTS']['machine_os']:
    try:
        os.system("rm /s " config['DEFAULTS']['root_folder_name'])
        os.system("del " + os.getcwd() + "/config.ini")
    except:
        os.system("rm -r " + os.getcwd() + "\\" + config['DEFAULTS']['root_folder_name'])
        os.system("rm " + os.getcwd() + "/config.ini")
import shutil
import random
import configparser
import os

#values
list_of_files = []
path_to_rust = "none"

#config init
config = configparser.ConfigParser()

#init config values
def init_functions():
    global path_to_rust, debug
    config.read("config.ini")

    #values
    path_to_rust = config["MAIN_CONFIG"]["RUST_PATH"]
    debug = config["MAIN_CONFIG"]["DEBUG"]

#logger
def log(text):
    if debug == True:
        print("LOG: " + text)

#change path to rust
def change_path_to_rust(path):
    global path_to_rust
    if "RustClient.exe" in os.listdir(path):
        config["MAIN_CONFIG"]["RUST_PATH"] = f"{path}/temp"
        with open('config.INI', 'w+') as configfile:
            config.write(configfile)
        path_to_rust = config["MAIN_CONFIG"]["RUST_PATH"]
        log("path_changed_to " + path + "/temp")
        return True
    else:
        return False

#initialisating list of loading screen images
def init_files():
    global list_of_files
    for i in os.listdir(path_to_rust):
        if ".jpg" in i:
            log(i + " ADDED TO LIST")
            if not i in list_of_files:
                list_of_files.append(i)

#replacing pictures (multiple)
def replace(file_list_to_copy):
    if len(file_list_to_copy) == len(list_of_files):    #if number of pictures in folder equals number of pictures in game
        for i in len(list_of_files):
            os.remove(f"{path_to_rust}/{list_of_files[i]}")
            shutil.copy(file_list_to_copy[i], f"{path_to_rust}/{list_of_files[i]}")
            log(i + " REPLACED")
    else:   #else select random pictures to replace
        for i in list_of_files:
            os.remove(f"{path_to_rust}/{i}")
            shutil.copy(f"{random.choice(file_list_to_copy)}", f"{path_to_rust}/{i}")
            log(i + " REPLACED USING RANDOM")
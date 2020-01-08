import os
import datetime
import shutil
import time
import re

BACKUP_PATH = "./TestFolder/{0}"
WEEKLY_ARCHIVE_PATH = "./Archive/{0}"
PDX_HMI_PATH = "/PDX-HMI/"
SITE_HMI_PATH = "/SITE-HMI/"
UCC_PATH = "/UCC/"
FE_PATH = "/FE/"
DIRECTORY = "./"

SUNDAY = 6
SIX_MONTHS = 6*30


def create_daily_folder(name):
	folder_name = BACKUP_PATH.format(name)
	try:
		os.makedirs(folder_name)
		os.makedirs(folder_name + PDX_HMI_PATH)
		os.makedirs(folder_name + SITE_HMI_PATH)
		os.makedirs(folder_name + UCC_PATH)
		os.makedirs(folder_name + FE_PATH)
	except:
		print("Folder already exists")


def create_weekly_folder(name):
	folder_name = WEEKLY_ARCHIVE_PATH.format(name.strftime("%m-%d-%Y (Week#%U)"))
	try:
		os.makedirs(folder_name)

	except:
		print("Folder already exists")


def create_sub_directories(path):
	try:
		os.makedirs(path+PDX_HMI_PATH)
		os.makedirs(path+SITE_HMI_PATH)
		os.makedirs(path+UCC_PATH)
		os.makedirs(path+FE_PATH)
	except:
		print("Some paths already exists")


'''
Copy the most recent created directory
'''
def copy_directory(current_directory,date):
	shutil.copytree(current_directory, BACKUP_PATH.format(date))
	pass

import os
import datetime
import shutil

PATH= "./TestFolder/{0}"
WEEKLY_ARCHIVE="./Archive/{0}"

SUNDAY=7


def create_daily_folder(date):
	folder_name = PATH.format(date)
	try:
		os.makedirs(folder_name)
	except:
		print("Folder already exists")


def create_weekly_folder(date=datetime.datetime.now()):
	folder_name = WEEKLY_ARCHIVE.format(date.strftime("%m-%d-%Y (Week#%U)"))
	try:
		os.makedirs(folder_name)
	except:
		print("Folder already exists")


def remove_folder(date=datetime.datetime.now()):
	folder_name:create_weekly_folder() = WEEKLY_ARCHIVE.format(date.strftime("%m-%d-%Y (Week#%U)"))
	try:
		shutil.rmtree(folder_name)
	except:
		print("Uh oh...")
		pass


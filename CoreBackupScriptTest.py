from datetime import timedelta
from datetime import datetime
import unittest
import CoreBackupScript as cbs
import Config as config
import os
import shutil

class MyTestCase(unittest.TestCase):

	sunday_datestr  =  "2020-01-12"
	sunday_date  =  datetime.strptime(sunday_datestr, "%Y-%m-%d")

	def setUp(self) -> None:
		shutil.rmtree(cbs.WEEKLY_ARCHIVE_PATH[:-3], True)
		shutil.rmtree(cbs.BACKUP_PATH[:-3], True)

	def test_create_daily_folder(self):
		date = datetime.now()
		folder_name = date.strftime("%m-%d-%Y")
		cbs.create_daily_folder(folder_name)
		self.assertTrue(os.path.isdir(str.format(cbs.BACKUP_PATH, folder_name)))
		self.assertTrue(os.path.isdir(str.format(cbs.BACKUP_PATH+"/{1}", folder_name, cbs.PDX_HMI_PATH)))
		self.assertTrue(os.path.isdir(str.format(cbs.BACKUP_PATH+"/{1}", folder_name, cbs.FE_PATH)))
		self.assertTrue(os.path.isdir(str.format(cbs.BACKUP_PATH+"/{1}", folder_name, cbs.SITE_HMI_PATH)))
		self.assertTrue(os.path.isdir(str.format(cbs.BACKUP_PATH+"/{1}", folder_name, cbs.UCC_PATH)))

	def test_create_weekly_folder(self):
		date = self.sunday_date
		folder_name = date.strftime("%m-%d-%Y (Week#%U)")
		cbs.create_weekly_folder(date)
		self.assertTrue(os.path.isdir(str.format(cbs.WEEKLY_ARCHIVE_PATH, folder_name)))

	def test_copy_directory(self):
		old_date = self.sunday_date.strftime("%m-%d-%Y")
		cbs.create_daily_folder(old_date)
		new_date = datetime.now()
		new_copied_directory_name = new_date.strftime("%m-%d-%Y")
		cbs.copy_directory(str.format(cbs.BACKUP_PATH, old_date), new_copied_directory_name)
		self.assertTrue(os.path.isdir(str.format(cbs.BACKUP_PATH, new_copied_directory_name)))
		self.assertTrue(os.path.isdir(str.format(cbs.BACKUP_PATH, old_date)))
		self.assertTrue(os.path.isdir(cbs.BACKUP_PATH[:-3]))

	def test_read_from_backup_config_csv(self):
		project_list = config.read_project_sites(config.UCC_PROJECT_CONFIG_FILE)
		self.assertTrue(len(project_list)>0)



if __name__  == '__main__':
	unittest.main()

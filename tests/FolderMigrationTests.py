import os
import shutil
import unittest
from datetime import datetime, timedelta

import CoreBackupScript as Cbs


class FolderMigration(unittest.TestCase):

	sunday_datestr = "2020-01-12"
	sunday_date = datetime.strptime(sunday_datestr, "%Y-%m-%d")

	def setUp(self) -> None:
		shutil.rmtree(Cbs.WEEKLY_ARCHIVE_PATH[:-3], True)
		shutil.rmtree(Cbs.BACKUP_PATH[:-3], True)

	def test_create_daily_folder(self):
		date = datetime.now()
		folder_name = date.strftime("%m-%d-%Y")
		Cbs.create_daily_folder(folder_name)
		self.assertTrue(os.path.isdir(str.format(Cbs.BACKUP_PATH, folder_name)))
		self.assertTrue(os.path.isdir(str.format(Cbs.BACKUP_PATH + "/{1}", folder_name, Cbs.PDX_HMI_PATH)))
		self.assertTrue(os.path.isdir(str.format(Cbs.BACKUP_PATH + "/{1}", folder_name, Cbs.FE_PATH)))
		self.assertTrue(os.path.isdir(str.format(Cbs.BACKUP_PATH + "/{1}", folder_name, Cbs.SITE_HMI_PATH)))
		self.assertTrue(os.path.isdir(str.format(Cbs.BACKUP_PATH + "/{1}", folder_name, Cbs.UCC_PATH)))

	def test_create_weekly_folder(self):
		date = self.sunday_date
		folder_name = date.strftime("%m-%d-%Y (Week#%U)")
		Cbs.create_weekly_folder(date)
		self.assertTrue(os.path.isdir(str.format(Cbs.WEEKLY_ARCHIVE_PATH, folder_name)))

	def test_copy_directory(self):
		current_date = datetime.now()
		Cbs.create_daily_folder(current_date.strftime("%m-%d-%Y"))
		new_date = current_date - timedelta(1)
		new_copied_directory_name = new_date.strftime("%m-%d-%Y")
		Cbs.copy_directory(str.format(Cbs.BACKUP_PATH, current_date.strftime("%m-%d-%Y")), new_copied_directory_name)
		self.assertTrue(os.path.isdir(str.format(Cbs.BACKUP_PATH, new_copied_directory_name)))
		self.assertTrue(os.path.isdir(str.format(Cbs.BACKUP_PATH, current_date.strftime("%m-%d-%Y"))))
		self.assertTrue(os.path.isdir(Cbs.BACKUP_PATH[:-3]))

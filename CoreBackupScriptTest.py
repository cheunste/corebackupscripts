from datetime import timedelta
from datetime import datetime
import unittest
import CoreBackupScript as cbs
import CoreRoboCopy as robo
import Config as config
import os
import shutil

class MyTestCase(unittest.TestCase):

	sunday_datestr = "2020-01-12"
	sunday_date = datetime.strptime(sunday_datestr, "%Y-%m-%d")

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
		current_date = datetime.now()
		cbs.create_daily_folder(current_date.strftime("%m-%d-%Y"))
		new_date = current_date - timedelta(1)
		new_copied_directory_name = new_date.strftime("%m-%d-%Y")
		cbs.copy_directory(str.format(cbs.BACKUP_PATH, current_date.strftime("%m-%d-%Y")), new_copied_directory_name)
		self.assertTrue(os.path.isdir(str.format(cbs.BACKUP_PATH, new_copied_directory_name)))
		self.assertTrue(os.path.isdir(str.format(cbs.BACKUP_PATH, current_date.strftime("%m-%d-%Y"))))
		self.assertTrue(os.path.isdir(cbs.BACKUP_PATH[:-3]))

	def test_read_from_config_csv(self):
		project_list = config.read_project_sites(config.UCC_PROJECT_CONFIG_FILE)
		self.assertTrue(len(project_list)>0)


class RoboCopyTests(unittest.TestCase):
	test_include_file_name = "test12345"
	test_ignore_file_name = "test_12345"

	source_dir = "./source_directory"
	dest_dir = "./dest_directory/"

	def setUp(self) -> None:
		shutil.rmtree(self.source_dir, True)
		shutil.rmtree(self.dest_dir, True)

	def test_robocopy_to_backup_folder(self):
		os.makedirs(self.source_dir)
		os.makedirs(self.dest_dir)

		self.create_dummy_files(self.source_dir)
		robo.call_robo_copy(self.source_dir, self.dest_dir, "/e /XF *_*.dat *_*.txt")
		self.check_file_in_path(self.dest_dir, self.test_include_file_name)

	def create_dummy_files(self, directory):
		dummy_txt_file = open(str.format("./{0}/{1}.txt", directory, self.test_include_file_name), "w")
		dummy_txt_file.close()
		dummy_good_txt_file = open(str.format("./{0}/{1}.txt", directory, self.test_include_file_name), "w")
		dummy_good_txt_file.close()
		dummy_dat_file = open(str.format("./{0}/{1}.dat", directory, self.test_ignore_file_name), "w")
		dummy_dat_file.close()

	def check_file_in_path(self, path, filename):
		complete_file_path = path + filename + ".txt"
		self.assertTrue(os.path.isfile(complete_file_path))
		pass


if __name__ == '__main__':
	unittest.main()

from datetime import timedelta
from datetime import datetime
import unittest
import CoreBackupScript as Cbs
import CoreRoboCopy as Robo
import Config as Config
import zipfile
import os
import shutil


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

	def test_read_from_config_csv(self):
		project_list = Config.read_project_sites(Config.UCC_PROJECT_CONFIG_FILE)
		self.assertTrue(len(project_list)>0)


class RoboCopyTests(unittest.TestCase):
	test_include_file_name = "test12345"
	test_ignore_file_name = "test_12345"

	source_dir = "./source_directory"
	dest_dir = "./latest/"
	number_of_sub_folders = 7

	def setUp(self) -> None:
		shutil.rmtree(self.source_dir, True)
		shutil.rmtree(self.dest_dir, True)

	def test_robocopy_to_backup_folder(self):
		self._create_dummy_directories()
		self._create_dummy_files(self.source_dir)
		Robo.call_robo_copy(self.source_dir, self.dest_dir, "/E /XF *_*.dat *_*.txt")

		self._check_file_in_path(self.dest_dir, self.test_include_file_name)

	def test_zipping_project(self):
		zip_file_name="test_zip"
		self._create_dummy_directories()
		self._create_dummy_files(self.source_dir)
		Robo.zip_directory(self.source_dir, self.dest_dir, zip_file_name)

		self.assertTrue(os.path.isfile(self.dest_dir+zip_file_name+".zip"))
		zipped_test_project = zipfile.ZipFile(self.dest_dir+zip_file_name+".zip",'r')
		number_of_items_in_zipped_project = 0
		for item in zipped_test_project.namelist():
			number_of_items_in_zipped_project = number_of_items_in_zipped_project+1
			print(item)
		self.assertTrue(number_of_items_in_zipped_project == ((self.number_of_sub_folders**2)+self.number_of_sub_folders+3))

	def _create_dummy_directories(self):
		sub_directory="/sub/"
		os.makedirs(self.source_dir)
		os.makedirs(self.dest_dir)
		# Create some sub directories. Very arbitrary
		for x in range(0,self.number_of_sub_folders):
			for y in range(0, self.number_of_sub_folders):
				sub_directory_name = str.format("/{0}/{1}",x,y)
				os.makedirs(self.source_dir+sub_directory+sub_directory_name)

	def _create_dummy_files(self, directory):
		dummy_txt_file = open(str.format("./{0}/{1}.txt", directory, self.test_include_file_name), "w")
		dummy_txt_file.close()
		dummy_good_txt_file = open(str.format("./{0}/{1}.txt", directory, self.test_include_file_name), "w")
		dummy_good_txt_file.close()
		dummy_dat_file = open(str.format("./{0}/{1}.dat", directory, self.test_ignore_file_name), "w")
		dummy_dat_file.close()

	def _check_file_in_path(self, path, filename):
		complete_file_path = path + filename + ".txt"

		self.assertTrue(os.path.isfile(complete_file_path))


if __name__ == '__main__':
	unittest.main()

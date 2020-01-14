import os
import shutil
import unittest
import zipfile

from module import RoboCopyModule as Robo
from module import ConfigModule as Config


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
		Robo.call_robo_copy(self.source_dir, self.dest_dir, Robo.FLAGS)
		self._check_file_in_path(self.dest_dir, self.test_include_file_name+".txt")

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

	def test_call_robocopy_with_config(self):
		config_file = Config.UCC_PROJECT_CONFIG_FILE
		project_list = Config.read_project_sites(config_file)

		for project in project_list:
			hostname = project[0]
			ip_address = project[1]
			zip_file_name = project[2]

			f_drive = str.format(r"\\{0}\f$\\", ip_address)
			d_drive = str.format(r"\\{0}\d$\\", ip_address)

			print(f_drive)
			self.assertFalse(not hostname)
			self.assertFalse(not ip_address)
			self.assertFalse(not zip_file_name)

			Robo.call_robo_copy(ip_address, f_drive, Robo.FLAGS)
			Robo.call_robo_copy(ip_address, d_drive, Robo.FLAGS)

	def _create_dummy_directories(self):
		sub_directory="/sub/"
		os.makedirs(self.source_dir)
		os.makedirs(self.dest_dir)
		# Create some sub directories. Very arbitrary
		for x in range(0,self.number_of_sub_folders):
			for y in range(0, self.number_of_sub_folders):
				sub_directory_name = str.format("/{0}/{0}{1}", x, y)
				os.makedirs(self.source_dir+sub_directory+sub_directory_name)

	def _create_dummy_files(self, directory):
		dummy_txt_file = open(str.format("./{0}/{1}.txt", directory, self.test_include_file_name), "w")
		dummy_txt_file.close()
		dummy_good_txt_file = open(str.format("./{0}/{1}.txt", directory, self.test_include_file_name), "w")
		dummy_good_txt_file.close()
		dummy_dat_file = open(str.format("./{0}/{1}.dat", directory, self.test_ignore_file_name), "w")
		dummy_dat_file.close()

	def _check_file_in_path(self, path, filename):
		complete_file_path = path + filename
		self.assertTrue(os.path.isfile(complete_file_path))


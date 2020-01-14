import os
import unittest
import threading

from module import ConfigModule as Config


class ConfigurationTest(unittest.TestCase):

	def test_read_ucc_configuration_file(self):
		self.assertTrue(os.path.isfile(Config.UCC_PROJECT_CONFIG_FILE))
		ucc_config_list = Config.read_project_sites(Config.UCC_PROJECT_CONFIG_FILE)
		self.assertTrue(len(ucc_config_list) == 2)

	def test_read_site_hmi_configuration_file(self):
		self.assertTrue(os.path.isfile(Config.SITE_HMI_PROJECT_CONFIG_FILE))
		ucc_config_list = Config.read_project_sites(Config.SITE_HMI_PROJECT_CONFIG_FILE)
		self.assertTrue(len(ucc_config_list) == 2)

	def test_read_fe_configuration_file(self):
		self.assertTrue(os.path.isfile(Config.FE_PROJECT_CONFIG_FILE))
		ucc_config_list = Config.read_project_sites(Config.FE_PROJECT_CONFIG_FILE)
		self.assertTrue(len(ucc_config_list) == 2)

	def test_read_pdx_hmi_configuration_file(self):
		self.assertTrue(os.path.isfile(Config.PDX_HMI_PROJECT_CONFIG_FILE))
		ucc_config_list = Config.read_project_sites(Config.PDX_HMI_PROJECT_CONFIG_FILE)
		self.assertTrue(len(ucc_config_list) == 2)

	def test_get_config_list(self):
		config_list = Config.compile_config_list()
		self.assertTrue(len(config_list) == 4)

	def test_get_tuple_from_config_list(self):
		hostname = "HOSTNAME"
		ip_address = "xx.xx.xx.xxx"
		zip_file_name = "some_zip_file"

		test_list = [hostname,ip_address,zip_file_name]
		(tuple_hostname,tuple_ip,tuple_zip)= Config.read_project_sites(test_list)

		self.assertTrue(tuple_hostname == hostname)
		self.assertTrue(tuple_ip == ip_address)
		self.assertTrue(tuple_zip == zip_file_name)

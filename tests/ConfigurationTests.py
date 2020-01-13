import os
import unittest

from module import ConfigModule as Config


class ConfigurationTest(unittest.TestCase):

	def test_read_ucc_configuration_file(self):
		self.assertTrue(os.path.isfile(Config.UCC_PROJECT_CONFIG_FILE))
		ucc_config_list = Config.read_project_sites(Config.UCC_PROJECT_CONFIG_FILE)
		self.assertTrue(len(ucc_config_list) == 2)

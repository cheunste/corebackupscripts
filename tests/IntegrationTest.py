import unittest
import CoreBackupScript as backup_script


class IntegrationTest(unittest.TestCase):
	def argument_test(self):
		backup_script.use_robocopy()



if __name__ == '__main__':
	unittest.main()

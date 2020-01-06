from datetime import timedelta
import unittest
import CoreBackupScript
import datetime
import os
import shutil

class MyTestCase(unittest.TestCase):

	def test_create_daily_folder(self):
		date=datetime.datetime.now()
		folderName=date.strftime("%m-%d-%Y")
		CoreBackupScript.create_daily_folder(folderName)
		self.assertTrue(os.path.isdir(str.format("./TestFolder/{0}",folderName)))

	def test_create_weekly_folder(self):
		date=datetime.datetime.now()
		folderName=date.strftime("%m-%d-%Y (Week#%U)")
		CoreBackupScript.create_weekly_folder()
		self.assertTrue(os.path.isdir(str.format("./Archive/{0}",folderName)))

	def test_six_month_removal(self):
		sixMonths=6*30
		date=datetime.datetime.now()+timedelta(days=sixMonths)
		print(date)
		folderName=date.strftime("%m-%d-%Y (Week#%U)")
		CoreBackupScript.create_weekly_folder(date)
		self.assertTrue(os.path.isdir(str.format("./Archive/{0}",folderName)))
		CoreBackupScript.remove_folder(date)
		self.assertFalse(os.path.isdir(str.format("./Archive/{0}",folderName)))

	def doCleanups(self) -> None:
		shutil.rmtree("./TestFolder/",True)
		shutil.rmtree("./Archive/",True)

if __name__ == '__main__':
	unittest.main()

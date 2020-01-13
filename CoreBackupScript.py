import sys, getopt
from module import RoboCopyModule
from module import FolderModule
from module import ConfigModule


def use_robocopy():
	pass


def copy_to_backup():
	pass


if __name__ == 'main':
	try:
		opts,args = getopt.getopt(sys.argv[1:],"rc:v",["robocopy","copy"])
	except getopt.GetoptError as err:
		print(err)
		sys.exit(2)

	for o,a in opts:
		if o in ("-r","--robocopy"):
			use_robocopy()
			sys.exit()
		elif o in ("-c","--copy"):
			copy_to_backup()
			sys.exit()
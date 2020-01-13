from subprocess import call
import os,zipfile


def call_robo_copy(source_dir,dest_dir, *flags):
	#ROBOCOPY \\source\f$\whatever destination /XF *_*.dat *_*.txt
	call(["robocopy",source_dir,dest_dir, flags])
	pass


def zip_directory(source_directory,zip_file_path,zip_file_name="Test"):

	file_paths = _get_file_paths_inside_directory(source_directory)

	zip_file = zipfile.ZipFile(zip_file_path+zip_file_name+'.zip','w')
	with zip_file:
		for file in file_paths:
			zip_file.write(file)
	pass


def _get_file_paths_inside_directory(directory_name) -> []:

	file_paths = []

	for root, directories, files in os.walk(directory_name):
		for file_name in files:
			file_path = os.path.join(root, file_name)
			file_paths.append(file_path)

		for directory_name in directories:
			file_path = os.path.join(root, directory_name)
			file_paths.append(file_path)

	return file_paths
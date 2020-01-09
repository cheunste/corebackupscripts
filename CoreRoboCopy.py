from subprocess import call


def call_robo_copy(source_dir,dest_dir, *flags):
	#TODO: create a robocopy line similar to the following:
	#ROBOCOPY \\source\f$\whatever destination /XF *_*.dat *_*.txt
	call(["robocopy",source_dir,dest_dir, flags])
	pass

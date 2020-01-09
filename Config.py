import csv

UCC_PROJECT_CONFIG_FILE='UccProjectConfig.csv'
PDX_HMI_PROJECT_CONFIG_FILE='PdxHmiProjectConfig.csv'
SITE_HMI_PROJECT_CONFIG_FILE='SiteHmiProjectConfig.csv'
FE_PROJECT_CONFIG_FILE='FeProjectConfig.csv'

def read_project_sites(config_file_name)->list:
	with open(config_file_name) as config_file:
		config_file.__next__()
		site_project_csv = csv.reader(config_file)
		project_list=[]
		for row in site_project_csv:
			project_list.append(row)
		return project_list

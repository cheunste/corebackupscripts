import csv

UCC_PROJECT_CONFIG_FILE='UccProjectConfig.csv'
PDX_HMI_PROJECT_CONFIG_FILE='PdxHmiProjectConfig.csv'
SITE_HMI_PROJECT_CONFIG_FILE='SiteHmiProjectConfig.csv'
FE_PROJECT_CONFIG_FILE='FeProjectConfig.csv'

def read_project_sites(config_file)->list:
	with open(config_file) as f:
		f.__next__()
		site_project_csv = csv.reader(f)
		projectList=[]
		for row in site_project_csv:
			projectList.append(row)
		return projectList

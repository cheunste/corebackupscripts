import csv

UCC_PROJECT_CONFIG_FILE='config/UccProjectConfig.csv'
PDX_HMI_PROJECT_CONFIG_FILE='config/PdxHmiProjectConfig.csv'
SITE_HMI_PROJECT_CONFIG_FILE='config/SiteHmiProjectConfig.csv'
FE_PROJECT_CONFIG_FILE='config/FeProjectConfig.csv'
_REQUIRED_FIELD_LENGTH = 3


def read_project_sites(config_file_name) -> list:
	with open(config_file_name) as config_file:
		config_file.__next__()
		site_project_csv = csv.reader(config_file)
		project_list=[]
		for row in site_project_csv:
			if _is_number_of_fields_valid(row) and _is_field_name_valid(row):
				project_list.append(row)
		return project_list


def _is_number_of_fields_valid(row) -> bool:
	return len(row) == _REQUIRED_FIELD_LENGTH


def _is_field_name_valid(row) -> bool:
	for field in row:
		if not field:
			return False
	return True

from prefect import task
from biz_logic.pdf_handler import get_report_pages


@task
def get_report_as_single_string(company_name):
	"""
	Returns report by given company name 
	as one single string.

	Parameters:
		company_name (str): company name
	Returns:
		string representing entire report
	"""
	return ' '.join(map(str, get_report_pages(company_name)))

from pypdf import PdfReader
from enum import Enum

class Company(Enum):
	MICROSOFT = "esg_reports/microsoft_2022.pdf"
	AIRBNB = "esg_reports/airbnb_2021.pdf"

def test():
	reader = PdfReader("esg_reports/microsoft_2022.pdf")
	number_of_pages = len(reader.pages)
	page = reader.pages[0]
	text = page.extract_text()

	print(number_of_pages)
	print(text)


def get_report_file_path(company_name):
	"""
	Returns report file path 
	by given company name.
	"""
	if company_name.upper() in dir(Company):
		file_path = Company[company_name.upper()].value
	else:
		file_path = None 

	return file_path
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


def get_reader_with_report(company_name):
	"""
	Returns reader containing report by 
	given company name.
	"""
	return PdfReader(get_report_file_path(company_name))


def get_report_pages(company_name):
	"""
	Returns list containing each page in report 
	by given company name.
	"""
	unparsed_pages = get_reader_with_report(company_name).pages
	pages = []

	for page in unparsed_pages:
		pages.append(page.extract_text())

	return pages # Note: each page contains markdown such as '\n'. Remove those if LLM has issues with it.


def get_report_as_single_string(company_name='microsoft'): #Company name hardcoded during dev.
	"""
	Returns report by given company name 
	as one single string.
	"""
	return ' '.join(map(str, get_report_pages(company_name)))








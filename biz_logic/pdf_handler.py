from pypdf import PdfReader
from biz_logic.Company import Company


def get_report_file_path(company_name):
	"""
	Returns report file path 
	by given company name.

	Parameters:
		company_name (str): company name
	Returns:
		file_path (str): file path
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

	Parameters:
		company_name (str): company name
	Returns:
		pdfreader instance containing report
	"""
	return PdfReader(get_report_file_path(company_name))


def get_report_pages(company_name):
	"""
	Returns list containing each page in report 
	by given company name.

	Parameters:
		company_name (str): company name
	Returns:
		pages (lst): list containing strings representing pages
	"""
	unparsed_pages = get_reader_with_report(company_name).pages
	pages = []

	for unparsed_page in unparsed_pages:
		page = remove_line_breaks_from_page(unparsed_page.extract_text())
		pages.append(page)

	return pages


def remove_line_breaks_from_page(page):
	"""
	Return page without line break symbols.

	Parameters:
		page (str): page content as a string
	Returns:
		string representing page content without line break symbols
	"""
	return ' '.join(page.splitlines())



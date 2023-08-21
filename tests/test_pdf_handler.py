import pytest
from biz_logic.pdf_handler import get_report_file_path, remove_line_breaks_from_page

def test_get_report_file_path_not_none():
	assert get_report_file_path('airbnb') is not None

def test_get_report_file_path_is_none():
	assert get_report_file_path('airbnbs') is None

def test_remove_line_breaks_from_page():
	page = 'An Update on \nEnvironmental, Social, and \nGovernance (ESG) at Airbnb\nDecember 2021'

	result = remove_line_breaks_from_page(page)
	expected_result = 'An Update on  Environmental, Social, and  Governance (ESG) at Airbnb December 2021'

	assert result == expected_result


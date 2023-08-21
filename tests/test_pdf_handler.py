import pytest
from pdf_handler import get_report_file_path

def test_get_report_file_path_not_none():
	assert get_report_file_path('airbnb') is not None

def test_get_report_file_path_is_none():
	assert get_report_file_path('airbnbs') is None


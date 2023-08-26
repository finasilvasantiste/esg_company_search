from enum import Enum

class Company(Enum): # TODO: replace hardcoded files with pdf upload option.
	""" 
	Represents a company and 
	the file path to its report.
	"""
	MICROSOFT = "esg_reports/microsoft_2022.pdf"
	AIRBNB = "esg_reports/airbnb_2021.pdf"

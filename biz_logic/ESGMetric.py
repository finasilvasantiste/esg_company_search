from enum import Enum

class ESGMetric(Enum): 
	""" 
	Represents an ESG metric.
	"""
	CARBON_FOOTPRINT = "Carbon Footprint/GHG Emissions"
	WATER_USAGE = "Water Usage/Water Management"
	DIVERSITY_AND_INCLUSION = "Diversity and Inclusion"
	EXECUTIVE_COMPENSATION = "Executive Compensation"
	# Only a few metrics so start out with.

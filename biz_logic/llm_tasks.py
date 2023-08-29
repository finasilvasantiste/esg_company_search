from prefect import task
from biz_logic.ESGMetric import ESGMetric
from biz_logic.LLMBot import LLMBot

@task
def llm_ask_esg_questions(company, report):
	""" 
	Asks LLM bot ESG questions using given
	company name and report.

	Parameters:
		company_name (str): company name
		report (str): company report
	Returns:
		None
	"""
	first_report_half = LLMBot.cut_string_to_max_token_size(report)
	bot = LLMBot(company = company, report = first_report_half)

	# Commenting out the api calls to openai during dev.
	# bot.ask_question(topic = ESGMetric.CARBON_FOOTPRINT.value)
    # bot.ask_question(topic = ESGMetric.WATER_USAGE.value)
    # bot.ask_question(topic = ESGMetric.DIVERSITY_AND_INCLUSION.value)
    # bot.ask_question(topic = ESGMetric.EXECUTIVE_COMPENSATION.value)

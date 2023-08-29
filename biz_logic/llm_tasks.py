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
	print('INSIDE TASK!')
	# print(report[0:4000])
	# first_report_half = report[0:4000]
	# print(first_report_half)

	first_report_half = LLMBot.cut_string_to_max_token_size(report)
	# print(first_report_half)
	# print('DONE')
	# first_report_half = report[0:4000] # 4,097 token max for LLM engine
	# print(first_report_half)
	bot = LLMBot(company = company, report = first_report_half)

	# print('ABOUT TO ASK QUESTION')
	# Commenting out the api calls to openai during dev.
	bot.ask_question(topic = ESGMetric.CARBON_FOOTPRINT.value)
    # bot.ask_question(topic = ESGMetric.WATER_USAGE.value)
    # bot.ask_question(topic = ESGMetric.DIVERSITY_AND_INCLUSION.value)
    # bot.ask_question(topic = ESGMetric.EXECUTIVE_COMPENSATION.value)

    # print('TASK DONE')
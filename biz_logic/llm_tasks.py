from prefect import task


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
	first_report_half = report[0:4000] # 4,097 token max for LLM engine
	bot = LLMBot(company = company_name, report = first_report_half)

    # Commenting out the api calls to openai during dev.
    bot.ask_question(topic = ESGMetric.CARBON_FOOTPRINT.value)
    # bot.ask_question(topic = ESGMetric.WATER_USAGE.value)
    # bot.ask_question(topic = ESGMetric.DIVERSITY_AND_INCLUSION.value)
    # bot.ask_question(topic = ESGMetric.EXECUTIVE_COMPENSATION.value)

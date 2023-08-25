from biz_logic.pdf_handler import get_report_as_single_string
from biz_logic.LLMBot import LLMBot
from biz_logic.ESGMetric import ESGMetric

def main():
    company_name = 'airbnb' # Company name hardcoded during dev.
    report = get_report_as_single_string(company_name)
    first_report_half = report[0:4000] # 4,097 token max for LLM engine

    bot = LLMBot(company = company_name, report = first_report_half)

    # Commenting out the api calls to openai during dev.
    # bot.ask_question(topic = ESGMetric.CARBON_FOOTPRINT.value)
    # bot.ask_question(topic = ESGMetric.WATER_USAGE.value)
    # bot.ask_question(topic = ESGMetric.DIVERSITY_AND_INCLUSION.value)
    # bot.ask_question(topic = ESGMetric.EXECUTIVE_COMPENSATION.value)
    

if __name__ == "__main__":
    main()


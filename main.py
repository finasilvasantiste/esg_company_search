from biz_logic.pdf_handler import get_report_as_single_string
from biz_logic.LLMBot import LLMBot
from biz_logic.ESGMetric import ESGMetric

def main():
    company_name = 'airbnb' # Company name hardcoded during dev.
    report = get_report_as_single_string(company_name)
    first_report_half = report[0:4000] # 4,097 token max for LLM engine

    bot = LLMBot()
    # bot.ask_questions(company_name, report[0:4000]) # 4,097 token max for this engine
    bot.ask_question(company_name = company_name, 
        report = first_report_half, 
        esg_metric = ESGMetric.CARBON_FOOTPRINT.value)
    

if __name__ == "__main__":
    main()


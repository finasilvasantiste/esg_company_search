from biz_logic.pdf_handler import get_report_as_single_string
from biz_logic.openai_handler import LLMBot

def main():
    company_name = 'airbnb' # Company name hardcoded during dev.
    report = get_report_as_single_string(company_name)

    bot = LLMBot()
    bot.ask_questions(company_name, report[0:4000]) # 4,097 token max for this engine

    

if __name__ == "__main__":
    # company_name = 'airbnb' # Company name hardcoded during dev.
    # report = get_report_as_single_string(company_name)

    # engine = 'gpt-4-0613'
    # bot = LLMBot(engine)
    # bot.ask_questions(company_name, report)

    # print("Hello World!")
    main()


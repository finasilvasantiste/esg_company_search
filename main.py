from biz_logic.pdf_handler import get_report_as_single_string
from biz_logic.openai_handler import test, question_example

def main():
    print("Hello World!")

if __name__ == "__main__":
    company_name = 'airbnb' # Company name hardcoded during dev.
    report = get_report_as_single_string(company_name)

    # print(report)

    # test()
    question_example()
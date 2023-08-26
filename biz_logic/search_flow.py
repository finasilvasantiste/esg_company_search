from prefect import flow
from biz_logic.LLMBot import LLMBot
from biz_logic.ESGMetric import ESGMetric
from biz_logic.pdf_tasks import get_report_as_single_string

@flow
def esg_company_search(company_name):
    """ 
    Workflow which runs an ESG company search.
    """
    print('Hello flow!')
    report = get_report_as_single_string(company_name)
    # first_report_half = report[0:4000] # 4,097 token max for LLM engine

    # bot = LLMBot(company = company_name, report = first_report_half)
    
    print('Bye flow!')

if __name__ == "__main__":
    esg_company_search('airbnb')
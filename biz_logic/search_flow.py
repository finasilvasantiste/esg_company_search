from prefect import flow
from biz_logic.pdf_tasks import get_report_as_single_string
from biz_logic.llm_tasks import llm_ask_esg_questions

@flow
def esg_company_search(company_name):
    """ 
    Workflow which runs an ESG company search.

    Parameters:
        company_name (str): company name
    Returns:
        None
    """
    print('Hello flow!')
    report = get_report_as_single_string(company_name)
    llm_ask_esg_questions(company = company_name, report = report)
    
    print('Bye flow!')

if __name__ == "__main__":
    esg_company_search('airbnb')

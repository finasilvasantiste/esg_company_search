import openai
import configparser
from biz_logic.esg_handler import Metric


class LLMBot():
	config = configparser.ConfigParser()
	config.read_file((open(r'keys.cfg')))
	openai.api_key = config.get('OPENAI', 'ACCESS_KEY_ID')		
	
	def __init__(self):
		self.engine = 'text-davinci-003'	


	def ask_questions(self, company_name, report):
		context = report
		metric = Metric.CARBON_FOOTPRINT.value
		question = "What is {} doing about {}? Use the context provided. Use quotation marks whenever you are quoting from the context.".format(company_name, metric)

		response = openai.Completion.create(
		  engine=self.engine,
		  prompt=f"Question answering:\nContext: {context}\nQuestion: {question}",
		  max_tokens=300
		)

		answer = response.choices[0].text.strip()
		print(answer)	


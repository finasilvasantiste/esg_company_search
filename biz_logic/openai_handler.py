import openai
import configparser
from biz_logic.esg_handler import Metric

# config = configparser.ConfigParser()
# config.read_file((open(r'keys.cfg')))
# openai.api_key = config.get('OPENAI', 'ACCESS_KEY_ID')


class LLMBot():
	config = configparser.ConfigParser()
	config.read_file((open(r'keys.cfg')))
	openai.api_key = config.get('OPENAI', 'ACCESS_KEY_ID')		
	
	def __init__(self, engine='text-davinci-003'):
		self.engine = engine	


	def ask_questions(self, company_name, report):
		context = report
		metric = Metric.CARBON_FOOTPRINT.value
		question = "What is {} doing about {}? Use the context provided.".format(company_name, metric)

		response = openai.Completion.create(
		  engine=self.engine,
		  prompt=f"Question answering:\nContext: {context}\nQuestion: {question}",
		  max_tokens=200
		)

		answer = response.choices[0].text.strip()
		print(answer)	


# def test():
# 	# list models
# 	models = openai.Model.list()
# 	print(models)


# def question_example():
# 	context = "Albert Einstein was a German-born theoretical physicist who developed the theory of relativity."
# 	question = "Where was Albert Einstein born?"
# 	response = openai.Completion.create(
# 	  engine="text-davinci-003",
# 	  prompt=f"Question answering:\nContext: {context}\nQuestion: {question}",
# 	  max_tokens=50
# 	)

# 	answer = response.choices[0].text.strip()
# 	print(answer)


# def ask_esg_questions(company_name, esg_report):
# 	context = esg_report
# 	metric = Metric.CARBON_FOOTPRINT.value
# 	question = "What is {} doing about {}?".format(company_name, metric)
# 	# engine="text-davinci-003" # limit of 4k tokens
# 	engine="gpt-3.5-turbo-16k-0613"

# 	response = openai.Completion.create(
# 	  engine=engine,
# 	  prompt=f"Question answering:\nContext: {context}\nQuestion: {question}",
# 	  max_tokens=200
# 	)

# 	answer = response.choices[0].text.strip()
# 	print(answer)	


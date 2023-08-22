import openai
import configparser


class LLMBot():
	config = configparser.ConfigParser()
	config.read_file((open(r'keys.cfg')))
	openai.api_key = config.get('OPENAI', 'ACCESS_KEY_ID')		
	
	def __init__(self, company, report):
		self.company = company,
		self.report = report,
		self.engine = 'text-davinci-003'	

	def ask_question(self, esg_metric):
		context = self.report
		question = ("What is {} doing about {}? Use the context provided." +
		" Use quotation marks whenever you are quoting from the context.").format(self.company, esg_metric)

		response = openai.Completion.create(
		  engine=self.engine,
		  prompt=f"Question answering:\nContext: {context}\nQuestion: {question}",
		  max_tokens=300
		)

		answer = response.choices[0].text.strip()
		print('Question topic: \n {} \n'.format(esg_metric))
		print('Answer: \n {} \n\n'.format(answer))	


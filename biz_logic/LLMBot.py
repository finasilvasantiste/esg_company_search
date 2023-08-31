import openai
import configparser


class LLMBot():
	"""
	Represents a LLM (Large Language Model) Bot.
	It can answer questions about given topics relating 
	to a given report (max size 4,097 tokens).
	"""
	config = configparser.ConfigParser()
	config.read_file((open(r'keys.cfg')))
	openai.api_key = config.get('OPENAI', 'ACCESS_KEY_ID')		
	
	def __init__(self, company, report):
		self.company = company,
		self.report = report,
		self.engine = 'text-davinci-003' # 4,097 token max for this engine
		# TODO: add engine to init, in order to be able to choose between engines. Harcoded engine for now.

	def ask_question(self, topic):
		""" 
		Submits question about given topic to LLM.
		Prints out topic and its answer.

		Parameters:
			topic (str): question topic
		Returns:
			None
		"""
		question = ("What is {company} doing about {topic}? The context provided is {company}'s factsheet. " + 
			"Use the factsheet to answer the question. Use quotation marks whenever " + 
			"you are quoting from the factsheet.").format(company = self.company, topic = topic)

		response = openai.Completion.create(
		  engine=self.engine,
		  prompt=f"Question answering:\nContext: {self.report}\nQuestion: {question}",
		  max_tokens=400
		)

		answer = response.choices[0].text.strip()
		print('Question topic: \n {} \n'.format(topic))
		print('Answer: \n {} \n\n'.format(answer))	

	@staticmethod
	def cut_string_to_max_token_size(string_to_cut):
		"""
		Cuts given string to max token size of LLM.
		4,097 token max for LLM engine currently used.

		Parameters:
			string_to_cut (str): string to cut
		Returns:
			string cut to 4,097 tokens
		"""

		return string_to_cut[0:4097]

import openai
import configparser

config = configparser.ConfigParser()
config.read_file((open(r'keys.cfg')))
openai.api_key = config.get('OPENAI', 'ACCESS_KEY_ID')

def test():
	# list models
	models = openai.Model.list()
	print(models)


def question_example():
	context = "Albert Einstein was a German-born theoretical physicist who developed the theory of relativity."
	question = "Where was Albert Einstein born?"
	response = openai.Completion.create(
	  engine="text-davinci-003",
	  prompt=f"Question answering:\nContext: {context}\nQuestion: {question}",
	  max_tokens=50
	)

	answer = response.choices[0].text.strip()
	print(answer)
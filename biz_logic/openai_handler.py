import openai
import configparser

config = configparser.ConfigParser()
config.read_file((open(r'keys.cfg')))
openai.api_key = config.get('OPENAI', 'ACCESS_KEY_ID')

def test():
	# list models
	models = openai.Model.list()
	print(models)

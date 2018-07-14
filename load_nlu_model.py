from rasa_nlu.model import Metadata, Interpreter

test1 = "Tell me how I can get to the venue from Alexanderplatz"
test2 = "Sure thing, can you also tell me how I can get to the venue from Alexanderplatz"

def load_model():
	# where `model_directory points to the folder the model is persisted in`
	interpreter = Interpreter.load('models/current/nlu_model')
	print(interpreter.parse(test2))
	
if __name__ == '__main__':
	load_model()
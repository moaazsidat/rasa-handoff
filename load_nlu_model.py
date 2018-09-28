from rasa_nlu.model import Metadata, Interpreter
import pprint

pp = pprint.PrettyPrinter(indent=2)

test1 = "Tell me how I can get to the venue from Alexanderplatz"
test2 = (
    "Sure thing, can you also tell me how I can get to the venue from Alexanderplatz"
)

inp = input("enter input: ")


def load_model():
    # where `model_directory points to the folder the model is persisted in`
    print("processing...")
    interpreter = Interpreter.load("models/current/nlu_model")
    pp.pprint(interpreter.parse(inp))


if __name__ == "__main__":
    load_model()

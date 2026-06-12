import random
import pathlib

current_dir = pathlib.Path(__file__).parent

def get_random_joke():
    try:
        with open(current_dir / "jokes.txt", "r") as file:
            jokes = file.readlines()
            return random.choice(jokes).strip()
    except FileNotFoundError:
        print("No jokes file found.")
import json
import random

def load_prayers(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data['prayers']

def generate_daily_prayer(prayers):
    return random.choice(prayers)['text']

if __name__ == "__main__":
    prayers = load_prayers('prayers.json')
    print("Daily Prayer:")
    print(generate_daily_prayer(prayers))

import json
import random
import argparse

def load_prayers(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data['prayers']

def generate_daily_prayer(prayers, theme=None):
    if theme:
        filtered_prayers = [p for p in prayers if p['theme'].lower() == theme.lower()]
        if not filtered_prayers:
            raise ValueError(f"No prayers found for theme: {theme}")
        return random.choice(filtered_prayers)['text']
    return random.choice(prayers)['text']

def main():
    parser = argparse.ArgumentParser(description="Generate daily Orthodox prayers.")
    parser.add_argument('--theme', type=str, help="Filter prayers by theme (e.g., invocation, repentance)")
    args = parser.parse_args()

    prayers = load_prayers('prayers.json')
    try:
        prayer = generate_daily_prayer(prayers, args.theme)
        print("Daily Prayer:")
        print(prayer)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

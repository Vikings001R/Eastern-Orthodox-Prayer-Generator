import json
import random
import argparse
from jinja2 import Environment, FileSystemLoader

def load_prayers(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data['prayers']

def generate_daily_prayer(prayers, theme=None):
    if theme:
        filtered_prayers = [p for p in prayers if p['theme'].lower() == theme.lower()]
        if not filtered_prayers:
            raise ValueError(f"No prayers found for theme: {theme}")
        return random.choice(filtered_prayers)
    return random.choice(prayers)

def render_html(prayer, output_file):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('prayer_template.html')
    html_content = template.render(prayer=prayer['text'])
    with open(output_file, 'w') as f:
        f.write(html_content)

def main():
    parser = argparse.ArgumentParser(description="Generate daily Orthodox prayers.")
    parser.add_argument('--theme', type=str, help="Filter prayers by theme (e.g., invocation, repentance)")
    parser.add_argument('--export', type=str, choices=['html'], help="Export format (e.g., html)")
    args = parser.parse_args()

    prayers = load_prayers('prayers.json')
    try:
        prayer = generate_daily_prayer(prayers, args.theme)
        if args.export == 'html':
            render_html(prayer, 'prayer.html')
            print(f"Generated HTML file: prayer.html")
        else:
            print("Daily Prayer:")
            print(prayer['text'])
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

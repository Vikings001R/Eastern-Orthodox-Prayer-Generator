import json
import random
import argparse
from jinja2 import Environment, FileSystemLoader
import os
import logging

logging.basicConfig(filename='prayer_generator.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def load_config(file_path):
    if not os.path.exists(file_path):
        logging.warning(f"Config file '{file_path}' not found, using defaults")
        return {"default_themes": [], "default_export": "text"}
    try:
        with open(file_path, 'r') as f:
            config = json.load(f)
        logging.info("Loaded configuration")
        return config
    except json.JSONDecodeError:
        logging.error(f"Invalid JSON format in '{file_path}'")
        raise ValueError(f"Invalid JSON format in '{file_path}'")

def load_prayers(file_path):
    if not os.path.exists(file_path):
        logging.error(f"Prayer file '{file_path}' not found")
        raise FileNotFoundError(f"Prayer file '{file_path}' not found")
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        logging.info(f"Loaded {len(data['prayers'])} prayers from {file_path}")
        return data['prayers']
    except json.JSONDecodeError:
        logging.error(f"Invalid JSON format in '{file_path}'")
        raise ValueError(f"Invalid JSON format in '{file_path}'")

def generate_daily_prayer(prayers, themes=None):
    if themes:
        themes = [t.lower() for t in themes]
        filtered_prayers = [p for p in prayers if p['theme'].lower() in themes]
        if not filtered_prayers:
            logging.warning(f"No prayers found for themes: {', '.join(themes)}")
            raise ValueError(f"No prayers found for themes: {', '.join(themes)}")
        prayer = random.choice(filtered_prayers)
    else:
        prayer = random.choice(prayers)
    logging.info(f"Selected prayer ID {prayer['id']} with theme '{prayer['theme']}'")
    return prayer

def render_html(prayer, output_file):
    if not os.path.exists('templates'):
        logging.error("Templates directory not found")
        raise FileNotFoundError("Templates directory not found")
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('prayer_template.html')
    html_content = template.render(prayer=prayer['text'])
    with open(output_file, 'w') as f:
        f.write(html_content)
    logging.info(f"Generated HTML file: {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Generate daily Orthodox prayers.")
    parser.add_argument('--theme', type=str, help="Filter prayers by theme(s), comma-separated (e.g., invocation,peace)")
    parser.add_argument('--export', type=str, choices=['html', 'text'], help="Export format (e.g., html, text)")
    args = parser.parse_args()

    try:
        config = load_config('config.json')
        prayers = load_prayers('prayers.json')
        themes = args.theme.split(',') if args.theme else config['default_themes']
        export = args.export or config['default_export']
        prayer = generate_daily_prayer(prayers, themes)
        if export == 'html':
            render_html(prayer, 'prayer.html')
            print(f"Generated HTML file: prayer.html")
        else:
            print("Daily Prayer:")
            print(prayer['text'])
    except (FileNotFoundError, ValueError, json.JSONDecodeError) as e:
        print(f"Error: {e}")
        logging.error(f"Program failed: {e}")
        exit(1)

if __name__ == "__main__":
    main()
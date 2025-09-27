from flask import Flask, request, render_template
import json
import random
import logging
import os

app = Flask(__name__, template_folder='templates')
logging.basicConfig(filename='prayer_generator.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def load_prayers(file_path):
    if not os.path.exists(file_path):
        logging.error(f"Prayer file '{file_path}' not found")
        raise FileNotFoundError(f"Prayer file '{file_path}' not found")
    with open(file_path, 'r') as f:
        data = json.load(f)
    logging.info(f"Loaded {len(data['prayers'])} prayers from {file_path}")
    return data['prayers']

def generate_daily_prayer(prayers, themes=None):
    if themes:
        themes = [t.lower().strip() for t in themes.split(',') if t.strip()]
        filtered_prayers = [p for p in prayers if p['theme'].lower() in themes]
        if not filtered_prayers:
            logging.warning(f"No prayers found for themes: {themes}")
            return None
        prayer = random.choice(filtered_prayers)
    else:
        prayer = random.choice(prayers)
    logging.info(f"Selected prayer ID {prayer['id']} with theme '{prayer['theme']}'")
    return prayer

@app.route('/')
def index():
    try:
        prayers = load_prayers('prayers.json')
        theme = request.args.get('theme', '')
        prayer = generate_daily_prayer(prayers, theme)
        if not prayer:
            return f"No prayers found for theme(s): {theme}", 400
        return render_template('prayer_template.html', prayer=prayer['text'], title=prayer.get('title', 'Daily Prayer'))
    except Exception as e:
        logging.error(f"Web server error: {e}")
        return f"Error: {e}", 500

if __name__ == "__main__":
   print("Running on http://0.0.0.0:5000 (Press CTRL+C to quit)")
   app.run(debug=True, host='0.0.0.0', port=5000)

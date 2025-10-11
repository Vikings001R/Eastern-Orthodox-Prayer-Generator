from flask import Flask, request, render_template, jsonify
import json
import random
import logging
import os
import datetime

app = Flask(__name__, template_folder='templates', static_folder='static')
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

def get_unique_themes(prayers):
    themes = set(p['theme'] for p in prayers)
    return sorted(list(themes))

def generate_daily_prayer(prayers, themes=None):
    random.seed(datetime.date.today().toordinal())  # Daily randomization
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

@app.route('/privacy')
def privacy():
    return """
    <html>
    <body>
    <h1>Privacy Policy</h1>
    <p>Effective Date: September 28, 2025<br>
    Eastern Orthodox Prayer Generator ("we," "us," or "our") operates the website at https://www.dailyeasternorthodoxgenerator.com (the "Site"). This Privacy Policy explains how we collect, use, disclose, and safeguard your information when you visit the Site. By using the Site, you consent to the practices described herein. If you do not agree, please do not access the Site.<br>
    Information We Collect:<br>
    Automatically Collected Data: When you visit the Site, our servers may automatically log standard data provided by your web browser, including your IP address, browser type, operating system, access times, and the pages viewed. This data is used solely for operational purposes, such as diagnosing server problems and ensuring Site functionality. No personal identifiers are collected.<br>
    No User-Provided Data: The Site does not require registration, forms, or user input. We do not collect names, email addresses, or other personal information from users.<br>
    How We Use Your Information:<br>
    The collected data is used to maintain and improve the Site's performance.<br>
    It may be analyzed in aggregate form for internal purposes, such as understanding usage patterns.<br>
    No data is used for marketing, advertising, or shared with third parties.<br>
    Data Sharing and Disclosure:<br>
    We do not sell, rent, or share your data with third parties.<br>
    Data may be disclosed if required by law or to protect our rights (e.g., in response to a court order).<br>
    Data Security:<br>
    We employ reasonable measures to protect data from unauthorized access or loss, though no internet transmission is entirely secure.<br>
    Logs are retained for a limited period (e.g., 30 days) and then deleted.<br>
    Children's Privacy:<br>
    The Site is not intended for children under 13. We do not knowingly collect data from children.<br>
    Changes to This Policy:<br>
    We may update this Privacy Policy. Changes will be posted here with an updated effective date.<br>
    Contact Us:<br>
    For questions, contact jacobloge@gmail.com.<br>
    This policy complies with general data protection principles but is not legal advice.</p>
    </body>
    </html>
    """

@app.route('/terms')
def terms():
    return """
    <html>
    <body>
    <h1>Terms and Conditions</h1>
    <p>Effective Date: September 28, 2025<br>
    By accessing or using the Eastern Orthodox Prayer Generator website (the "Site"), you agree to be bound by these Terms and Conditions ("Terms"). If you do not agree, please do not use the Site.<br>
    Use of the Site:<br>
    The Site provides access to Eastern Orthodox prayers for spiritual purposes only.<br>
    You may use the Site for personal, non-commercial purposes. You may not reproduce, distribute, or modify content without permission.<br>
    Intellectual Property:<br>
    All content, including prayers and design, is owned by us or licensed. You may not use it for commercial purposes.<br>
    Disclaimer of Liability:<br>
    The Site is provided "as is" without warranties. Prayers are for spiritual guidance and not professional advice (e.g., medical or legal).<br>
    We are not liable for any damages arising from Site use.<br>
    Prohibited Activities:<br>
    You may not misuse the Site, including hacking, scraping, or spreading malware.<br>
    Governing Law:<br>
    These Terms are governed by the laws of the United States.<br>
    Changes to Terms:<br>
    We may update these Terms. Continued use constitutes acceptance.<br>
    Contact Us:<br>
    For questions, contact jacobloge@gmail.com.</p>
    </body>
    </html>
    """

@app.route('/')
@app.route('/category/<theme>')
def index(theme=None):
    try:
        prayers = load_prayers('prayers.json')
        selected_prayer = generate_daily_prayer(prayers, theme)
        if not selected_prayer:
            return f"No prayers found for theme: {theme}", 400
        unique_themes = get_unique_themes(prayers)
        return render_template('prayer_template.html', 
                             prayer=selected_prayer['text'], 
                             title=selected_prayer.get('title', 'Daily Prayer'), 
                             saint=selected_prayer.get('saint', 'Traditional'),
                             selected_theme=theme or 'all',
                             themes=unique_themes)
    except Exception as e:
        logging.error(f"Web server error: {e}")
        return f"Error: {e}", 500

@app.route('/random-prayer', methods=['GET'])
def random_prayer():
    try:
        prayers = load_prayers('prayers.json')
        prayer = random.choice(prayers)  # Use random.choice directly for API
        logging.info(f"API selected prayer ID {prayer['id']} with theme '{prayer['theme']}'")
        return jsonify({
            'prayer': prayer['text'],
            'saint': prayer.get('saint', 'Traditional'),
            'title': prayer.get('title', 'Daily Prayer'),
            'theme': prayer['theme']
        })
    except Exception as e:
        logging.error(f"API error: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)


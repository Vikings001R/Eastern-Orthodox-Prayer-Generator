
# Eastern Orthodox Prayer Generator

<<<<<<< HEAD
A CLI tool to generate daily prayers from the saints of traditional ROC, ROCOR, and Serbian Orthodox Christian sources.
=======
A CLI tool and web app to generate daily prayers from authentic sources in the traditional ROC, ROCOR, and Serbian Orthodox Christian traditions, attributed to well-known saints. This project aims to provide spiritual support with plans to expand to 1,000 prayers.
>>>>>>> 9d7453c (Updated README with improved structure, instructions, and details)

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/eochurchprevails01/Eastern-Orthodox-Prayer-Generator.git
   cd Eastern-Orthodox-Prayer-Generator

Create and activate a virtual environment (recommended for Python 3.12+):
bashpython3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies:
bashpip install -r requirements.txt


Usage (CLI Tool)

Generate a random prayer:
bashpython main.py

Generate by theme (comma-separated for multiple):
bashpython main.py --theme=patron,church

Export to HTML:
bashpython main.py --theme=fasting --export=html


Web Interface
Run a local web server to access prayers via a browser:
bashpython server.py

Visit http://localhost:5000 for a random prayer.
Filter by theme: http://localhost:5000?theme=patron or http://localhost:5000?theme=marriage,thanksgiving.

The interface features Byzantine-inspired styling: serif fonts, gold accents, and a subtle cross motif for a reverent Orthodox aesthetic.
Logging
Actions and errors are logged to prayer_generator.log for debugging and tracking.
Requirements

Python 3.12 or higher
Dependencies listed in requirements.txt (e.g., Flask, Jinja2)

License
This project is licensed under the MIT License - see the LICENSE file for details.
Contact
For questions or suggestions, contact jacobloge@gmail.com.
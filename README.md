
# Eastern Orthodox Prayer Generator

A CLI tool to generate daily prayers from traditional ROC, ROCOR, and Serbian Orthodox sources.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Vikings001R/Eastern-Orthodox-Prayer-Generator.git
   cd Eastern-Orthodox-Prayer-Generator

## Usage

- Generate a random prayer:
  ```bash
  python main.py

## Logging

Actions and errors are logged to `prayer_generator.log` for debugging and tracking.

## Web Interface

Run a local web server to access prayers via a browser:
```bash
python server.py
```
Visit  for a random prayer or  to filter by theme(s).

## Web Interface

Run a local web server to access prayers via a browser:
```bash
python server.py
```
Visit `http://localhost:5000` for a random prayer or `http://localhost:5000?theme=patron` to filter by theme(s).

### Enhanced Appearance

The web interface features Byzantine-inspired styling: serif fonts, gold accents, and a subtle cross motif for a reverent Orthodox aesthetic. Access via `http://localhost:5000?theme=<theme>`.

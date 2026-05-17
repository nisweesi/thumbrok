# Thumbnail Auto-Generator using Grok + Grok Imagine

### Pre-setup

Make sure you have [brew](https://brew.sh/) installed
If uv is not installed
   
   Run
   ```bash
   brew install uv
   ```

### Setup

1. Clone this repo:
   ```bash
   git clone git@github.com:nisweesi/thumbrok.git
   cd thumbrok

2. Install dependencies:
   ```bash
   uv sync

3. Install pre-commit hooks:
    ```bash
    uv run pre-commit install

4. Run the file
     ```bash
     uv run python main.py

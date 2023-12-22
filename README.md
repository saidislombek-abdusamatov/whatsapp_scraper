# WhatsApp Web Scraping

## Table of Contents

1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Instructions](#instructions)

## Overview

### Problem

1. Exports are limited up to a maximum of 40,000 messages
2. Exports are limited to a `.txt` file format

### Solution

_WhatSoup_ solves these problems by loading the entire chat history in a browser, scraping the chat messages (only text, no media), and exporting it to `.csv` file format.

## Prerequisites

- You have a WhatsApp account
- You have Chrome or Edge browser installed
- You have some familiarity with setting up and running Python scripts

## Instructions

1. Make sure your WhatsApp chat settings are set to English language. This needs to be done on your phone (instructions [here](https://faq.whatsapp.com/general/account-and-profile/how-to-change-whatsapps-language/)). You can change it back afterwards, but for now the script relies on certain HTML elements/attributes that contain English characters/words.

2. Clone the repo:

   ```
   https://github.com/saidislombek-abdusamatov/whatsapp_scraper.git
   ```

3. Create a virtual environment:

   ```
   # Windows
   python -m venv env

   # Linux & Mac
   python3 -m venv env
   ```

4. Activate the virtual environment:

   ```
   # Windows
   env/Scripts/activate

   # Linux & Mac
   source env/bin/activate
   ```

5. Install the dependencies:

   ```
   # Windows
   pip install -r requirements.txt

   # Linux & Mac
   python3 -m pip install -r requirements.txt
   ```

6. Setup your environment

- Get your Chrome browser `Profile Path` by opening Chrome and entering `chrome://version` into the URL bar
- Get your Edge browser `Profile Path` by opening Edge and entering `edge://version` into the URL bar
- Create an `.env` file with an entry for `EDGE_PROFILE`, `CHROME_PROFILE` and `BROWSER` that specify the directory paths for your Edge Profile and your Chrome Profile from above steps:

  ```
  # Windows
  CHROME_PROFILE = 'C:\Users\your-username\AppData\Local\Google\Chrome\User Data'
  EDGE_PROFILE  = 'C:\Users\your-username\AppData\Local\Google\Chrome\User Data'
  BROWSER = 'chrome' or 'edge'

  # Linux & Mac
  CHROME_PROFILE = 'C:\Users\your-username\AppData\Local\Google\Chrome\User Data'
  EDGE_PROFILE  = 'C:\Users\your-username\AppData\Local\Google\Chrome\User Data'
  BROWSER = 'chrome' or 'edge'
  ```

7. Run the script

   ```
   # Windows
   python whatsapp_scraper.py

   # Linux & Mac
   python3 whatsapp_scraper.py
   ```

   **Note for Mac users**: you may get blocked when trying to run the script the first time with a message about chromedriver not being from an identified developer. This is normal. Follow [these instructions](https://stackoverflow.com/a/60362134) to grant chromedriver an exception, then re-run the script.

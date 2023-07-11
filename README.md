# Botagram

Botagram is a Python script that automates interactions on Instagram using the Selenium library. With Botagram, you can log in to your Instagram account and like all the posts on a given profile.

## Requirements

- Python 3.10+
- Selenium
- Firefox web browser

## Installation

1. Clone the repository
``` bash
git clone https://github.com/vilquid/Botagram.git
```
2. Install the required dependencies. You can use pip to install the dependencies listed in the requirements.txt file :
``` bash
pip install -r requirements.txt
```
3. Download the [GeckoDriver executable](https://github.com/mozilla/geckodriver) for Firefox (maybe you don't need it)
4. Extract the GeckoDriver executable and place it in the same directory as the Botagram script.

## Usage

1. Open the Botagram.py file in a text editor.

2. Replace the following placeholders with your Instagram account credentials and the profile URL you want to interact with :
   - username: Your Instagram username
   - password: Your Instagram password
   - profile_url: URL of the profile you want to interact with

Save the changes to the Botagram.py file.

Run the Botagram script.

The script will open a Firefox browser in private mode, log in to the given Instagram account and like all the posts on the specified profile.

Sit back and let Botagram automate the interactions for you!

## Disclaimer
Botagram is intended for educational purposes only. Please use this script responsibly and respect Instagram's terms of service. The developers of Botagram are not responsible for any misuse or violations.

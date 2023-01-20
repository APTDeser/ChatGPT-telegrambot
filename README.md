# Telegram bot fot ChatGPT
[made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

The simplest bot for Telegram based on 
[EasyChatGPT](https://github.com/LanLan69/easyChatGPT)\
## Features

- [x] Bypass Cloudflare's anti-bot protection using `undetected_chromedriver`
- [x] Complementary and fast Audio Recaptcha solver using the `pypasser` library.



## Installation

You must **install** ffmpeg and ffprobe on your machine before running.

[Install On Windows](https://phoenixnap.com/kb/ffmpeg-windows)\
[Install On Linux](https://www.golinuxcloud.com/ubuntu-install-ffprobe/)\
[Install On MacOS](https://bbc.github.io/bbcat-orchestration-docs/installation-mac-manual/)

Install the official easyChatGPT package
```bash
pip install easychatgpt
```


    
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`OPENAI_EMAIL`

`OPENAI_PASSWORD`

Copy the .env file and put in your openai email and password
```
cp .env.example .env
```


## Usage / Demo

Simple Usage
```
python ChatGPTBOT.py
```


## Acknowledgement
[EasyChatGPT](https://github.com/LanLan69/easyChatGPT)\

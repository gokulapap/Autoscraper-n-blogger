# Autoscraper-n-blogger
An Automated udemy coupons scraper which scrapes coupons and autopost the result in blogspot post and notifies via Telegram bot 

# Requirements
<li> Blogger account and blog id
<li> Telegram Bot API key and Your Telegram chat id to notify you and send results

# Setup

Before setup place Telegram bot API key, Telegram chat id and Blogger id in `config.json` file !

> <a href="https://stackoverflow.com/questions/43291868/where-to-find-the-telegram-api-key">Telegram-bot API key</a>

> <a href="https://www.wikihow.com/Know-Chat-ID-on-Telegram-on-Android">Telegram chat-id</a>

`pip3 install requirements.txt`

Once Installed all the requirements, setup the easyblogger by below command

`easyblogger --blogid <yourblogid> get`

> To get the blog id refer - https://subinsb.com/how-to-find-blogger-blog-id

This will open up a browser window that you use to authenticate with your google account 

> Note : Authenticate the google account associated with blogger account

you’re all set to use Easyblogger !

`python3 auto.py`

This above file will scrape all the udemy course and coupons and it will post in blogger and it will send a copy of scraped results via Telegram bot !

`This can be hosted on a cloud server to run it automatically everyday !`

# Demo
_Loading ..._

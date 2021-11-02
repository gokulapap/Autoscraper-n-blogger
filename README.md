# Autoscraper-n-blogger
An Automated udemy coupons scraper which scrapes coupons and autopost the result in blogspot post and notifies via Telegram bot 

`sample blog : https://free-course-coupons.blogspot.com`

# Requirements
<li> Blogger account and blog id
<li> Telegram Bot API key and Your Telegram chat id to notify you and send results

# Setup

Before setup place Telegram bot API key, Telegram chat id and Blogger id in `config.json` file !

> How to get my Telegram bot api key ? - <a href="https://stackoverflow.com/questions/43291868/where-to-find-the-telegram-api-key">Telegram-bot api-key</a>

> How to get your Telegram chat id ? - <a href="https://www.wikihow.com/Know-Chat-ID-on-Telegram-on-Android">Telegram chat-id</a>

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

https://user-images.githubusercontent.com/57899332/139593172-0c8bae42-798b-45d2-a699-6c5e1011662d.mp4





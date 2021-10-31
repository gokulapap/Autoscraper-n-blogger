import json
import telebot
from telebot import util
from datetime import date
from datetime import datetime
from os import system
import os

API_KEY = os.environ['API_KEY']
BLOG_ID = os.environ['BLOG_ID']
CHAT_ID = os.environ['CHAT_ID']

bot = telebot.TeleBot(API_KEY)

part1 = '''
<html>
<head>
<style>
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;400;500;600;700&display=swap");

.card {
  width: 350px;
  height: 87px;
  border-radius: 20px;
  background-color: #fff;
  padding: 10px 10px;
  position: relative;
}

.main,
.copy-button {
  display: flex;
  justify-content: space-between;
  padding: 0 10px;
  align-items: center;
}

.copy-button {
  margin: 12px 0 -5px 0;
  height: 45px;
  border-radius: 4px;
  padding: 0 5px;
  border: 1px solid #e1e1e1;
}

.copy-button input {
  width: 55%;
  height: 100%;
  border: none;
  outline: none;
  font-size: 15px;
}

.copy-button button {
  padding: 5px 20px;
  background-color: #dc143c;
  color: #fff;
  border: 1px solid transparent;
}

</style>
</head>

<body>
<div class="separator" style="clear: both;"><a href="https://1.bp.blogspot.com/-f5NKdS1sCsc/YKd5kR-2E9I/AAAAAAAAABo/ykARrUdn750UobuBvmmVodmsfb78uubBgCLcBGAsYHQ/s300/udemy.png" style="display: block; padding: 1em 0; text-align: center; "><img alt="" border="0" width="320" data-original-height="168" data-original-width="300" src="https://1.bp.blogspot.com/-f5NKdS1sCsc/YKd5kR-2E9I/AAAAAAAAABo/ykARrUdn750UobuBvmmVodmsfb78uubBgCLcBGAsYHQ/s320/udemy.png"/></a></div>

<p>
<script>
let copybtn = document.querySelector(".copybtn");
function copyIt(i){
  var x = document.getElementsByClassName("test")[i].id;
  let copyInput = document.querySelector(`#${x}`);
  copyInput.select();
  document.execCommand("copy");
  copybtn.textContent = "COPIED";
}
</script>

'''

part2 = '</body></html>'

##
def rem_code(str):
  str_en = str.encode("ascii", "ignore")
  str_de = str_en.decode()
  return str_de

#print("started..")
file = open('courses.json', 'r')
a = json.loads(file.read())
file.close()

fn = str(date.today().strftime("%d%m")) + '-' + str(datetime.now().strftime("%H%M"))
file = open('./htmls/courses_{}.html'.format(fn), 'w')
courses = a['courses']
l = len(courses)

file.write(part1)

for i in range(l):
  file.write("<h3>{}</h3>".format(rem_code(courses[i]['title'])))
  file.write("<p><h6>{}</h6>".format(courses[i]['date']))
  file.write('<div class="card"><div class="copy-button"><input class="test" id="'+str("ran{}".format(i))+'" type="text" readonly value="'+str(courses[i]['coupon'])+'"/><button onclick="copyIt('+str(i)+')" class="copybtn">COPY COUPON</button></div></div>') 
  file.write("<p><b>Enroll Now !</b> - <a href={} target='_blank'>{}</a>".format(courses[i]['enroll'], courses[i]['enroll']))
  file.write("<br><hr><br>")

file.write(part2)

file.close()
#print("\nCompleted!")

print("\n[+] Posting the Blog to blogger...")
system('easyblogger --blogid {} post -t "Free Udemy Courses - {}" -l "coupons,udemy" --publish -f ./htmls/courses_{}.html'.format(BLOG_ID, date.today().strftime("%d %b"), fn))
print("\n[+] Posted successfully!")

tel = ''
tel = tel + '*FREE UDEMY COURSES - {}*'.format(date.today().strftime("%d-%B"))
tel = tel + '\n\n'

print("\n[+] Sending to Telegram bot")
for i in range(l):
  tel = tel+'*COURSE* : {}\n'.format(courses[i]['title'])
  tel = tel+'*COUPON* : {}\n'.format(courses[i]['coupon'])
  tel = tel+'*LINK* : http://bitly.com/free-course-coupons\n'
  tel = tel+'\n'

file = open('telebot.txt','w')
file.write(tel)
file.close()

large_text = open("telebot.txt", "rb").read()

splitted_text = util.split_string(large_text, 3000)
for text in splitted_text:
    bot.send_message(CHAT_ID, text)

print('\n[+] Sent to telegram bot!\n')

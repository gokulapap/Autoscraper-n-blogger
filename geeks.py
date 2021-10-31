from bs4 import BeautifulSoup
import requests
from googlesearch import search
from datetime import date
import json

courses_last = {"source": "geeksgod", "courses": []}

def coupon_scraper(url):
        content = requests.get(url).text
        soup = BeautifulSoup(content, 'lxml')
        coupon = soup.find('p', class_ = 'elementor-heading-title elementor-size-default').text
        return coupon

def udemy_link(title):
        query = title+' udemy course'
        for j in search(query, tld="com", num=1, stop=1, pause=1):
                return j

urls = ['https://geeksgod.com/category/freecoupons/udemy-courses-free/', 'https://geeksgod.com/category/freecoupons/udemy-courses-free/page/2/']

for i in urls:
        content = requests.get(i).text
        soup = BeautifulSoup(content, 'lxml')
        print("scraping udemy courses and coupons ...")
        courses = soup.find_all('div', class_ = 'item-details')

        for course in courses:
                course_json = dict()

                try:
                        coupon = coupon_scraper(course.a["href"])
                        if coupon == None:
                                continue

                        title = course.h3.text
                        dat = course.time.text
                        udemylink = udemy_link(title)

                        course_json['title'] = title
                        course_json['link'] = udemylink
                        course_json['date'] = dat
                        course_json['coupon'] = coupon
                        course_json['enroll'] = f'{udemylink}?couponCode={coupon}'

                        courses_last['courses'].append(course_json)

                except:
                        pass

print("scraped the courses and results are saved !")
final = json.dumps(courses_last, indent=4)

file = open('geeksgod.json', 'w')
file.write(final)
file.close()


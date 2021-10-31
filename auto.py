from os import system
from time import sleep

system('python scrape.py')
sleep(2.5)
system('python post.py')

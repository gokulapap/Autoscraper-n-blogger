from os import system
from time import sleep

while(1):
  system('python geeks.py')
  sleep(3)
  system('python post.py')
  sleep(43200)

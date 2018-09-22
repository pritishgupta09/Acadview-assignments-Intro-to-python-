#Q.1 Print the Current Day

from datetime import date
days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
print(days[date.weekday(date.today())])

#Q.2 Use Webbrowser module in python

import webbrowser
webbrowser.open('https://www.github.com/pritishgupta09')

#Q.3 Rename All the Files in a Directory And Convert Them Into .jpg File Format

import os
os.rename('sample.txt','sample.jpg')
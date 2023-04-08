# =========================================== #
# py4e Week_4 (Web_Data) Parse HTML
# =========================================== #
# Worked example 
# =========================================== #

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
# soup is a clean proxy variable for the html

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))

# =========================================== #
# Exercise 1
# =========================================== #

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
# html = urlopen(url, context=ctx).read()
html = urlopen('http://py4e-data.dr-chuck.net/comments_1785347.html', context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
total = list()

# Retrieve all of the span tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    # print('TAG:', tag)
    # print('URL:', tag.get('href', None))
    # print('Contents:', tag.contents[0])
    # print('Attrs:', tag.attrs)

    # after looking at the data that was being parsed noticed that the contents tag contained the comments value so could extract this, add it to the accumulator list and sum the list for the answer.
    val = int(tag.contents[0])
    total.append(val)
print(sum(total))

# =========================================== #
# Exercise 2
# =========================================== #

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
count_in = input('Enter count: ')
count = int(count_in)
pos_in = input('Enter position: ')
pos = int(pos_in)

# print the initial url that is being visited
print('Retrieving:',url)
   
# use for loop with a range parameter to define the number of times that a link is followed
for i in range(0,count):
    # url is defined at the start of the initial loop and updated with the new url produced as the loop completes
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    # iterate through list of anchor tags that Bsoup creates up to pos (defined by input) to find the next url to follow and overwrite the url var. 
    # i + 1 to manage the loop count and the new url is printed for ref
    for tag in tags[:pos]:
        url = tag.get('href', None)
    i + 1
    print('Retrieving:',url) 



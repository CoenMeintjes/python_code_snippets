# =========================================== #
# py4e Week_5 (Web_Data) Parse XML
# =========================================== #
# Exercise 1
# =========================================== #

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

uh = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_1785349.xml')
lst =list()

data = uh.read()
print(data.decode())
tree = ET.fromstring(data)
counts = tree.findall('.//count')

for item in counts:
    print('Count', item.text)
    val = int(item.text)
    lst.append(val)

print('\nSum of number of comments =', sum(lst),'\n')


# WITH THIS CODE I KEPT HITTING THE ERROR AttributeError: 'NoneType' object has no attribute 'text'. 
# THIS WAS BECAUSE I WAS AT THE BOTTOM OF THE TREE AND THERE WAS NO NEED TO GO FIND THE TAG I WAS ALREADY IN IT DO JUST HAD TO DISPLAY THE TEXT. 
# SEE https://stackoverflow.com/questions/71451955/problem-parsing-xml-when-retrieving-from-a-url FOR THE EXPLAINATION OF THE ISSUE AND HOW TO FIX IT
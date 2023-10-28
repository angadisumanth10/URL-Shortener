# pip install pyshorteners
# pip install pyperclip

import pyshorteners

url = input('Enter the Url: ')

# Define the function..
def shortenurl(url):
    s = pyshorteners.Shortener()
    print(s.tinyurl.short(url))

shortenurl(url)


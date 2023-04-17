#PROBLEM DESCRIPTION
#Implement a URL shortener with the following methods:
#shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
#restore(short), which expands the shortened string into the original url. If no such shortened string exists, return null.
#Hint: What if we enter the same URL twice?

import random
import string

class URLShortener:
    def __init__(self):
        self.short_to_long = {}
        self.long_to_short = {}

    def shorten(self, long_url):
        if long_url in self.long_to_short:
            return self.long_to_short[long_url]
        else:
            chars = string.ascii_letters + string.digits
            short_url = ''.join(random.choice(chars) for _ in range(6))
            while short_url in self.short_to_long:
                short_url = ''.join(random.choice(chars) for _ in range(6))
            self.short_to_long[short_url] = long_url
            self.long_to_short[long_url] = short_url
            return short_url

    def restore(self, short_url):
        return self.short_to_long.get(short_url, None)

shortener = URLShortener()

original_url = 'https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox/FMfcgzGsmDnxDWSHcCbxKKNMxTGhkPMN'
# Shorten a URL
short_url = shortener.shorten(original_url)
# Restore a shortened URL
long_url = shortener.restore(short_url)
print("Original URL: "+ original_url)
print("Shortened URL: "+ short_url)
print("Long URL: "+long_url)



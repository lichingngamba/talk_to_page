'''
The purpose of this module is to extract urls from a given query.
'''

import re

class extract_url:
    def __init__(self):
        self.__pattern = re.compile(r"\b(?:https?://)?(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b")

    def extract(self, query):
        '''
        extract urls from a given query
        '''
        return re.findall(self.__pattern, query)
    
    def add_http(self, query):
        '''
        If the etracted url does not start with http, add http to the url
        '''
        added_url = []
        list_url = self.extract(query= query)
        for url in list_url:
            if not url.startswith("http"):
                url = url.replace(url, "http://" + url)
                added_url.append(url)
            else:
                added_url.append(url)
                
        return added_url

if __name__ == "__main__":
    url_extractor = extract_url()
    print(url_extractor.add_http("This is a test url: https://www.google.com lichingngamba.github.io"))

'''
This checks the reelevance of the content of the url to the query
'''

try:
    from utils.url_extractor import extract_url
    from utils.store_content import store_content, Content
    from utils.crawler import crawl
except:
    from url_extractor import extract_url
    from store_content import store_content, Content
    from crawler import crawl

class Relevance:
    def __init__(self):
        self.extractor = extract_url()

    def store_relevance(self, query):
        '''
        This function will do:
        - `Extract urls from the query`
        - `Crawl the urls`
        - `Store the content of the urls`
        - `Return the content`
        
        '''
        append_url = list()
        append_content = list()
        urls = self.extractor.add_http(query)
        urls = urls[:1]
        scrap_data = [crawl(url) for i, url in enumerate(urls) if i < 1]
        for item in scrap_data.pop():
            if isinstance(item, dict):
                append_url.append(item['url'])
                append_content.append(item['content'])
            
        # print(f"append_url:{append_url}")
        content = store_content(content= Content(url= append_url, content= append_content)) 
               
        return content
    
if __name__ == '__main__':
    relevance = Relevance()
    response = relevance.store_relevance('What is the capital of Nigeria? find out from en.wikipedia.org/wiki/Nigeria')
    print(response)
    
    

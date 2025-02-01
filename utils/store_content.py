'''
This module helps store the content of the url in a list of dictionaries
'''

from pydantic import BaseModel
from typing import List

class Content(BaseModel):
    url: list
    content: list
    

def store_content(content: Content)->List[dict]:
    '''
    Store the content of the url in a list of dictionaries
    '''
    content_list = []
    
    for url, content in zip(content.url, content.content):
        content_list.append({"url": url, "content": content, "meta": {"url": url}})

    return content_list


if __name__ == "__main__":
    print(store_content(content= Content(url=["https://www.google.com", "https://www.youtube.com"], content=["This is a test content", "This is another test content"])))
    # [{'url': 'https://www.google.com', 'content': 'This is a test content'}, {'url': 'https://www.youtube.com', 'content': 'This is another test content'}]
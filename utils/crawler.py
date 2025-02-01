import requests
from bs4 import BeautifulSoup
import io
import PyPDF2 

def extract_pdf_text(pdf_bytes):
    '''Use PyPDF2 to extract text from the PDF content in memory'''
    reader = PyPDF2.PdfReader(io.BytesIO(pdf_bytes))
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def process_url(url):
    '''process url and return content'''
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Check for HTTP errors
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return {'url': None, 'type': 'error', 'content': None, 'links': None}

    content_type = response.headers.get('Content-Type', '').lower()
    # If the content is a PDF (check MIME type or URL extension)
    if 'application/pdf' in content_type or url.lower().endswith('.pdf'):
        print("Processing PDF:", url)
        pdf_text = extract_pdf_text(response.content)
        return {'url': url, 'type': 'pdf', 'content': pdf_text}
    else:
        # Otherwise assume it is an HTML page
        print("Processing HTML:", url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extract text (you can further refine this, e.g., removing navigation, etc.)
        text = soup.get_text(separator='\n', strip=True)
        # Find all links to crawl further
        links = [a.get('href') for a in soup.find_all('a', href=True)]
        return {'url': url, 'type': 'html', 'content': text, 'links': links}

def crawl(seed_url, max_depth=1):
    '''
    name
    -----
    
    crawl
    
    
    description
    -----------
    
    To crawl a given url with defualt dept of 1
    
    parameters
    ----------

    seed_url: the url to start crawling from
    max_depth: the maximum depth to crawl to
    
    Returns
    -------

    A list of dictionaries containing the url, type, content and links of each page crawled
    '''
    visited = set()
    to_visit = [(seed_url, 0)]
    results = []

    while to_visit:
        current_url, depth = to_visit.pop(0)
        if current_url in visited or depth > max_depth:
            break
        visited.add(current_url)
        data = process_url(current_url)
        if data:
            results.append(data)
            # If it is HTML, add discovered links to the crawl queue
            if data['type'] == 'html' and 'links' in data:
                for link in data['links']:
                    # Normalize the URL (this example assumes absolute URLs)
                    if link.startswith('http'):
                        if depth < max_depth - 1:
                            to_visit.append((link, depth + 1))
                        else:    
                            break
        # You can add a delay here to respect target servers.
    return results

def main(seed_url):
    '''The main file to run the crawler'''
    scraped_data = crawl(seed_url)
    print(len(scraped_data)) 
    for item in scraped_data:
        print(f"\nURL: {item['url']}")
    #     print(f"Type: {item['type']}")
        # print("Content:\n" + item['content'].strip() + "\n")

if __name__ == "__main__":
    # import sys
    # if len(sys.argv) < 2:
    #     print("Usage: python crawler.py <seed_url>")
    #     sys.exit(1)
    # main(sys.argv[1])
    main('https://en.wikipedia.org/wiki/Nigeria')

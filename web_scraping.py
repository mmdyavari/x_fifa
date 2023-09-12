import requests
import bs4

def find_elements (url , element):
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    # get html of page
    page = requests.get(url, headers=headers).content
    soup = bs4.BeautifulSoup(page, 'html.parser')
    # select element with class or id in html
    elements = soup.select(element)
    # cleaning data
    elements = list(filter(lambda item: item != None, elements))
    result = []
    for i in elements:
        result.append((i.string).strip())
    return result


# for exampel (work with this function)
# find_elements(url='https://www.futbin.com/', element='.article-title')

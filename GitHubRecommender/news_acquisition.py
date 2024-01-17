import requests
from bs4 import BeautifulSoup

def fetch_latest_python_news():
    url = "https://planetpython.org/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    news_data = []
    posts = soup.find_all('h3', class_='post')

    for post in posts[:10]:  
        title_element = post.find('a')
        title = title_element.get_text().strip()
        link = title_element['href']
        date = post.find_next('p').find('em').get_text().strip()
        description = post.find_next('h4').get_text().strip()

        news_data.append({'title': title, 'link': link, 'date': date, 'description': description})

    return news_data




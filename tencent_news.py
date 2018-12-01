import requests
from bs4 import BeautifulSoup
url = 'https://news.qq.com/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}
response = requests.get(url,headers = headers)
html_test = response.text
soup = BeautifulSoup(html_test,'lxml')
# print(soup)
news_list = soup.select("a.linkto")
# print(news_list)
for i in news_list:
    title = i.get_text()
    link = i.get('href')
    data = {'title':title,'link':link}
    print(data)
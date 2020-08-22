学习笔记

##pip
[`pip`](https://pip.pypa.io/en/stable/) is like `npm` for `node`.
```
pip install SomePackage
pip install SomerPackage==2.6.0
pip install --upgrade SomePackge
pip uninstall SomePackage
pip list
pip search SomePackage
pip show SomePackage
pip freeze > requirements.txt
pip install -r requirements.txt
```

##venv
Create and manage virtual environments. 
```
python3 -m venv tutorial-env
source tutorial-env/bin/activate
```

##requests and BeautifulSoup Example
```
import requests
from bs4 import BeautifulSoup as bs

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
headers = {'user-agent': user_agent}
url = 'https://movie.douban.com/top250'

response = requests.get(url, headers=headers)
# print(response.text)
# print(f'status code is: {response.status_code}')

bs_info = bs(response.text, 'html.parser')
for tags in bs_info.find_all('div', attrs={'class': 'hd'}):
  for atag in tags.find_all('a'):
    print(atag.get('href'))
    print(atag.find('span').text)
```

##lxml.etree, XPath and Pandas Example
```
import requests
import lxml.etree

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
headers = {'user-agent': user_agent}
url = 'https://movie.douban.com/subject/1292052/'

response = requests.get(url, headers=headers)

selector = lxml.etree.HTML(response.text)

#film name
film_name = selector.xpath('//*[@id="content"]/h1/span[1]/text()')
print(f'file name is: {film_name}')

#release date
release_date = selector.xpath('//*[@id="info"]/span[10]/text()')
print(f'release date is: {release_date}')

#rating
rating = selector.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')
print(f'rating is: {rating}')

my_list = [film_name, release_date, rating]

import pandas
movie1 = pandas.DataFrame(data=my_list)
movie1.to_csv('./movie1.csv', encoding='utf8', index=False, header=False)
```
##[Working with XPath](https://docs.scrapy.org/en/latest/topics/selectors.html#working-with-xpaths)

##Delay request
```
from time import sleep
sleep(10)
```

##Scrapy
[Architecture review](https://docs.scrapy.org/en/latest/topics/architecture.html)
[Quick tutorial](https://docs.scrapy.org/en/latest/intro/tutorial.html)
```
scrapy startproject example example.com
cd example/spiders
scrapy genspider example
scrapy crawl example
```
**pipeline example using CsvItemExporter**
```
from scrapy.exporters import CsvItemExporter

class Assignment2Pipeline:
    def __init__(self):
        self.file = open('./movies.csv', 'wb')
        self.exporter = CsvItemExporter(self.file)
        self.exporter.fields_to_export = ['name', 'movie_type', 'release_date']
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
```
**yield vs return**
If you use `return`, your for-loop will finish after the first iteration. In contrast to `return`, `yield` doesn't exit the function and continues with the your for-loop.

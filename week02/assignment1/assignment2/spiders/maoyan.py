import scrapy
from scrapy.selector import Selector
from assignment2.items import MovieItem

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def parse(self, response):
      movies_list = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
      for movie in movies_list[:10]:
        info = movie.xpath('./div')
        item = MovieItem()
        item['name'] = info[0].xpath('./span/text()').get()
        item['movie_type'] = info[1].xpath('./text()')[1].get().strip()
        item['release_date'] = info[3].xpath('./text()')[1].get().strip()
        yield item


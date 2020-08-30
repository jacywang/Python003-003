# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
from scrapy.exceptions import DropItem

class Assignment2Pipeline:
    def __init__(self):
      try:
        self.connection = pymysql.connect(host='localhost',
                                          user='user',
                                          password='password',
                                          db='db',
                                          charset='utf8mb4',)
      except Exception as e:
        raise DropItem(f'Connection to MySQL failed {e}')
      self.cursor = self.connection.cursor()

    def close_spider(self, spider):
      try:
        self.cursor.close()
        self.connection.commit()
        self.connection.close()
      except Exception as e:
        raise DropItem(f'Failed to close {e}')

    def process_item(self, item, spider):
      try:
        sql = "INSERT INTO 'movies' ('name', 'type', 'release_date) VALUES (%s, %s, %s))"
        self.cursor.execute(sql, tuple(item.values()))
      except Exception as e:
        self.connection.rollback()
        print(f'Insert item failed {e}')
      return item

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ReitArticleItem(scrapy.Item):
    month = scrapy.Field()
    year = scrapy.Field()
    sector = scrapy.Field()
    companies_mentioned = scrapy.Field()

    sentiment_score = scrapy.Field()

    # title = scrapy.Field()
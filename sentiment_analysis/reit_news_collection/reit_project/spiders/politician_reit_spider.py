# Cameron Keith
# August 20, 2023
# AI ML U Chicago Class

# Import the scrapy library and the ReitArticleItem from the items module
import scrapy
from reit_project.items import ReitArticleItem

# Define the PoliticianReitSpider class
class PoliticianReitSpider(scrapy.Spider):
    name = 'politician_reit_spider'
    allowed_domains = ['quiverquant.com']

    # Custom settings for the spider
    custom_settings = { 
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'output_politician_data.csv',
        'ITEM_PIPELINES': {
            "reit_project.pipelines.ReitPolPipeline": 100,
        },
    }

    # Define the start_requests method to initiate crawling
    def start_requests(self):
        base_url = 'https://www.quiverquant.com/congresstrading/stock/{}'
        tickers = ['BXP', 'HIW', 'KRC', 'WRE', 'CLI', 'VRE', 'MPG', 'BPO', 'SLG', 'BDN', 'DEI', 'OFC', 'PDM', 'ESRT', 'EQC', 'PGRE', 'JBGS', 'HPP', 'AAT']

        # Loop through tickers and yield requests
        for ticker in tickers:
            yield scrapy.Request(base_url.format(ticker), callback=self.parse, meta={'ticker': ticker})

    # Define the parse method to extract data from the response
    def parse(self, response):
        ticker = response.meta['ticker']
        rows = response.css('.table-congress tbody tr')

        # Loop through rows and extract data
        for row in rows:
            item = ReitArticleItem()

            td_elements = row.css('td')

            item['companies_mentioned'] = ticker 
            item['sentiment_score'] = td_elements[1].css('a span::text').get().strip()
            item['month'] = td_elements[4].css('a::text').get().strip()
            item['sector'] = 'Office'

            yield item

import scrapy
from reit_project.items import ReitArticleItem

class ReitSpider(scrapy.Spider):
    name = 'reit_spider'
    allowed_domains = ['reit.com']

    def start_requests(self):
        base_url = 'https://www.reit.com/news/search?topic=All&contenttype[news_article]=news_article&publish_date=All&article_type=All&sort_by=created&sort_order=DESC&page={}'
        for page_number in range(0, 150):  # Pages 1 to 149
            yield scrapy.Request(base_url.format(page_number), callback=self.parse)

    def parse(self, response):
        # Extract links to each article from the current page
        article_links = response.css('.search-news-item-content .title a::attr(href)').extract()
        for link in article_links:
            article_url = response.urljoin(link)
            yield scrapy.Request(article_url, callback=self.parse_article)

    def parse_article(self, response):
        # Extract article content here and populate the item
        item = ReitArticleItem()

        # item['title'] = response.css('.field--name-title.field--type-string.field--label-hidden::text').get()
        item['month'] = response.css('.node__intro-date::text').get()

        sector_links = response.css('.node--full__related-content .field--name-field-search-categories .field__item a')
        sectors = [link.css('::text').get().replace('Sector', '').strip() for link in sector_links if 'sector' in link.css('::text').get().lower()]
        item['sector'] = sectors

        # Extract company and sector mentioned information
        companies_mentioned = []
        company_divs = response.css('article.node--company--card')
        for company_div in company_divs:
            company_name = company_div.css('.node__title .title::text').get().strip()  # Strip extra spaces
            company_sectors = [sector.css('::text').get().strip() for sector in company_div.css('.sectors .field__item')]  # Strip extra spaces
            for sector in company_sectors:
                companies_mentioned.append(f"{company_name}, {sector}")
        item['companies_mentioned'] = companies_mentioned  # Add companies mentioned information

        content = response.css('.field--name-field-text p::text').getall()
        content = ' '.join(content).strip()
        item['sentiment_score'] = content

        
        # Yield the populated item
        yield item

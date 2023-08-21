# Cameron Keith
# August 20, 2023
# AI ML U Chicago Class

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter

import re
from datetime import datetime
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Pipeline for cleaning data
class CleanDataPipeline:

    def process_item(self, item, spider):

        if 'month' in item:
            raw_date = item['month']
            month, year = self.clean_date(raw_date)
            item['month'] = month
            item['year'] = year[-2:]

        return item

    def clean_date(self, raw_date):
        # Extract month and year using regex
        match = re.search(r'(\d{2})/(\d{2})/(\d{4})', raw_date)
        if match:
            month, day, year = match.groups()
            return month, year #,day
        return None, None #, None

# Pipeline for sentiment analysis
class SentimentAnalysisPipeline:

    def process_item(self, item, spider):

        content = item['sentiment_score']
        sia = SentimentIntensityAnalyzer()
        sentiment_scores = sia.polarity_scores(content)
        sentiment_score = sentiment_scores['compound']
        item['sentiment_score'] = sentiment_score
        return item

# Pipeline for REIT political data
class ReitPolPipeline:

    def process_item(self, item, spider):

        sentiment = 0
        if item['sentiment_score'] == 'Purchase':
            sentiment = 1
        elif item['sentiment_score'] == 'Sale':
            sentiment = -1

        item['sentiment_score'] = sentiment
        month, year = self.clean_date(item['month'])

        item['month'] = month
        item['year'] = year

        return item

    def clean_date(self, input_date):
        # Convert input string to a datetime object
        input_date = datetime.strptime(input_date, "%b. %d, %Y")

        # Convert datetime object to desired output format
        output_month = input_date.strftime("%m")
        output_year = input_date.strftime("%Y")

        output_year = output_year[-2:]

        return output_month, output_year

# Pipeline for REIT insider data
class ReitInsiderPipeline:

    def process_item(self, item, spider):

        sentiment = 0
        if item['sentiment_score'] == 'Purchase':
            sentiment = 1
        elif item['sentiment_score'] == 'Sale':
            sentiment = -1

        item['sentiment_score'] = sentiment
        month, year = self.clean_date(item['month'])

        item['month'] = month
        item['year'] = year[-2:]

        return item

    def clean_date(self, input_date):
        # Convert input string to a datetime object
        input_date = input_date[:3] + '.' + input_date[3:]
        input_date = datetime.strptime(input_date, "%b. %d, %Y")

        # Convert datetime object to desired output format
        output_month = input_date.strftime("%m")
        output_year = input_date.strftime("%Y")
        output_year = output_year[-2:]
        return output_month, output_year

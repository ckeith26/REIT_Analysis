# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class CleanDataPipeline:

    def process_item(self, item, spider):
        if 'month' in item:
            raw_date = item['month']
            month, year = self.clean_date(raw_date)
            item['month'] = month
            item['year'] = year[-2:]

        # # Clean the title
        # if 'title' in item:
        #     cleaned_title = self.clean_title(item['title'])
        #     item['title'] = cleaned_title
        
        return item

    def clean_date(self, raw_date):
        # Extract month and year using regex
        match = re.search(r'(\d{2})/(\d{2})/(\d{4})', raw_date)
        if match:
            month, day, year = match.groups()
            return month, year #,day
        return None, None #, None

    # def clean_title(self, raw_title):
    #     # Remove excess spaces and unwanted characters
    #     cleaned_title = ' '.join(raw_title.strip().split())
    #     cleaned_title = cleaned_title.replace('"', '').replace('“', '').replace('”', '')  # Remove double quotes and similar characters
    #     return cleaned_title

class SentimentAnalysisPipeline:
    def process_item(self, item, spider):
        content = item['sentiment_score']
        sia = SentimentIntensityAnalyzer()
        sentiment_scores = sia.polarity_scores(content)
        sentiment_score = sentiment_scores['compound']
        item['sentiment_score'] = sentiment_score
        return item


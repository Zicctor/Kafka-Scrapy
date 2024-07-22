# bookscraper/pipelines.py
import psycopg2
from scrapy import signals
from itemadapter import ItemAdapter
from bookscraper.kafka_producer import send_message
from scrapy.exceptions import NotConfigured
class SaveToPostgrePipeline:
    def open_spider(self, spider):
        self.conn = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='postgres',
            database='postgres'
        )
        self.cur = self.conn.cursor()
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id SERIAL PRIMARY KEY,
            url VARCHAR(255),
            title TEXT,
            upc VARCHAR(255),
            product_type VARCHAR(255),
            price_excl_tax DECIMAL,
            price_incl_tax DECIMAL,
            tax DECIMAL,
            price DECIMAL,
            availability INTEGER,
            num_reviews INTEGER,
            stars INTEGER,
            category VARCHAR(255),
            description TEXT
        )
        """)
        self.conn.commit()

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()

    def process_item(self, item, spider):
        try:
            self.cur.execute("""
            INSERT INTO books (
                url, 
                title, 
                upc, 
                product_type, 
                price_excl_tax,
                price_incl_tax,
                tax,
                price,
                availability,
                num_reviews,
                stars,
                category,
                description
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                item['url'],
                item['title'],
                item['upc'],
                item['product_type'],
                item['price_excl_tax'],
                item['price_incl_tax'],
                item['tax'],
                item['price'],
                item['availability'],
                item['num_reviews'],
                item['stars'],
                item['category'],
                item['description']
            ))
            self.conn.commit()
        except psycopg2.Error as e:
            spider.logger.error(f"Error inserting item into database: {e}")
            self.conn.rollback()
        return item

class KafkaPipeline:
    @classmethod
    def from_crawler(cls, crawler):
        if not crawler.settings.getbool('KAFKA_ENABLED'):
            raise NotConfigured
        return cls()

    def open_spider(self, spider):
        spider.crawler.signals.connect(self.spider_closed, signal=signals.spider_closed)

    def spider_closed(self, spider):
        spider.logger.info(f"Sending completion message to Kafka for spider: {spider.name}")
        send_message('email_topic', f'Spider {spider.name} has completed scraping.')

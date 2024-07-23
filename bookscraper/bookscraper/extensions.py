import logging
from scrapy import signals
from .email_sender import send_email
from datetime import datetime

class EmailSenderExtension:

    @classmethod
    def from_crawler(cls, crawler):
        ext = cls()
        crawler.signals.connect(ext.spider_closed, signal=signals.spider_closed)
        return ext

    def spider_closed(self, spider):
        logging.info(f"Spider {spider.name} has closed. Sending email...")
        
        # Get the current time
        finish_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        subject = f"Scraping job '{spider.name}' completed"
        body = (
            f"The scraping job for spider '{spider.name}' has been completed.\n"
            f"Finish time: {finish_time}"
        )
        to_email = 'svshirunai123@gmail.com'  # Replace with the destination email address
        
        send_email(subject, body, to_email)
        logging.info("Email sent.")

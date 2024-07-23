BOT_NAME = 'bookscraper'

SPIDER_MODULES = ['bookscraper.spiders']
NEWSPIDER_MODULE = 'bookscraper.spiders'

ROBOTSTXT_OBEY = False

SPIDER_MIDDLEWARES = {
    'bookscraper.middlewares.BookscraperSpiderMiddleware': 543,
}

DOWNLOADER_MIDDLEWARES = {
    'bookscraper.middlewares.BookscraperDownloaderMiddleware': 543,
}

# Add your Kafka broker URL and topic name
KAFKA_BROKER = 'localhost:9092'
KAFKA_TOPIC = 'scrapy_items'

# Enable the Kafka pipeline
ITEM_PIPELINES = {
    'bookscraper.pipelines.BookscraperPipeline': 100,
    'bookscraper.pipelines.SaveToPostgreSQLPipeline': 200,
    'bookscraper.pipelines.KafkaPipeline': 300,
}

EXTENSIONS = {
    'bookscraper.extensions.EmailSenderExtension': 500,
}

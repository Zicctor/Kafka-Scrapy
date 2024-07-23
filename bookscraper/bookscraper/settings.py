
BOT_NAME = 'bookscraper'

SPIDER_MODULES = ['bookscraper.spiders']
NEWSPIDER_MODULE = 'bookscraper.spiders'

#Using this if you want to save the data locally
# FEEDS = {
#     'booksdata.json': {'format': 'json'},
# }

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

SPIDER_MIDDLEWARES = {
    'bookscraper.middlewares.BookscraperSpiderMiddleware': 543,
}

DOWNLOADER_MIDDLEWARES = {
    'bookscraper.middlewares.BookscraperDownloaderMiddleware': 543,
}

ITEM_PIPELINES = {
   'bookscraper.pipelines.BookscraperPipeline': 300,
   'bookscraper.pipelines.SaveToPostgreSQLPipeline': 400,
}



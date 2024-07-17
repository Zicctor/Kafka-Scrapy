# Scrapy settings for bookscraper project

BOT_NAME = 'bookscraper'

SPIDER_MODULES = ['bookscraper.spiders']
NEWSPIDER_MODULE = 'bookscraper.spiders'

FEEDS = {
    'booksdata.json': {'format': 'json'},
}

SCRAPEOPS_API_KEY = '4936f549-3429-4061-8ec0-dba18cb0f39b' 
SCRAPEOPS_FAKE_USER_AGENT_ENDPOINT = 'https://headers.scrapeops.io/v1/user-agents'
SCRAPEOPS_FAKE_USER_AGENT_ENABLED = True
SCRAPEOPS_NUM_RESULTS = 5
SCRAPEOPS_PROXY_ENABLED = True

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Enable or disable downloader middlewares
DOWNLOADER_MIDDLEWARES = {
    'bookscraper.middlewares.BookscraperDownloaderMiddleware': 543,
    'bookscraper.middlewares.ScrapeOpsFakeBrowserHeaderAgentMiddleware': 400,
}

# Configure item pipelines
ITEM_PIPELINES = {
   'bookscraper.pipelines.BookscraperPipeline': 300,
   'bookscraper.pipelines.SaveToPostgrePipeline': 400,
}

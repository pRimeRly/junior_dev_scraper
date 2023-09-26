BOT_NAME = "junior_dev_scraper"

SPIDER_MODULES = ["junior_dev_scraper.spiders"]
NEWSPIDER_MODULE = "junior_dev_scraper.spiders"

# Set a custom User-Agent
USER_AGENT = "jun_dev_assignment (+http://www.example.com)"

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Download delay of 3 seconds between requests
DOWNLOAD_DELAY = 3

# Enable item pipelines and specify their order
ITEM_PIPELINES = {
    "jun_dev_scraper.pipelines.JunDevAssignmentPipeline": 300,
}

# Output format and location
FEED_FORMAT = 'csv'
FEED_URI = 'cars24_data.csv'

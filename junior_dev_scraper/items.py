# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JunDevAssignmentItem(scrapy.Item):
    # define the fields for your item here like:
    Brand = scrapy.Field()
    Engine_Size = scrapy.Field()
    Year_of_Manufacture = scrapy.Field()
    Deeplink = scrapy.Field()
    Fuel_Type = scrapy.Field()
    Price = scrapy.Field()
    Model = scrapy.Field()
    Mileage = scrapy.Field()

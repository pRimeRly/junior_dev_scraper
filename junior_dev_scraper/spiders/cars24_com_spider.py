import scrapy
import json
import re
from benedict import benedict
from w3lib.url import add_or_replace_parameter

from typing import Any
from scrapy.http import Response
from junior_dev_scraper.items import JunDevAssignmentItem

# See https://www.cars24.com/ae/buy-used-cars-dubai/


class Car24ComSpider(scrapy.Spider):
    name = 'cars24_com_spider'
    start_urls = ['https://www.cars24.com/ae/buy-used-cars-dubai/']

    def parse(self, response: Response, **kwargs: Any) -> Any:

        # Container with individual car advertisements
        car_ads = response.css('div.TGZkx._3q5mX div._3IIl_._1xLfH')
        for car_ad in car_ads:
            item = JunDevAssignmentItem(
                Brand=car_ad.css('h3.RZ4T7::text').get(default='Unknown Brand'),
                Engine_Size=car_ad.css('ul._3ZoHn li:nth-child(3)::text').get(default='Unknown Engine Size'),
                Year_of_Manufacture=car_ad.css('p._1i1E6::text').get(default='Unknown Manufacture Year').split('|')[0],
                Deeplink=car_ad.css('a._1Lu5u::attr(href)').get(default='Unknown Deeplink'),
                Fuel_Type=car_ad.css('p._1i1E6::text').get(default='Unknown Fuel Type').split('|')[1],
                Price=car_ad.css('span._7yds2::text').get(default='Unknown Price'),
                Model=car_ad.css('h3.RZ4T7::text').get(default='Unknown Brand').split(' ')[1],
                Mileage=car_ad.css('ul._3ZoHn li:nth-child(2)::text').get(default='Unknown Mileage'),
            )
            yield item

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

    def start_requests(self):
        # Define the URL and headers
        start_url = 'https://listing-service.c24.tech/v2/vehicle?isSeoFilter=true&sf=city:DU&sf=gaId:1738878581.1695743410&size=25&spath=buy-used-cars-dubai&page={}&variant=filterV5'
        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-GB,en;q=0.9,en-US;q=0.8",
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "sec-ch-ua": "\"Microsoft Edge\";v=\"117\", \"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"117\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "x_country": "AE",
            "x_vehicle_type": "CAR"
        }

        # Change this to the desired number of pages
        num_pages = 5

        # Make requests for each page
        for page in range(1, num_pages + 1):
            url = start_url.format(page)
            yield scrapy.Request(
                url=url,
                headers=headers,
                callback=self.parse
            )

    def parse(self, response: Response, **kwargs: Any) -> Any:
        data = json.loads(response.text)

        if "results" in data:
            for car_ad in data["results"]:
                item = JunDevAssignmentItem(
                    Brand=car_ad['make'],
                    Engine_Size=car_ad['engineSize'],
                    Year_of_Manufacture=car_ad['year'],
                    Deeplink=car_ad['checkoutUrl'],
                    Fuel_Type=car_ad['fuelType'],
                    Price=car_ad['price'],
                    Model=car_ad['model'],
                    Mileage=car_ad['odometerReading']
                )
                yield item

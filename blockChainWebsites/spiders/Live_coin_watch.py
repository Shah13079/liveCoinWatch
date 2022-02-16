import scrapy
import json
from ..utilties import user_agents, payload_url
from ..items import BlockchainwebsitesItem


class LiveCoinWatchSpider(scrapy.Spider):
    """This is our main spider class

    Args:
        scrapy (framework): class in inherited with scrapy framework written in python for crawling websites.
    """

    name = "live_coint"

    allowed_domains = ["www.livecoinwatch.com", "http-api.livecoinwatch.com"]

    default_url = "https://http-api.livecoinwatch.com/coins?"

    def __init__(self, start_page=1, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.starting_page = (int(start_page) - 1) * 50
        
        self.payload = {
            "offset": self.starting_page,
            "limit": "50",
            "sort": "rank",
            "order": "ascending",
            "currency": "USD",
            "platforms": "",
        }

    def start_requests(self):

        """In scrapy we start sending Requests to target URL in start_requests methood.

        scrapy.Request:
                        Sending Request to target Url with supported
                        Arguments, and sending response back to method provided to callback.
        """

        yield scrapy.Request(
            url=self.default_url + payload_url(self.payload),
            callback=self.parse,
            headers={"User-agent": user_agents},
            method="GET",
            body=json.dumps(self.payload),
        )

    def parse(self, response):

        """Receiving the Response object from the Request

        Args:
            response (selector): Receiving the response object

        Yields:
            Generator: used for Returning dict and sending Request to server
        """

        items = BlockchainwebsitesItem()

        parse_as_dict = json.loads(response.body)
        listings = parse_as_dict["data"]
        total = parse_as_dict["total"]

        for each_listings in listings:
            items["code"] = each_listings.get("code")
            items["name"] = each_listings.get("name")
            items["color"] = each_listings.get("color")
            items["rank"] = each_listings.get("rank")
            items["price"] = each_listings.get("price")
            items["cap"] = each_listings.get("cap")
            items["totalCap"] = each_listings.get("totalCap")
            items["maxSupply"] = each_listings.get("maxSupply")
            items["totalSupply"] = each_listings.get("totalSupply")
            items["circulating"] = each_listings.get("circulating")
            items["issued"] = each_listings.get("issued")
            items["volmcap"] = each_listings.get("volmcap")
            items["exchanges"] = each_listings.get("exchanges")
            items["elisted"] = each_listings.get("elisted")
            items["twitter"] = each_listings.get("twitter")
            items["reddit"] = each_listings.get("reddit")
            items["telegram"] = each_listings.get("telegram")
            items["delta"] = str(each_listings.get("delta"))
            items["deltav"] = str(each_listings.get("deltav"))

            yield items

        if self.payload["offset"] < int(total):
            self.payload["offset"] += 50

            yield scrapy.Request(
                url=self.default_url + payload_url(self.payload),
                callback=self.parse,
                headers={"User-agent": user_agents},
                method="GET",
                body=json.dumps(self.payload),
            )

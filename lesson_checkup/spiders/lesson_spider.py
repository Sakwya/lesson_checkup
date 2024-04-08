import scrapy
from scrapy.http import Response
from scrapy_splash import SplashRequest

import lesson_checkup
from . import autostart
import importlib


class LessonSpider(scrapy.Spider):
    name = 'lesson'
    def start_requests(self):
        container = None
        if autostart == 'true':
            splash = importlib.import_module('lesson_checkup.splash')
            container = splash.Splash()
            container.run()

        # yield SplashRequest(url, self.parse_result,
        #                     args={
        #                         # optional; parameters passed to Splash HTTP API
        #                         'wait': 0.5,
        #
        #                         # 'url' is prefilled from request url
        #                         # 'http_method' is set to 'POST' for POST requests
        #                         # 'body' is set to request body for POST requests
        #                     },
        #                     endpoint='render.json',  # optional; default is render.html
        #                     splash_url='<url>',  # optional; overrides SPLASH_URL
        #                     slot_policy=scrapy_splash.SlotPolicy.PER_DOMAIN,  # optional
        #                     )

        if autostart == 'true':
            container.stop()

    def parse(self, response: Response, **kwargs):
        pass

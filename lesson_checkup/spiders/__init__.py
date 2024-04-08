# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

autostart = config['Docker']['autostart']

from .lesson_spider import LessonSpider

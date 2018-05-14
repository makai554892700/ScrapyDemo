# -*- coding: utf-8 -*-
import sys
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from ScrapyDemo.spiders.news_estadao import EstadaoSpider
from ScrapyDemo.spiders.news_gazetaesportiva import DemoSpider
from ScrapyDemo.spiders.news_megacurioso import MegacuriosoSpider

if sys.getdefaultencoding != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

process = CrawlerProcess(get_project_settings())
process.crawl(EstadaoSpider)
process.crawl(DemoSpider)
process.crawl(MegacuriosoSpider)
process.start()

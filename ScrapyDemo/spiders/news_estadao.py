# -*- coding: utf-8 -*-
import scrapy, sys
from ScrapyDemo.items import ScrapydemoItem
from ScrapyDemo.utils.time_utils import get_pt_time

if sys.getdefaultencoding != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')


class EstadaoSpider(scrapy.Spider):
    name = 'news_estadao'
    allowed_domains = ['www.estadao.com.br']
    start_urls = ['http://www.estadao.com.br/ultimas']
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'utf-8',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Host': 'www.estadao.com.br',
        'Pragma': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    }

    def parse(self, response):
        print('Start parse.')
        for element in response.xpath("//section[@class='col-md-12 col-sm-12 col-xs-12 init item-lista']"):
            title = element.xpath(".//a[@class='link-title']/h3[1]/text()").extract_first()
            imageUrl = [element.xpath(".//img[@class='elazy']/@data-src-desktop").extract_first()]
            des = element.xpath(".//a[@class='link-title']/p[1]/text()").extract_first()
            source = 'estadao'
            actionUrl = element.xpath(".//a[@class='link-title']/@href").extract_first()
            contentType = ''
            itemType = ''
            createTime = get_pt_time(element.xpath(".//span[@class='data-posts']/text()").extract_first().encode("utf-8"))
            country = 'PZ'
            headUrl = ''
            if title is not None and title != "" and actionUrl is not None and actionUrl != "" and imageUrl is not None and imageUrl != "":
                item = ScrapydemoItem()
                item['title'] = title
                item['imageUrl'] = imageUrl
                item['des'] = des
                item['source'] = source
                item['actionUrl'] = actionUrl
                item['contentType'] = contentType
                item['itemType'] = itemType
                item['createTime'] = createTime
                item['country'] = country
                item['headUrl'] = headUrl
                yield item
        print('End parse.')

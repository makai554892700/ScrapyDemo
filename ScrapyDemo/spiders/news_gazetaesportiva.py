# -*- coding: utf-8 -*-
import scrapy
from ScrapyDemo.items import ScrapydemoItem


class DemoSpider(scrapy.Spider):
    name = 'news_gazetaesportiva'
    allowed_domains = ['www.gazetaesportiva.com']
    start_urls = ['https://www.gazetaesportiva.com/noticias/']
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    }

    def parse(self, response):
        print('Start parse.')
        for element in response.xpath('//article'):
            title = element.xpath(".//h3[@class='entry-title no-margin']/a/text()").extract_first()
            imageUrl = [element.xpath(".//img[@class='medias-object wp-post-image']/@src").extract_first()]
            des = element.xpath(".//div[@class='entry-content space']/text()").extract_first()
            source = 'gazeta'
            actionUrl = element.xpath(".//a[@class='blog-image']/@href").extract_first()
            contentType = ''
            itemType = ''
            createTime = element.xpath(".//small[@class='updated']/text()").extract_first()
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

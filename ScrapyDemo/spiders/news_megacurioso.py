# -*- coding: utf-8 -*-
import scrapy, json, sys
from ScrapyDemo.items import ScrapydemoItem
from ScrapyDemo.utils import time_utils

if sys.getdefaultencoding != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')


class MegacuriosoSpider(scrapy.Spider):
    name = 'news_megacurioso'
    allowed_domains = ['www.megacurioso.com.br']
    start_urls = ['http://www.megacurioso.com.br/']
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'utf-8',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Host': 'www.megacurioso.com.br',
        'Pragma': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    }

    def parse(self, response):
        print('Start parse.')
        str = response.xpath("//script[@id='json-script']").extract_first().encode("utf-8")
        mark_str = "window._mosaicJson ="
        start = str.index(mark_str) + len(mark_str)
        str = str[start:(len(str) - 16)]
        datas = json.loads(str)['data']
        for data in datas:
            title = data['Title']
            imageUrl = [data['Image']]
            des = data['Chamada']
            source = data['NomeAutor']
            actionUrl = data['Social']['Url']
            contentType = ''
            itemType = ''
            createTime = time_utils.format_time(data['DateISO'])
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

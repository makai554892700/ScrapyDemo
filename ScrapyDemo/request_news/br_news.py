#!/usr/bin/env python
# encoding: utf-8
import json, requests, sys, commands

if sys.getdefaultencoding != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

URL_GLOBO = 'https://falkor-cda.bastian.globo.com/feeds/ce198dac-feb2-43d3-bc58-22e6148ae268/posts/page/1'
TAG_GLOBO = 'globo'
GLOBO_HEADERS = {'accept': '*/*',
                 'accept-encoding': 'gzip, deflate, br',
                 'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
                 'origin': 'http://globoesporte.globo.com',
                 'referer': 'http://globoesporte.globo.com/futebol/',
                 'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}


def get_globo_create_time(time_str):
    return time_str[0:16].replace('T', ' ')


def get_globo():
    global URL_GLOBO, GLOBO_HEADERS, TAG_GLOBO
    result = []
    try:
        response_str = requests.get(URL_GLOBO, headers=GLOBO_HEADERS)
    except:
        print 'Get request error.'
        return result
    if response_str.status_code == 200:
        response_obj = json.loads(response_str.text)
        for item in response_obj['items']:
            if 'materia' == item['type']:
                try:
                    result.append({
                        'title': item['content']['title'],
                        'imageUrl': [item['content']['image']['sizes']['S']['url']],
                        'des': item['content']['summary'],
                        'source': response_obj['source'],
                        'actionUrl': item['content']['url'],
                        'contentType': '',
                        'itemType': '',
                        'createTime': get_globo_create_time(item['created']),
                        'country': 'PT',
                        'headUrl': 'https://s2.glbimg.com/7IvhrrApqilJPuP2ccpEYCfJK_k=/32x32/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_bc8228b6673f488aa253bbcb03c80ec5/internal_photos/bs/2018/f/L/FlDVTgTqe0Xif1LlZH9A/favicon.png'
                    })
                except:
                    print 'Get response error.'
            else:
                print 'type=' + item['type']
                print json.dumps(item)
    else:
        print 'Get request code error.'
    result.reverse()
    return result


def get_estadao():
    result = []
    try:
        commands.getoutput("echo '' > /tmp/estadao.json")
        commands.getoutput("scrapy crawl news_estadao -o /tmp/estadao.json")
        result = json.loads(commands.getoutput("cat /tmp/estadao.json"))
    except:
        print "Get estadao error."
    result.reverse()
    return result


def get_gazetaesportiva():
    result = []
    try:
        commands.getoutput("echo '' > /tmp/gazetaesportiva.json")
        commands.getoutput("scrapy crawl news_gazetaesportiva -o /tmp/gazetaesportiva.json")
        result = json.loads(commands.getoutput("cat /tmp/gazetaesportiva.json"))
    except:
        print "Get gazetaesportiva error."
    result.reverse()
    return result


def get_megacurioso():
    result = []
    try:
        commands.getoutput("echo '' > /tmp/megacurioso.json")
        commands.getoutput("scrapy crawl news_megacurioso -o /tmp/megacurioso.json")
        result = json.loads(commands.getoutput("cat /tmp/megacurioso.json"))
    except:
        print "Get megacurioso error."
    result.reverse()
    return result


def common_save_all_news():
    globo = get_globo()
    estadao = get_estadao()
    gazetaesportiva = get_gazetaesportiva()
    megacurioso = get_megacurioso()
    print(json.dumps(globo))
    print(json.dumps(estadao))
    print(json.dumps(gazetaesportiva))
    print(json.dumps(megacurioso))


if __name__ == '__main__':
    common_save_all_news()

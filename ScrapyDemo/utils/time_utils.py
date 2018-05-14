# -*- coding: utf-8 -*-
import time, re, sys

if sys.getdefaultencoding != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

PT_MONTH = {
    'janeiro': '1',
    'fevereiro': '2',
    'março': '3',
    'abril': '4',
    'maio': '5',
    'junho': '6',
    'julho': '7',
    'agosto': '8',
    'setembro': '9',
    'outubro': '10',
    'novembro': '11',
    'dezembro': '12'
}


def get_current_time():
    return time.strftime("%Y-%m-%d %H:%M", time.localtime(time.time()))


def format_time(time_str):
    return time_str[0:16].replace('T', ' ')


def get_pt_time(time_str):
    global PT_MONTH
    reg = re.compile('^(?P<day>[^ ]*) de (?P<month>[^ ]*) de (?P<year>[^ ]*) \| (?P<hour>[^ ]*)h(?P<minute>[^ ]*)')
    regMatch = reg.match(time_str)
    linebits = regMatch.groupdict()
    return linebits.get('year') + "-" + PT_MONTH[str(linebits.get('month')).lower()] + "-" \
           + linebits.get('day') + " " + linebits.get('hour') + ":" + linebits.get('minute')


if __name__ == '__main__':
    print get_pt_time("11 de Maio de 2018 | 00h10")

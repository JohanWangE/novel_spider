#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
__author__ = 'meng'

class Row(dict):
    def __getattr__(self,name):
        try:
            return self[name]
        except KeyError:
            raise  AttributeError(name)


type = Row(
    {
        '22mt': Row({
            "site_name": "墨坛文学",
            "site_url": "http://www.22mt.com/",
            "chapter_list": "//div[@class='book_listtext']",
            "content": "//div[@id='booktext']/text()",
            "filter": ["/墨坛文学", "墨坛文学网"],
        }),
        'fftxt':Row({
            "site_name":"非凡文学",
            "site_url":"http://www.fftxt.net/",
            "book":"//div[@class='book_news_style_text2']/h1/text()",
            "author":"",
            "chapter_list":"//ul[@id='chapterlist']/li",
            "content":"//div[@class='novel_content']/text()",
            "filter":["非凡TXT下载","www.fftxt.net"]
        }),
        'siluke':Row({
            "site_name":'思路客',
            "site_url":'http://www.siluke.com/',
            "book":"//div[@id='bread']/strong/text()",
            "author":"//div[@id='details']/a[1]/text()",
            "chapter_list":"//div[@id='list']/dl/dd",
            "content":"//div[@id='content']/text()",
            "filter":[],
            "regex":r""
        }),
        'base':Row({
            "site_name":"",
            "site_url":"",
            "book":"",
            "author":"",
            "chapter_list":"",
            "content":"",
            "filter":[],
            "regex":r""
        }),
        'biquge':Row({
            "site_name":"笔趣阁",
            "site_url":"http://www.biquge.com/",
            "book":"//div[@id='info']/h1/text()",
            "author":"",
            "chapter_list":"//div[@id='list']/dl/dd",
            "content":"//div[@id='content']/text()",
            "filter":[],
            "regex":r"\/(?P<cid>\d+)\.html"
        }),

    }
)

#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 解析 Feed 的库
import feedparser
# 解析 html xml 的库
from bs4 import BeautifulSoup
import urllib2
from os.path import basename
from urlparse import urlsplit
import os


try:
    feed_ = feedparser.parse("feed.xml")
    count = len(feed_['entries'])
    counts = [i for i in range(count)]

    #文章标题
    #titles = [feed_.entries[x].title for x in counts]
    #print titles

	#文章作者
    #authors = [feed_.entries[x].author for x in counts]
    #print feed_.entries[0].author

    #文章内容
    #descriptions = [feed_.entries[x].content for x in counts]
    #print descriptions
    #content = [descriptions[x][0].value for x in counts]
    #print content
    print feed_.entries[0].title
    print feed_.entries[0].author
    #print feed_.entries[0].content[0].value
    #description_soup = beautifulsoup(''.join(feed_.entries[0].content[0].value))
    cont = feed_.entries[0].content[0].value
    #print cont
    imc = BeautifulSoup(cont)
    #print imc
    #print len(imc.find_all('img'))
    i=0
    for i in range(len(imc.find_all('img'))):
        img_src = imc.find_all('img')[i]['src']
        print img_src

except:
    print 'RSS 源有问题，请检查！'
    exit()




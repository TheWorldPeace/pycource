#!/usr/bin/env python3

#coding: utf-8
import sys
import urllib
import urllib2
from BeautifulSoup import BeautifulSoup

question_name ="jianghp92"
url ="http://www.baidu.com/s?wd="+ urllib.quote(question_name.decode(sys.stdin.encoding).encode('gbk'))
htmlpage = urllib2.urlopen(url).read()
soup = BeautifulSoup(htmlpage)
print len(soup.findAll("table", {"class":"result"}))
for result_table in soup.findAll("table", {"class":"result"}):
 a_click = result_table.find("a")
 print"----����----n"+ a_click.renderContents()#����
 print"----����----n"+ str(a_click.get("href"))#����
 print"----����----n"+ result_table.find("div", {"class":"c-abstract"}).renderContents()#����
print
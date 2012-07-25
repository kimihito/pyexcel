#!/usr/bin/env python
# coding: utf-8
import xlwt
import cgi
from datetime import date

def printItem(item):
    name,price,piece = item
    print "<h2>Result</h2><br />" 
    print u"品名".encode('utf-8')
    print unicode(name,"utf-8").encode('utf-8')
    print "<br \>"
    print u"価格:".encode('utf-8')
    print unicode(price,"utf-8").encode('utf-8')
    print "<br \>"
    print u"個数:".encode('utf-8')
    print unicode(piece,"utf-8").encode('utf-8')
    print "<br \>"

def putItem(row,item):
    name,price,piece = item

    row.write(0,name)
    row.write(1,price)
    row.write(2,piece)

def printError():
    print "<h1>ERROR</h1>\n\n"
    print "someform(s) are empty"


print "Content-Type: text/html;charset=UTF-8\n\n"

print "<html><body>"

form = cgi.FieldStorage()
if form.has_key("name") and form.has_key("price") and form.has_key("piece"):

    params = [form.getlist(param) for param in ["name","price","piece"]]

    items =  zip(*params)

    book = xlwt.Workbook()
    newsheet = book.add_sheet(u"商品登録")

    for i,item in enumerate(items):
        row = newsheet.row(i+1)
        putItem(row, item)
        printItem(item)

else:
    printError()

print "</body></html>"

date = date.today()
book.save(str(date) + ".csv")


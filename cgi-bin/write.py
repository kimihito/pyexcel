#!/usr/bin/env python
# coding: utf-8
import xlwt
import cgi
from datetime import date

print "Content-Type: text/html;charset=UTF-8\n\n"

print "<html><body>"

form = cgi.FieldStorage()
form_ok = 0
if form.has_key("name") and form.has_key("price") and form.has_key("piece"):
   form_ok = 1
   name = form["name"].value
   price = form["price"].value
   piece = form["piece"].value
#   name = unicode(form["name"].value,"utf-8")
#   price = unicode(form["price"].value,"utf-8")
#   piece = unicode(form["piece"].value,"utf-8")

if form_ok == 1:
  book = xlwt.Workbook(encoding='utf-8')
  NewSheet_1 = book.add_sheet("NewSheet_2")
  newSheet_1_row_1 = NewSheet_1.row(1)
  newSheet_1_row_1.write(0,name)
  newSheet_1_row_1.write(1,price)
  newSheet_1_row_1.write(2,piece)

#for文で登録した商品全部表示させれるようにする
  print "<h2>Result</h2><br />" 
  str1 = u"品名:"
  print str1.encode('utf-8')
  print unicode(name,"utf-8").encode('utf-8')
  print "<br \>"
  str2 = u"価格:"
  print str2.encode('utf-8')
  print unicode(price,"utf-8").encode('utf-8')
  print "<br \>"
  str3 = u"個数:"
  print str3.encode('utf-8')
  print unicode(piece,"utf-8").encode('utf-8')
  print "<br \>"
else:
  print "<h1>ERROR</h1>\n\n"
  print "someform(s) are empty"

print "</body></html>"

#book.save(str(date.today()) +".xls")
date = date.today()
book.save(str(date) + ".csv")

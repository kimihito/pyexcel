#!/usr/bin/env python
# coding: utf-8
import xlwt
import cgi
from datetime import date

print "Content-Type: text/html\n\n"

print "<html><body>"

form = cgi.FieldStorage()
form_ok = 0
if form.has_key("name") and form.has_key("price") and form.has_key("piece"):
    form_ok = 1

if form_ok == 1: 
  book = xlwt.Workbook()
  NewSheet_1 = book.add_sheet("NewSheet_2")

  newSheet_1_row_1 = NewSheet_1.row(1)
  newSheet_1_row_1.write(0,form["name"].value)
  newSheet_1_row_1.write(1,form["price"].value)
  newSheet_1_row_1.write(2,form["piece"].value)

  book.save(date.today() +'.csv')

  print "<h2>Result</h2><p>"
  print "<p><b>name:</b>", form["name"].value
else:
  print "<h1>ERROR</h1>\n\n"
  print "someform(s) are empty"

print "</body<</html>"

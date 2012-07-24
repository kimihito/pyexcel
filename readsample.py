#!/usr/bin/env python
# coding: utf-8

import xlrd

if __name__ == "__main__":
  
  book = xlrd.open_workbook('sample.xls')

  print "-----------------"
  print book.nsheets


  print "-----------------"
  for name in book.sheet_names():
    print name



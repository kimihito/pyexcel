#!/usr/bin/env python
# coding: utf-8
import xlwt

if __name__ == "__main__":

  book = xlwt.Workbook()
  newSheet_1 = book.add_sheet("NewSheet_1")

  newSheet_1.write(0,0,"A1")

  newSheet_1_row_1 = newSheet_1.row(1)
  newSheet_1_row_1.write(0,"A2")
  newSheet_1_row_1.write(1,"B2")
  newSheet_1_row_1.write(2,"C2")
  newSheet_1_row_1.write(3,"D2")
  newSheet_1_row_1.write(4,"E2")

  book.save('sample.csv')

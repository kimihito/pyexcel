#!/usr/bin/env python
# coding: utf-8
import xlwt
import xlrd
import sys
from datetime import datetime


#入力した言葉をExcelにプロットして、表示(場所の指定はなし)
def write(word):
  # ⇨入力した言葉を関数に渡す
  argv = sys.argv

  # ⇨Excelに渡した言葉をいれる
  book = xlwt.Workbook()
  newSheet_1 = book.add_sheet("testsheet_1")

  #場所の指定(引数ごとに変更する今のところ0,0)
  newSheet_1.write(0,0,word)

  #csvのファイルで保存
  #ファイル名+作成日時で保存
  time = str(datetime.now())
  book.save("testsheet_1_" + time + ".csv")

if __name__ == '__main__':
  #コマンドラインからの入力
  write(sys.argv[1:])

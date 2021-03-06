# this is for importing xml and pdf files from sources and change xml file encodings from euc-jp to utf-8.
#coding:utf-8

import shutil
import os
import codecs
import sys
import datetime
from pathlib import Path

ipt = ""
opt = ""

# テスト用ディレクトリ
# ipt = "/Users/k-fukuzawa/Dropbox/tmp/01input/"
# opt = "/Users/k-fukuzawa/Dropbox/tmp/01output/"

# コマンドライン引数を使ってインプットディレクトリとアウトプットディレクトリを指定する
# 1はインプット，2はアウトプットディアレク取りを指定する

if len(sys.argv) < 2:
      print("インプットディレクトリを入力してください")
      sys.exit()
if len(sys.argv) < 3:
      print("アウトプットディレクトリを入力してください")
      sys.exit()


ipt = sys.argv[1]
opt = sys.argv[2]

ipt_path = Path(ipt)
opt_path = Path(opt)

def copy_xml_and_chg_ipt_codec(ipt, opt):
    ipt_path = Path(ipt)
    opt_path = Path(opt)
    xml_path = ipt_path.glob('**/*.xml')
    for i in xml_path:
        with open(str(opt_path) + '/' + i.name, 'w', encoding='utf_8') as f_out:
            print(opt_path, i.name)
            with open(i, encoding='euc_jp') as f_in:
                # 下記はxmlからcsvに変換する際に、euc-jpの記載があると「マルチバイト文字列は使えません」みたいなエラーが出て進まないのでやむを得ず外科手術を行った結果がこれである…
                f_out.write(f_in.read().replace('<?xml version="1.0" encoding="EUC-JP"?>', '<?xml version="1.0" encoding="UTF-8"?>'))
def copy_pdf(ipt, opt): #copy pdf file
    ipt_path = Path(ipt)
    opt_path = Path(opt)
    pdf_path = ipt_path.glob('**/*.pdf')
    for i in pdf_path:
        print(opt_path, i.name )
        shutil.copyfile(i, str(opt_path) + '/' + i.name)

copy_xml_and_chg_ipt_codec(ipt, opt)
now = datetime.datetime.now()
print("----------------------------------------")
print("{0}: {1:%Y/%m/%d %H:%M} xml copy files done.".format(opt_path, now))
print("----------------------------------------")
with open(str(opt_path) + '/' + '_output_result.txt', 'a', encoding='utf_8') as f_out:
    f_out.write("{0}: {1:%Y/%m/%d %H:%M} xml copy files done.\n".format(opt_path, now))

copy_pdf(ipt, opt)
now = datetime.datetime.now()
print("----------------------------------------")
print("{0}: {1:%Y/%m/%d %H:%M} pdf copy files done.".format(opt_path, now))
print("----------------------------------------")
with open(str(opt_path) + '/' + '_output_result.txt', 'a', encoding='utf_8') as f_out:
    f_out.write("{0}: {1:%Y/%m/%d %H:%M} pdf copy files done.\n".format(opt_path, now))
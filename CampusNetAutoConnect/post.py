#!/usr/bin/env python
# -* - coding: utf-8 -* -
# @Time : 2021/1/285:21
# @Author: Suyongbiao
# @File: post

import requests
from time import sleep
from subprocess import run, PIPE

post_addr = "https://drcom.szu.edu.cn/a70.htm"

# post_header = {
#     'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
#     'Connection': 'keep-alive',
#     'Content-Length': '66',
#     'Content-Type': 'application/x-www-form-urlencoded',
#     'Cookie': 'program=szdx_wlan0718; vlan=3431; ip=172.31.104.162; md5_login2=330385%7Csu/358779',
#     'Host': 'drcom.szu.edu.cn',
#     'Origin': 'https://drcom.szu.edu.cn',
#     'Referer': 'https://drcom.szu.edu.cn/a70.htm',
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
# }

post_data = {
    'DDDDD':'330385',
    'upass':'su/358779',
    'R1': '0',
    'R2': '',
    'R6': '0',
    'para': '00',
    '0MKKey':'123456'
}

while True:
    r = run('ping www.baidu.com', stdout=PIPE, stderr=PIPE, stdin=PIPE)
    if r.returncode:
        z = requests.post(post_addr, data = post_data)
        print('ok')
    else:
        sleep(60*10)

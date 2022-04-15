#!/usr/bin/env python
# encoding: utf-8
"""
@Author: Lekwe
@License: (C) Copyright 2013-2021, Lekwe Armat co.,ltd
@Contact: zscleo@qq.com leokeyn@sina.cn
@Software: Pycharm
@File: Main.py
@Time: 2021/2/8 15:38
@Desc:
"""
from requests import *
from bs4 import BeautifulSoup
import os
import lxml
import winreg
from colorama import Fore, Back, init

a = lxml
init(autoreset=True)

while True:
    def isConnected(url):
        try:
            test = get(url=url, timeout=2)
            return True
        except:
            return False


    returns = isConnected("http://180.97.33.108/")
    if returns:
        while True:
            print(Fore.CYAN + "请输入歌曲id或歌曲链接(酷我):", end='')
            songinfo = str(input(" "))
            songid = songinfo.replace('http://www.kuwo.cn/play_detail/', '').replace('https://www.kuwo.cn/play_detail/',
                                                                                     '').replace('www.kuwo.cn/play_detail/', '')
            url = "http://www.kuwo.cn/api/v1/www/music/playUrl?mid={}&type=music&httpsStatus=1&reqId=c3ca9201-4da8-11ec-bf5f-6321ab9e6552".format(
                songid)
            headers = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.63",
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                "Cookie": "_ga=GA1.2.1020771698.1616155957; _gid=GA1.2.231281904.1617449349; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1617449349,1617500181,1617506562,1617506927; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1617506962; _gat=1; kw_token=6XI6QB43639",
                "csrf": "6XI6QB43639",
                "Referer": "https://www.kuwo.cn/search/list?key=%E9%94%99%E4%BD%8D%E6%97%B6%E7%A9%BA",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Host": "www.kuwo.cn",
                "Pragma": "no-cache",
                "Upgrade-Insecure-Requests": "1"
            }

            try:
                req = get(url=url, headers=headers).text
                pe1 = req.split('"')
                songurl = pe1[15]
                res = get("http://www.kuwo.cn/play_detail/" + songid)
                res.encoding = 'utf-8'  #
                soup = BeautifulSoup(res.text, 'html.parser')
                song = soup.title.text
                name = str(song).replace('_单曲在线试听_酷我音乐', '').replace('_', '-')
                f1 = "?"
                f2 = "<"
                f3 = ">"
                f4 = ":"
                f5 = "/"
                f6 = '\\'
                f7 = "|"
                f8 = "*"
                f9 = '"'
                names = list(name)
                try:
                    i = names.index(f1)
                    names.pop(i)
                    names.insert(i, '-')
                    print(Fore.YELLOW + "歌曲名中含有特殊符号“?”,已更换为“-”")
                except:
                    pass
                try:
                    i2 = names.index(f2)
                    names.pop(i2)
                    names.insert(i2, '-')
                    print(Fore.YELLOW + "歌曲名中含有特殊符号“<”,已更换为“-”")
                except:
                    pass
                try:
                    i3 = names.index(f3)
                    names.pop(i3)
                    names.insert(i3, '-')
                    print(Fore.YELLOW + "歌曲名中含有特殊符号“>”,已更换为“-”")
                except:
                    pass
                try:
                    i4 = names.index(f4)
                    names.pop(i4)
                    names.insert(i4, '-')
                    print(Fore.YELLOW + "歌曲名中含有特殊符号“:”,已更换为“-”")
                except:
                    pass
                try:
                    i5 = names.index(f5)
                    names.pop(i5)
                    names.insert(i5, '-')
                    print(Fore.YELLOW + "歌曲名中含有特殊符号“/”,已更换为“-”")
                except:
                    pass
                try:
                    i6 = names.index(f6)
                    names.pop(i6)
                    names.insert(i6, '-')
                    print(Fore.YELLOW + r"歌曲名中含有特殊符号“\”,已更换为“-”")
                except:
                    pass
                try:
                    i7 = names.index(f7)
                    names.pop(i7)
                    names.insert(i7, '-')
                    print(Fore.YELLOW + "歌曲名中含有特殊符号“|”,已更换为“-”")
                except:
                    pass
                try:
                    i8 = names.index(f8)
                    names.pop(i8)
                    names.insert(i8, '-')
                    print(Fore.YELLOW + "歌曲名中含有特殊符号“*”,已更换为“-”")
                except:
                    pass
                try:
                    i9 = names.index(f9)
                    names.pop(i9)
                    names.insert(i9, '-')
                    print(Fore.YELLOW + '歌曲名中含有特殊符号“"”,已更换为“-”')
                except:
                    pass
                name2 = "".join(names)
                if name2 == "服务错误":
                    print(Fore.BLACK + Back.RED + "酷我音乐服务器服务错误或你的链接、id错误，无法下载。请检查你的链接、id或稍后重试")
                    print(server-error)
                if songurl == "failed":
                    print(Fore.BLACK + Back.RED + "你输入的链接或id有误，请检查你的链接或id")
                    pass
                print(Fore.GREEN + "已或取到歌曲名称: " + str(name2))
                print(Fore.GREEN + "正在下载“{}”".format(name2))
                rp = get(url=songurl)
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                     r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
                wd = winreg.QueryValueEx(key, "Desktop")[0]
                path = wd
                if not os.path.exists(path + "\\music\\"):
                    os.mkdir(path + "\\music")

                filepath = path + "\\music\\" + "{}.mp3".format(name2)
                if os.path.exists(filepath):
                    print(Fore.YELLOW + Back.BLACK + "文件存在,已覆盖")
                    with open(filepath, 'wb') as f:
                        f.write(rp.content)
                else:
                    with open(filepath, 'wb') as f:
                        f.write(rp.content)
                print(Fore.GREEN + Back.BLACK + "下载成功,已存储到{}".format(filepath))
            except Exception as ex:
                def isConnected(url):
                    try:
                        test = get(url=url, timeout=2)
                        return True
                    except:
                        return False
                returns = isConnected("http://180.97.33.108/")
                if returns:
                    print(
                        Fore.BLUE + Back.BLACK + "爬取失败，请检查你的链接或id、网络设置，或代理设置，若都设置正常，请稍后再试，或向我们反馈下方" + Fore.YELLOW + "黄色" + Fore.BLUE + "英文错误信息:\n总工:张书畅\n邮箱:zscleo@qq.com\n    "
                                                 " abc.lkw@aliyun.com\nQQ:1144757260\n电话:18953021320\n副总工:赵子汉\n邮箱:a_1666666@126.com\n   "
                                                 "  a_1666666@yeah.net\nQQ:3199398113\n电话:13256210166\n帮助文档: https://support.lekwe.rf.gd/getkuwo/faq/doc/#")
                    print(Fore.YELLOW + str(ex))
                else:
                    print(Back.RED + Fore.BLACK + "你的网络未连接，请检查你的网络连接。")
                    print(
                        Fore.BLUE + Back.BLACK + "爬取失败，请检查你的链接或id、网络设置，或代理设置，若都设置正常，请稍后再试，或向我们反馈下方" + Fore.YELLOW + "黄色" + Fore.BLUE + "英文错误信息:\n总工:张书畅\n邮箱:zscleo@qq.com\n    "
                                                 " abc.lkw@aliyun.com\nQQ:1144757260\n电话:18953021320\n副总工:赵子汉\n邮箱:a_1666666@126.com\n   "
                                                 "  a_1666666@yeah.net\nQQ:3199398113\n电话:13256210166")
                    print(Fore.YELLOW + str(ex))
    else:
        print(Fore.YELLOW + "你的网络未连接，请检查你的网络连接,设置好后按下回车键继续")
        input()

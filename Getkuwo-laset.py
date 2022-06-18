#!/usr/bin/env python
# encoding: utf-8
"""
@Author: Lekwe
@License: (C) Copyright 2013-2021, Lekwe Armat co.,ltd
@Contact: zscleo@qq.com leokeyn@sina.cn
@Software: Pycharm
@File: 1.py
@Time: 2021/4/4 11:31
@Desc:
"""
import requests
import json
from bs4 import BeautifulSoup
import lxml
import parser
import os
import sys
import winreg
from urllib.parse import quote
from colorama import Fore, Back, init
import headers
import time

os.environ['REQUESTS_CA_BUNDLE'] = os.path.join(os.path.dirname(sys.argv[0]), 'cacert.pem')
headers = headers.headers
init(autoreset=True)


def isConnected(url):
    try:
        test = requests.get(url=url, timeout=2)
        return True
    except Exception as ex2:
        # print(ex2)
        return False


while True:
    returns = isConnected("http://baidu.com/")
    print('初始化完成')
    # print(returns)
    if returns:
        print('已连接服务器')
        while True:
            ab = 1
            try:
                print(Fore.BLUE + Back.BLACK + '请输入要下载的歌名: ', end='', flush=True)
                sn = str(input(''))
                if sn == 'imzsc':
                    print('我靠( ‵o′)凸，你竟然发现了彩蛋！')
                    time.sleep(1)
                    # print('彩蛋链接:{}'.format())
                name = 'https://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={}'.format(sn)

                a = requests.get(name, headers=headers)
                rid0 = json.loads(a.text).get("data").get("list")[0].get("rid")
                res = requests.get("http://www.kuwo.cn/play_detail/" + str(rid0))
                res.encoding = 'utf-8'  #
                soup = BeautifulSoup(res.text, 'html.parser')
                song = soup.title.text
                names0 = str(song).replace('_单曲在线试听_酷我音乐', '').replace('_', '-')

                a = requests.get(name, headers=headers)
                ridx = json.loads(a.text).get("data").get("list")[0].get("rid")
                res = requests.get("http://www.kuwo.cn/play_detail/" + str(ridx))
                res.encoding = 'utf-8'  #
                soup = BeautifulSoup(res.text, 'html.parser')
                song = soup.title.text
                namesx = str(song).replace('_单曲在线试听_酷我音乐', '').replace('_', '-')

                a = requests.get(name, headers=headers)
                rid1 = json.loads(a.text).get("data").get("list")[0].get("rid")
                res = requests.get("http://www.kuwo.cn/play_detail/" + str(rid1))
                res.encoding = 'utf-8'  #
                soup = BeautifulSoup(res.text, 'html.parser')
                song = soup.title.text
                names1 = str(song).replace('_单曲在线试听_酷我音乐', '').replace('_', '-')
                print("搜索结果:")
                print(Fore.BLUE + '1. ' + names1)
                list2 = json.loads(a.text).get("data").get("list")
                if len(list2) >= 2:
                    rid2 = list2[1].get("rid")
                    res = requests.get("http://www.kuwo.cn/play_detail/" + str(rid2))
                    res.encoding = 'utf-8'  #
                    soup = BeautifulSoup(res.text, 'html.parser')
                    song = soup.title.text
                    names2 = str(song).replace('_单曲在线试听_酷我音乐', '').replace('_', '-')
                    print(Fore.BLUE + '2. ' + names2)
                if len(list2) >= 3:
                    rid3 = list2[2].get("rid")
                    res = requests.get("http://www.kuwo.cn/play_detail/" + str(rid3))
                    res.encoding = 'utf-8'  #
                    soup = BeautifulSoup(res.text, 'html.parser')
                    song = soup.title.text
                    names3 = str(song).replace('_单曲在线试听_酷我音乐', '').replace('_', '-')
                    print(Fore.BLUE + '3. ' + names3)
                if len(list2) >= 4:
                    rid4 = list2[3].get("rid")
                    res = requests.get("http://www.kuwo.cn/play_detail/" + str(rid4))
                    res.encoding = 'utf-8'  #
                    soup = BeautifulSoup(res.text, 'html.parser')
                    song = soup.title.text
                    names4 = str(song).replace('_单曲在线试听_酷我音乐', '').replace('_', '-')
                    print(Fore.BLUE + '4. ' + names4)
                if len(list2) >= 5:
                    rid5 = list2[4].get("rid")
                    res = requests.get("http://www.kuwo.cn/play_detail/" + str(rid5))
                    res.encoding = 'utf-8'  #
                    soup = BeautifulSoup(res.text, 'html.parser')
                    song = soup.title.text
                    names5 = str(song).replace('_单曲在线试听_酷我音乐', '').replace('_', '-')
                    print(Fore.BLUE + '5. ' + names5)
                if len(list2) >= 6:
                    rid6 = list2[5].get("rid")
                    res = requests.get("http://www.kuwo.cn/play_detail/" + str(rid6))
                    res.encoding = 'utf-8'  #
                    soup = BeautifulSoup(res.text, 'html.parser')
                    song = soup.title.text
                    names6 = str(song).replace('_单曲在线试听_酷我音乐', '').replace('_', '-')
                    print(Fore.BLUE + '6. ' + names6)
                if len(list2) >= 7:
                    rid7 = list2[6].get("rid")
                    res = requests.get("http://www.kuwo.cn/play_detail/" + str(rid7))
                    res.encoding = 'utf-8'  #
                    soup = BeautifulSoup(res.text, 'html.parser')
                    song = soup.title.text
                    names7 = str(song).replace('_单曲在线试听_酷我音乐', '').replace('_', '-')
                    print(Fore.BLUE + '7. ' + names7)
                if len(list2) >= 8:
                    rid8 = list2[7].get("rid")
                    res = requests.get("http://www.kuwo.cn/play_detail/" + str(rid8))
                    res.encoding = 'utf-8'  #
                    soup = BeautifulSoup(res.text, 'html.parser')
                    song = soup.title.text
                    names8 = str(song).replace('_单曲在线试听_酷我音乐', '').replace('_', '-')
                    print(Fore.BLUE + '8. ' + names8)
                if len(list2) >= 9:
                    rid9 = list2[8].get("rid")
                    res = requests.get("http://www.kuwo.cn/play_detail/" + str(rid9))
                    res.encoding = 'utf-8'  #
                    soup = BeautifulSoup(res.text, 'html.parser')
                    song = soup.title.text
                    names9 = str(song).replace('_单曲在线试听_酷我音乐', '').replace('_', '-')
                    print(Fore.BLUE + '9. ' + names9)
                if len(list2) >= 10:
                    rid10 = list2[9].get("rid")
                    res = requests.get("http://www.kuwo.cn/play_detail/" + str(rid10))
                    res.encoding = 'utf-8'  #
                    soup = BeautifulSoup(res.text, 'html.parser')
                    song = soup.title.text
                    names10 = str(song).replace('_单曲在线试听_酷我音乐', '').replace('_', '-')
                    print(Fore.BLUE + '10. ' + names10)

                while ab == 1:
                    try:
                        print(Fore.WHITE + '你要下载哪一首(输入序号,输入q可重新输入歌名): ', end='')
                        i = input('')
                        i2 = i

                        if str(i2) == 'q':
                            err = 0
                            ss
                        elif 'p' in i:
                            i = i.replace('p', '')
                            i = int(i)
                            if i <= len(list2):
                                pre = 1
                                ab = 0
                            else:
                                print(Fore.RED + "你的序号有误，请检查你的序号")
                                ab = 1
                            # print(i)

                        else:
                            i = int(i)
                            if i <= len(list2):
                                ab = 0
                                pre = 0
                            else:
                                print(Fore.RED + "你的序号有误，请检查你的序号")
                                ab = 1
                    except:
                        if str(i2) == 'q':
                            err = 0
                            ss

                        else:
                            print(Fore.RED + "序号输入有误")
                            ab = 1
                if i == 1:
                    rid = rid1
                elif i == 2:
                    rid = rid2
                elif i == 3:
                    rid = rid3
                elif i == 4:
                    rid = rid4
                elif i == 5:
                    rid = rid5
                elif i == 6:
                    rid = rid6
                elif i == 7:
                    rid = rid7
                elif i == 8:
                    rid = rid8
                elif i == 9:
                    rid = rid9
                elif i == 10:
                    rid = rid10
                else:
                    a = 1

                url = "http://www.kuwo.cn/api/v1/www/music/playUrl?mid=15651705&type=convert_url3&httpsStatus=1&reqId=cd404260-eeb3-11ec-a8d6-a546fe644e18".format(
                    rid)
                req = requests.get(url=url, headers=headers).text
                pe1 = req.split('"')
                # print(pe1)
                songurl = pe1[15]
                # print(pe1)
                # print(songurl)
                f1 = "?"
                f2 = "<"
                f3 = ">"
                f4 = ":"
                f5 = "/"
                f6 = '\\'
                f7 = "|"
                f8 = "*"
                f9 = '"'
                if i == 1:
                    names = list(names1)
                elif i == 2:
                    names = list(names2)
                elif i == 3:
                    names = list(names3)
                elif i == 4:
                    names = list(names4)
                elif i == 5:
                    names = list(names5)
                elif i == 6:
                    names = list(names6)
                elif i == 7:
                    names = list(names7)
                elif i == 8:
                    names = list(names8)
                elif i == 9:
                    names = list(names9)
                elif i == 10:
                    names = list(names10)
                else:

                    a = 1

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
                    print(Fore.BLACK + Back.RED + "酷我音乐服务器服务错误或你的歌名错误，无法下载。请检查你的歌名或稍后重试")
                    print(server - error)
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                     r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
                wd = winreg.QueryValueEx(key, "Desktop")[0]
                path = wd
                filepath = path + "\\music\\" + "{}.mp3".format(name2)
                print(Fore.GREEN + "已获取到歌曲名称: " + str(name2))
                if pre == 1:
                    # res = requests.get(
                    #     url='https://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={}pn=1&rn=30&httpsStatus=1&reqId=1e2f48f1-c8f9-11ec-9c36-53a9948184b8'.format(quote(sn)),
                    #     headers=headers
                    #     )
                    res = requests.get(
                        'http://m.kuwo.cn/newh5/singles/songinfoandlrc?musicId={}&httpsStatus=1&reqId=b25496a0-c9be-11ec-a722-4f261b808a2a'.format(
                            rid), headers=headers)
                    http_pic = json.loads(res.text).get('data').get('songinfo').get('pic')
                    https_pic = str(http_pic).replace('http://img1.kwcdn.kuwo.cn/', 'https://img3.kuwo.cn/')
                    songname = json.loads(res.text).get('data').get('songinfo').get('songName')
                    artist = json.loads(res.text).get('data').get('songinfo').get('artist')
                    # print('ok')
                    os.system(
                        'start https://gk.lps-mc.xyz?play={}?name={}?artist={}?img={}'.format(
                            songurl, str(songname).replace(' ', '').replace('?', '？'), str(artist).replace(' ', '-').replace('，', '-').replace('&', ''), https_pic))
                    # print(songurl, str(songname).replace(' ', '-'), str(artist).replace(' ', '-').replace('，', '-').replace('&', '-'), https_pic)
                    print(Fore.GREEN + '已打开预览链接')
                    print(Fore.GREEN + '按g进行下载(按q退出):', end='')
                    sbsbsb = input('')
                    if sbsbsb == 'q':
                        err = 0
                        ss
                    elif sbsbsb == 'g':
                        print("正在下载音乐至%s" % filepath)
                        rp = requests.get(url=songurl)
                        # print(songurl)

                        if not os.path.exists(path + "\\music\\"):
                            os.mkdir(path + "\\music")

                        if os.path.exists(filepath):
                            print(Fore.YELLOW + Back.BLACK + "文件存在,已覆盖")
                            with open(filepath, 'wb') as f:
                                f.write(rp.content)
                        else:
                            with open(filepath, 'wb') as f:
                                f.write(rp.content)
                        print(Fore.GREEN + Back.BLACK + "下载成功,已存储到{}".format(filepath))
                        os.startfile(filepath)
                        print(Fore.GREEN + Back.BLACK + "正在打开下载的音乐...")
                else:
                    print("正在下载音乐至%s" % filepath)
                    rp = requests.get(url=songurl)
                    # print(songurl)

                    if not os.path.exists(path + "\\music\\"):
                        os.mkdir(path + "\\music")

                    if os.path.exists(filepath):
                        print(Fore.YELLOW + Back.BLACK + "文件存在,已覆盖")
                        with open(filepath, 'wb') as f:
                            f.write(rp.content)
                    else:
                        with open(filepath, 'wb') as f:
                            f.write(rp.content)
                    print(Fore.GREEN + Back.BLACK + "下载成功,已存储到{}".format(filepath))
                    os.startfile(filepath)
                    print(Fore.GREEN + Back.BLACK + "正在打开下载的音乐...")

            except Exception as ex:
                try:
                    err += 1
                    if err == 0:
                        pass
                    else:
                        if ex == "name 'ss' is not defined":
                            pass
                        else:
                            if str(
                                    ex) == "name 'rid10' is not defined" or "name 'rid9' is not defined" or "name 'rid8' is not defined" or "name 'rid7' is not defined" or "name 'rid6' is not defined" or "name 'rid5' is not defined" or "name 'rid4' is not defined" or "name 'rid3' is not defined" or "name 'rid2' is not defined":

                                print(Fore.RED + "你的歌曲名或序号有误，请检查你的歌曲名或序号")
                                print(ex)
                            else:
                                if ex == "name 'ss' is not defined":
                                    pass
                                else:
                                    print('阿欧!出错了,你可将错误信息反馈: ', end='')
                                    print(Fore.YELLOW + ex)
                                    if a == 1:
                                        print(Fore.RED + "你的歌曲名或序号有误，请检查你的歌曲名或序号")
                except:
                    if str(
                            ex) == "name 'rid10' is not defined" or "name 'rid9' is not defined" or "name 'rid8' is not defined" or "name 'rid7' is not defined" or "name 'rid6' is not defined" or "name 'rid5' is not defined" or "name 'rid4' is not defined" or "name 'rid3' is not defined" or "name 'rid2' is not defined":
                        if ex == "name 'ss' is not defined":
                            pass
                        else:
                            print(Fore.RED + "你的歌曲名或序号有误，请检查你的歌曲名或序号")
                            print(ex)
                    else:
                        if ex == "name 'ss' is not defined":
                            pass
                        else:
                            print('阿欧!出错了,你可将错误信息反馈: ', end='')
                            print(Fore.YELLOW + ex)
                            if a == 1:
                                print(Fore.RED + "你的歌曲名或序号有误，请检查你的歌曲名或序号")
    else:
        print(Fore.YELLOW + "你的网络未连接，请检查你的网络连接,设置好后按下回车键继续")
        input()

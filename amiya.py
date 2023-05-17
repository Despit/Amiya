# '''
# Author: Azulene
# Date: 2022-10-20 18:55:54
# LastEditors: Azulene
# LastEditTime: 2022-10-24 13:00:39
# FilePath: \undefinede:\amiya\amiya.py
# Description: :-P

# Copyright (c) 2022 by Azulene, All Rights Reserved. 
# '''
import requests
import json
import re
import os

#from bs4 import BeautifulSoup
from urllib import request

headers={"Connection":"close","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0"}
local="temp"

def MakeDir(Name_comic,Name_Subtitle,Name_title):
    if not os.path.isdir(Name_comic):
        os.makedirs(Name_comic)
    os.chdir(Name_comic)
    if not os.path.isdir("%s %s"%(Name_Subtitle,Name_title)):
        os.makedirs("%s %s"%(Name_Subtitle,Name_title))
    os.chdir("..")
pass

def CallBack(cur_down, cur_size, total_size):
    progress = 100 * cur_down * cur_size / total_size
    if progress > 100:
        print("\r >>%s %d%%" %(local,progress))
pass

def Download(Id_comic,Id_episode,Name_comic,Name_Subtitle,Name_title):
    global page,local,count
    MakeDir(Name_comic,Name_Subtitle,Name_title)
    url_comic="https://terra-historicus.hypergryph.com/api/comic/"+Id_comic+"/episode/"+Id_episode+"/page?pageNum=%d"
    url_page=requests.get(url_comic%page)
    while(url_page.status_code == 200):
        url_page=url_page.json()
        url_pic=url_page["data"]["url"]
        PathName="./"+Name_comic+"/"+Name_Subtitle+" "+Name_title+"/img"+"%d"%count+".jpg"
        local=PathName
        if not os.path.isfile(PathName):
            request.urlretrieve(url=url_pic,filename=PathName,reporthook=CallBack)
        else:
            print("%s 已存在"%PathName)
        page+=1
        count+=1
        url_page=requests.get(url_comic%page)
pass
#https://terra-historicus.hypergryph.com/comic/9382/episode/3195
if __name__ == "__main__":
    print("address?")
    address=input()+" "
    Id_comic="".join(re.findall(r"comic/(.+?)/",address))
    info=requests.get(url="https://terra-historicus.hypergryph.com/api/comic/"+Id_comic,headers=headers)
    FileName_comic=info.json()["data"]["title"]
    Index_episode=info.json()["data"]["episodes"]
    count=1
    for Seq_episode in range(len(Index_episode)):
        page=1
        count=1
        Download(Id_comic,Index_episode[len(Index_episode)-Seq_episode-1]["cid"],FileName_comic,Index_episode[len(Index_episode)-Seq_episode-1]["shortTitle"],Index_episode[len(Index_episode)-Seq_episode-1]["title"])
    print("下载完成")
pass 
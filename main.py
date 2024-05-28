# -*- coding: utf-8 -*-
import platform
import sys
import os
import requests
import json

from utils import system

def start_environment():
    os_name = platform.system()
    os_version = platform.release()
    url = 'https://cloud.lxweb.cn/f/JogGFk/1.json'
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        software = data.get('software')
        announcement = data.get('announcement')
        version = data.get('version')
        print("欢迎您使用"+software+"脚本"+"\t 版本:"+version+"\n公告:"+announcement+"\n操作系统:"+os_name+"\t"+os_version)
        pd = input("是否同意运行此脚本，误操作造成的系统错误概不负责 (true/false) \n")
        if pd == "true":
            return True
        else:
            False
    else:
        network_choose = input('脚本加载失败，请检查您的网络环境，如果您的网络环境正常可以选择跳过(y/n)' )
        if network_choose == "y":
            return True
        else:
            return False    


def choose():
    os.system("clear")
    print("(1 系统工具\n"+
        "(2 磁盘工具\n" +
        "(3 数据库工具\n" +
        "(4 web工具\n"
    )
    chooses = input("输入数字选择工具：\n")
    # 调用相应的函数
    if chooses == "1":
        #这里是个测试
        print("=================系统状况=================");
        print("CPU占用："+system.get_cpu_usage())
        print("内存占用："+system.get_memory_usage())
        value1,value2,value3 = system.get_disk_usage()
        print("磁盘占用："+value1+"+\t+",value2+"\t"+value3)
    elif chooses == "2":
        case2()
    elif chooses == "3":
        print("111")
    elif chooses == "4":
        case4()
    else:
        print("输入错误")

if __name__ == "__main__":
    if start_environment():
        choose()



        



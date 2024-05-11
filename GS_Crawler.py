from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import requests
from urllib.parse import urlparse
import pandas as pd
import numpy as np
import time
import hashlib


def zidonghua(value, i):
    # value为生成的语音文本，i为生成的语音文件的名称

    # 执行JavaScript代码来获取Shadow DOM中的textarea元素
    element = driver.execute_script('return document.querySelector("body > gradio-app").shadowRoot.querySelector("#component-11 > label > textarea")')
    element.clear()  # 清空文本框内容
    element.send_keys(value)  # 替换为你想要输入的文本

    # 执行 JavaScript 代码来获取 Shadow DOM 中的按钮元素
    button_element = driver.execute_script('return document.querySelector("body > gradio-app").shadowRoot.querySelector("#component-13")')

    # 点击按钮元素
    button_element.click()
    
    # 等待语音合成的时间 可根据文本的长度来调整
    time.sleep(12)
    # 获取音频文件的URL 使用 JavaScript 路径查找 Shadow DOM 中的 <audio> 元素
    audio_element = driver.execute_script('return document.querySelector("body > gradio-app").shadowRoot.querySelector("#component-14 > audio")')

    # 获取 src 属性值
    src_value = audio_element.get_attribute('src')
    print(src_value)

    # 发送 GET 请求下载音频文件
    url = src_value
    response = requests.get(url)

    if response.status_code == 200:
        # 指定本地文件名
        base_path = r"E:\vedio_generated\\"
        file_name = base_path + str(i) + ".wav"  # 拼接文件名

        # 将文件内容写入到本地文件中
        with open(file_name, 'wb') as file:
            file.write(response.content)
            
        print("音频文件已成功下载并保存为", file_name)
    else:
        print("无法下载音频文件，状态码:", response.status_code)


if __name__=="__main__":
    
    # 启动浏览器
    driver = webdriver.Chrome()

    # 打开网页
    driver.get('http://your_web_address/')  # 替换为本地部署接口的网页地址
    time.sleep(60) # 等待网页加载完成 上传参考音和参考音对应的文本

    input_file=r"./千秋诗颂_zh.txt"  # 输入文件路径
    with open(input_file, 'r') as file:
        lines = file.readlines()

    name_list = []
    i = 1
    for line in lines:
        print(line, end=" ") 
        zidonghua(line, i)
        i += 1




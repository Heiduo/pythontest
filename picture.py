'''
@Description: 
@Version: 2.0
@Autor: Heiduo
@Date: 2020-05-13 16:09:27
@LastEditors: Seven
@LastEditTime: 2020-05-13 16:33:49
@Contact: heiduox@163.com
'''


"""
@author: nsf
@contact: 121752308@qq.com
@time: 2020/4/23 17:03
@file: main.py
@desc:
"""
import json
import os
import timeit
from datetime import datetime

import requests

# 查找的关键字
key = 'girl'
# 要下载的页数
no = 1
# 要下载的图片质量
level = 'regular'
# 下载的文件保存目录
file_path = '.\img_download'
# 图片保存格式
img_format = 'jpg'
# 请求延时
time_delay = 60


def download_img(img_url, file_path):
    try:
        req = requests.get(url=img_url, timeout=time_delay)
    except Exception:
        print('请求错误请重试')
    with open(file_path, 'wb') as f:
        f.write(req.content)


if __name__ == '__main__':
    time_today = datetime.now()
    ymd = time_today.strftime('%Y-%m-%d')
    my_dir = f'{file_path}\{ymd}'
    if not os.path.exists(my_dir):
        os.makedirs(my_dir)
    start = timeit.default_timer()
    url = f'https://unsplash.com/napi/search/photos?query={key}&xp=&per_page=20&page='
    i = 1
    html_data = json.loads(requests.get(f'{url}{i}').text)
    total_pages = html_data['total_pages']
    no = no if no < total_pages else total_pages
    while i < no:
        try:
            html_data = json.loads(requests.get(f'{url}{str(i)}', timeout=time_delay).text)
        except Exception:
            print('请求错误请重试')
            continue
        img_url_l = [i['urls'][level] for i in html_data['results']]
        j = 0
        for img_url in img_url_l:
            img_url = img_url[:-26]
            download_img(img_url, f'{my_dir}\{i}{j}.{img_format}')
            j += 1
        print(f'爬取第{i}页完成')
        i += 1
    elapsed = (timeit.default_timer() - start)
    print(f'完成数据爬取，耗时{elapsed}s')
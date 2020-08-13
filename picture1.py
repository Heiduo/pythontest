'''
@Description: 
@Version: 2.0
@Autor: Heiduo
@Date: 2020-05-13 16:35:58
@LastEditTime: 2020-05-15 16:58:51
@Contact: heiduox@163.com
'''
import os
import timeit
import requests
from datetime import datetime
from lxml import etree
import time
from jsontest import JsonConf

# 请求链接示例 
# https://wallhaven.cc/search?q=anime&categories=110&purity=100&sorting=favorites&order=desc

# 查找关键字
key = "anime"
# 排序方式 (relevance,radam,date_added, views, favorites, toplist, toplist-beta  (后两个包含日期参数，topRange=3d,3M，1y )
sorting = "favorites"
# 图片质量
purity = 100
# 下载页数
numbers = 2
# 大图前缀
pre = "wallhaven"
# 下载文件保存目录
img_path = "./wallheaven_download"
# 下载文件的原请求位置存储文件 避免重复下载
img_list = "donwload_list.json"
# 图片格式
img_format = "jpg"
# 请求延时
time_delay = 60

def download_img(img_url,file_path,reload = False):
    try:
        req = requests.get(url=img_url,timeout = time_delay)
    except Exception as err:
        print(f"{img_url} 图片下载失败")
        print(repr(err))
        if not reload:
            time.sleep(2)
            print(f"{img_url} 重新下载")
            return download_img(img_url,file_path,True)
        return False
    else:
        with open(file_path,"wb") as f:
            f.write(req.content)
            print(f'{img_url} 图片下载成功')
            req.close()
            time.sleep(1)
            return True


if __name__ == "__main__":
    time_today = datetime.now()
    ymd = time_today.strftime("%Y-%m-%d")
    my_dir = f"{img_path}/{ymd}"
    if not os.path.exists(my_dir):
        os.makedirs(my_dir)
    
    # 加载已经下载过的图片链接
    download_list = []
    download_dict = JsonConf.load(f"{img_path}/{img_list}")
    
    if key in download_dict:
        download_list = download_dict[key]
    
    start = timeit.default_timer()
    url = f"https://wallhaven.cc/search?q={key}&categories=110&purity={purity}&sorting={sorting}&order=desc&page="
    # 当前页数
    i = 1
    # 图片编号
    j = 0
    files = os.listdir(my_dir)
    if len(files) > 0:
        new_files = [int(name[:-4]) for name in files]
        j = max(new_files) + 1
    file_list = [j]
    
    while i < numbers:
        # 当前页面开始爬取
        page_start = timeit.default_timer()

        html_data = etree.HTML(requests.get(f'{url}{i}').text)
        result = html_data.xpath('//a[@class = \'preview\']/@href')
        print(result)

        for img_large_url in result:
            if img_large_url in download_list:
                print('图片已存在！略过')
                continue
            img_html_data = etree.HTML(requests.get(img_large_url).text)
            img_large_result = img_html_data.xpath('//img[@id = "wallpaper"]/@src')
            if len(img_large_result)>0:
                if download_img(img_large_result[0],f'{my_dir}\{j}.{img_format}'):
                    j += 1
                    download_list.append(img_large_url)
                    download_dict[key] = download_list
                    JsonConf.set(download_dict,f"{img_path}\{img_list}")
                    
        file_list.append(j-file_list[len(file_list)-1])
        page_expand = timeit.default_timer() - page_start
        print(f'第{i}页耗时{page_expand} s, 共下载{file_list[i]} 张图')
        i += 1
    
    endTime = timeit.default_timer() - start
    total_download = 0
    for x in file_list:
        total_download += x
    print(f'下载完成，此次共耗时{endTime} s, 共下载{total_download} 张图')
    


'''
@Description: json 测试
@Version: 2.0
@Autor: Heiduo
@Date: 2020-05-15 14:21:08
@LastEditTime: 2020-05-15 16:17:09
@Contact: heiduox@163.com
'''
import os
import json

# 存储文件路径
file_path = '.\wallheaven_downlod'

class JsonConf:
    @staticmethod
    def store(data,path):
        with open (path,'w') as json_file:
            json.dump(data,json_file)
    
    @staticmethod
    def load(path):
        if not os.path.exists(file_path):
            os.mkdir(file_path)
        os.chdir(file_path)
        if not os.path.exists(path):
            with open(path,'w') as json_file:
                data = {}
                
        else: 
            with open(path,'r') as json_file:
                try:
                    data = json.load(json_file)
                except Exception as err:
                    print(repr(err))
                    data = {}
        return data

    @staticmethod
    def set(data_dict,path):
        json_obj = JsonConf.load(path)
        for key in data_dict:
            json_obj[key] = data_dict[key]
        JsonConf.store(json_obj,path)

if __name__ == "__main__":
    img_list = []
    for i in range(12):
        img_list.append(i)

    data = {"test":"gadsdga"}
    #data['anime_list'] = img_list
    #data.setdefault("anime_list",img_list)
    JsonConf.set(data,"config1.json")
    #print(data)
    #obj = JsonConf.load("config1.json")
    #print(obj)

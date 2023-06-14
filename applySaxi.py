import numpy as np
import pandas as pd
import json
import os
import matplotlib.pyplot as plt
import math

# 需要处理文件名
fileName = "minicom_141.txt"

file_path = "saxi"
row_length = 1000
column_length = 1

# 存储文件路径
def load(path):
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    # os.chdir(file_path)
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

def set(data_dict,path):
    json_obj = load(path)
    # for key in data_dict:
        # json_obj[key] = data_dict[key]
    json_obj = data_dict
    store(json_obj,path)

def store(data,path):
    with open (path,'w') as json_file:
        json.dump(data,json_file)

def loadData(fileName):   
    trainingData=[]
    with open(file_path+'/'+fileName,'r') as txtData:
        lines=txtData.readlines()
        for line in lines:
            lineData=line.split(']=')    #去除空白和逗号“,”
            lineData2 = []
            if (len(lineData) == 2):
                lineData2.append(lineData[1])
                # if(lineData[1].strip()!=""):
                    # for i in range(int(len(line)/2)):
                        # lineData2.append(line[i*2:i*2+2])
                    # print(line[i*2:i*2+2])
                # lineData2 = line.strip().split(' ')

            for dataOrigin in lineData2:
                trainingData.append(int(dataOrigin,16))   #训练数据集
    return trainingData

data = loadData(fileName)
file_path_2 = fileName.split(".")[0]
data1 = []
for i in range(int(len(data)/3)):
    data2 = ((data[i*3]&0xff)<<16) + ((data[i*3 + 1]&0xff)<<8) + (data[i*3+2]&0xff)
    # data2 = 256*256*data[i*3] + (256*data[i*3 + 1]) + (data[i*3+2])
    if data2>=128*256*256:
        data2 = data2 - 256*256*256
    print()
    data1.append(data2)
    
set(data1,file_path +"\\" + file_path_2 + "_trans" +".txt")

### 画图
length = math.ceil(len(data1)/row_length)
# length = math.ceil(len(data1)/row_length)
row_count = math.ceil(length/column_length)

plt.title("Line chart", fontsize=16)     # 标题，字体大小
plt.xlabel("X", fontsize=12)         # X轴标签，字体大小
plt.ylabel("Y", fontsize=12)   # Y轴标签，字体大小
plt.tick_params(axis='both', labelsize=9)  # 设置刻度标记大小，哪个轴，标签字体大小
for i in range(length):
    write_data = data1[i * row_length: (i+1)*row_length]
    x_values = range(len(write_data))    # x值
    y_values = write_data  # Y值
    plt.subplot(row_count, column_length, i+1)  # 画图 x,y,线宽
    plt.plot(x_values, y_values, linewidth=1)  # 画图 x,y,线宽

plt.show()    # 画图
# set(data,file_path + "data.txt")
# set(data1,file_path + "data1.txt")
# print(data)

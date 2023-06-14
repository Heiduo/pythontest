import os
import re

file_path_all = 'D:\Dowload\BaiduNetdiskDownload\sh'
common_length_all = 3

def renameNum(file_path,common_length):
    if os.path.isdir(file_path) :
        # print("dir")
        common_pre_name = ''
        for file in os.listdir(file_path):
            if len(common_pre_name)==0:
                common_pre_name = file
            else:
                for i in range(len(common_pre_name)):
                    if(common_pre_name[i] == file[i]):
                        continue
                    else:
                        common_pre_name = common_pre_name[0:i]
                        break
            print('common_name: ' + common_pre_name)
        pre_len = len(common_pre_name)
        for file in os.listdir(file_path):
            print(file)
            num = re.findall("\d+",file[pre_len:])
            # print(num)
            if len(num) > 0 and len(num[0])<common_length:
                # print(num[0])
                did = common_length - len(num[0])
                tianchong = ""
                for i in range(did):
                    tianchong = tianchong+"0"
                # print(tianchong+num[0])
                new_name = file.replace(common_pre_name+num[0],common_pre_name+tianchong+num[0])
                print(new_name)
                old_file = os.path.join(file_path,file)
                new_file = os.path.join(file_path,new_name)
                os.rename(old_file,new_file)
    else :
        print("file")

if __name__ == "__main__":
    renameNum(file_path_all,common_length_all)
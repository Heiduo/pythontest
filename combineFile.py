import os
import rename
file_path_all = 'D:\Dowload\BaiduNetdiskDownload\sh'
file_name_all='*.ts'
new_name_all='big.ts'

def osCombine(file_path,file_name = '*.ts',new_name='new.ts'):
    file_name_path = file_path+'\\'+file_name
    file_new_path = file_path+'\\'+new_name
    print(os.system('copy /b '+file_name_path+' ' + file_new_path))

if __name__ == '__main__':
    osCombine(file_path_all,file_name_all,new_name_all)
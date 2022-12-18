import combineFile
import rename

file_path_all = 'D:\Dowload\BaiduNetdiskDownload\sh'
file_name_all='*.ts'
new_name_all='big.ts'
common_length_all = 3
if __name__ == '__main__':
    rename.renameNum(file_path_all,common_length_all)
    combineFile.osCombine(file_path_all,file_name_all,new_name_all)

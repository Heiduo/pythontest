error = {
    'signal of pulse data is bad!':'脉搏波信号质量差，请重新测量!',
    'internal error!':'内部错误，请重新测量!',
    'watch is unwarable!':'设备未佩戴！',
    'Unexpected blood pressure, try again!':'异常血压值，请重新测量！',
    'signal processing exception!':'信号处理异常，请重新测量'
}
#临时用于算法返回中文错误提示，后续优化下，返回不同语种错误
def get_error_descripe(code,language='zh'):
    if code in error.keys():
        return error[code]
    else:
        return '未知错误'

# print(get_error_descripe('1001'))
# print(get_error_descripe('1002'))

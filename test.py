print(int(4.5))
print(int(4.4))

import ctypes

so = ctypes.cdll.LoadLibrary   
lib = so("./libpycall.so")

lib.foo(1, 3)  
print ('***finish***') 

print('display()')  
# lib.display()  

print('display(100)')  
# lib.display_int(ctypes.c_int(100))
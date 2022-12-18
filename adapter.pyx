# distutils: language = c++

from cpycall cimport TestLib

# Create a Cython extension type which holds a C++ instance
# as an attribute and create a bunch of forwarding methods
# Python extension type.
cdef class PyMyDemo:
    cdef TestLib c_mydemo  # Hold a C++ instance which we're wrapping

    def sayHello(self ):
        self.c_mydemo.display() 
    def sayHello(self, a):
        self.c_mydemo.display(a)
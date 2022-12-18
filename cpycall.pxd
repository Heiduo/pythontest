cdef extern from "display.cpp"
    pass
# Decalre the class with cdef
cdef extern from "display.h" namespace "display":
    cdef cppclass TestLib:
        void display()
        void display(int)

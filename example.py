#!/usr/bin/env python

from cffi import FFI
import numpy as np

# Array data for a 4x3 RGB (black) image.
dtype = [("r", np.uint8), ("g", np.uint8), ("b", np.uint8)]
array = np.zeros((4,3), dtype=dtype)

# declare data & function for cffi 
ffi = FFI()
data = ffi.cast("unsigned char*", array.__array_interface__["data"][0])
length = ffi.cast("unsigned int", array.size)
ffi.cdef("void greenify(unsigned char* data, unsigned int length);")

# open the C lib and call a C function
libgreen = ffi.dlopen("./libgreen.so")
libgreen.greenify(data, length)

# the array has been modified.
print array

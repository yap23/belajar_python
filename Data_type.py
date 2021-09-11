# a = 10, adalah variabel dengan nilai 10

#tipe data : angka satuan yang gak ada komanya (integer)
data_integer = 11
print("data:", data_integer)
print("data:", data_integer, "Type:", type(data_integer))

#tipe data: angka dengan koma (float)
data_float = 1.5
print("data:", data_float)
print("data:", data_float, "Type:", type(data_float))

#tipe data: kumpulan karakter (string)
data_string = "ucup"
print("data:", data_string)
print("data:", data_string, "Type:", type(data_string))

#tipe data: biner (boolean)
data_bool = True
print("data:", data_bool)
print("data:", data_bool, "Type:", type(data_bool))

## Tipe data khusus

#bilangan kompleks
data_complex = complex(5,6)
print("data:", data_complex)
print("data:", data_complex, "Type:", type(data_complex))

#tipe data dari bahasa C
from ctypes import c_double

data_c_double = c_double(10.5)
print("data:", data_c_double)
print("data:", data_c_double, "Type:", type(data_c_double))
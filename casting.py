#Belajar Casting
#Merubah dari satu tipe ke tipe lain

print("========Integer==========")
data_int = 9;
print("data =", data_int, "type =", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) #akan false jika intger 0
print("data =", data_float, "type =", type(data_float))
print("data =", data_str, "type =", type(data_str))
print("data =", data_bool, "type =", type(data_bool))

## FLOAT
print("========Float==========")
data_float = 9.8;
print("data =", data_float, "type =", type(data_float))

data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float) #akan false jika intger 0
print("data =", data_int, "type =", type(data_int))
print("data =", data_str, "type =", type(data_str))
print("data =", data_bool, "type =", type(data_bool))

## BOOLEAN
print("========Boolean==========")
data_bool = False;
print("data =", data_bool, "type =", type(data_bool))

data_int = int(data_bool)
data_str = str(data_bool)
data_float = float(data_bool)
print("data =", data_int, "type =", type(data_int))
print("data =", data_str, "type =", type(data_str))
print("data =", data_float, "type =", type(data_float))

## String
print("========String==========")
data_str = "10";
print("data =", data_str, "type =", type(data_str))

data_int = int(data_str)
data_bool = bool(data_str) #false jika sting kosong
data_float = float(data_str)
print("data =", data_int, "type =", type(data_int))
print("data =", data_bool, "type =", type(data_bool))
print("data =", data_float, "type =", type(data_float))

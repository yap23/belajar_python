#Input data user

#data yang dimasukan pasti string
data = input("masukan data: ")
print("data = ",data,",type = ",type(data))

# #jika ingin mengambil int, maka:
angka = float(input("masukan angka: "))
angka = int(input("masukan angka: "))
print("data = ", angka,",type =", type(angka))

#Bagaimana dengan boolean
biner = bool(int(input("masukan nilai boolean: ")))
print("data = ", biner,",type =", type(biner))
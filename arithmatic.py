#Operasi aritmatika

a = 10
b = 3

#Operasi tambah
hasil = a+b
print(a,'+',b,'=',hasil)

#Operasi pengurangan
hasil = a-b
print(a,'-',b,'=',hasil)

#Operasi perkalian
hasil = a*b
print(a,'*',b,'=',hasil)

#Operasi pembagian
hasil = a/b
print(a,'/',b,'=',hasil)

#Operasi eksponen (pangkat) **
hasil = a**b
print(a,'**',b,'=',hasil)

#Operasi modulus (sisa pembagian) %
hasil = a%b
print(a,'%',b,'=',hasil)

#Operasi floor divison //
hasil = a//b
print(a,'//',b,'=',hasil)


#Prioritas operasi
'''
    1. ()
    2. exponen **
    3. perkalian dan teman2 * / ** % //
    4. Pertambahan dan pengurangan + -
'''
x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x ,'**' ,y ,'*' ,z ,'+' ,x ,'/' ,y ,'-' ,y ,'%' ,z ,'//' ,x, '=', hasil)
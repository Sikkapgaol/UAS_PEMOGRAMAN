# Nama  : Sikkap Lumban Gaol
# Nim   : 180402162
# Ujian Akhir Semester Pemrograman Komputer TE-D

# section 1 : Membuat dengan hasil print ('str', 'float', 'int')
x = "apel"
y = 2.6
z = 8
print(x,y,z)
print(x)
print(y)
print(z)

# section 2 : Menentukan tipe dari hasil print
a = 3.5, 2.3
b = 13 , 77
c = "kedokteran", "gigi" 
d = 2.25
e = 9
f = "USU"
g = 11.1
h =92.59
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))

# section 3 : Python Number

x,y = 4, 8
y,x = 6, 20
print(x,y)
print(y,x)

# section 4 : Memotong huruf pada kalimat berdasarkan peletakkan huruf
kevin = "Mahasiswa USU"
print(kevin)
print(kevin[::-3])
print(kevin[3])
print(kevin[3:])
print(kevin.upper())
print(kevin.lower())
print(kevin.replace("S","m"))

# section 5 : Pyhton List
list1 = [2,3,5,7,11,13,17]
print(list1)
data1 = list1[0]
print(data1)
data2 = list1[-2]
print(data2)

# section 6 : Kombinasi python list
ikan = ['lele', 'Nila', 'Patin']
print(ikan)
print(type (ikan))
ikan=''.join(hewan)
print(ikan)
print(type (ikan))

# section 7 : Menunjukkan angka berapa kali muncul
Nilai = [1,3,4,2,3,7,6,4,3,5,5,1,2,6,7,5,2]
print(Nilai.count(1))
print(Nilai.count(2))
print(Nilai.count(3))
print(Nilai.count(4))
print(Nilai.count(5))
print(Nilai.count(6))
print(Nilai.count(7))

# section 8 : Membuat kalimat menjadi Besar ataupun Kecil
Jurusan = "Teknik Elektro"
Jurusan2 = "TEKNIK ELEKTRO"
print(Jurusan.lower()) # teknik elektro
print(Jurusan.upper()) # TEKNIK ELEKTRO
print(Jurusan.capitalize()) # Teknik elektro
print(Jurusan2.capitalize()) # Teknik elektro
print(Jurusan2.lower()) # teknik elektro
print(Jurusan2.upper()) # TEKNIK ELEKTRO

# section 9 :
Hari = ['senin', 'selasa', 'rabu', 'kamis']
Jadwal = map(str.upper, Hari)
print(list(Jadwal))

# section 10 : Dictionary
Biodata = {"ID":404,
           "Nama": "Martinus",
           "Pekerjaan":"Mahasiswa",
           "Nim":"190402153"
           "Universitas Sumatera Utara"
            }
print(Biodata)
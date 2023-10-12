# isim = input("İsminiz Nedir? ")
# print("merhaba "+ isim)

# alıştırma
# isim = input("isminiz nedir? ")
# yemek = input("Ne yemeyi seversiniz? ")
# print(isim + " " + yemek + " " + "yemeyi sever.")

# değişken türü değiştirme
isim = "Ali"
yas = 31
#print(isim +" "+ str(yas) +" "+ "yaşında.")

# aşağıdakileri neyin başına getirirsen değişkenin türü değişir.
int() #integer
float() #float
str() #string
bool() #boolean

# matematik işlemleri
x = 9
y = 5

#print(x + y)
#print(x - y)
#print(x * y)
#print(x / y)

#print(x // y) # tam sayı şeklinde böler, virgülsüz
#(x % y) # kalanı verir

# alıştırma
# sayi1 = input("ilk sayıyı girin ")
# sayi2 = input("ikinci sayıyı girin ")

# print(int(sayi1) + int(sayi2))

# matematik fonksiyonları
round(9.8) # sayıyı tam sayıya yuvarlar
abs(6) # sayının mutlak değerini yani sıfıra olan uzaklığını bulur
import math # kütüphane eklenir
#print(math.sqrt(9)) # karekökünü bulma
min(2,3,4,5,7,7,8,9) # içinde bulunan sayıların en küçüğünü bulur
max(2,3,4,5,6,7,8,9) # içinde bulunan sayıların en büyüğünü bulur

# string kuralları
isim = "samur" # eğer kelimenin içinde bir harfi tırnak içine alınacaksa, stirng çift tırnakla yazılmışsa tek tırnakla harfi tırnak içine alırız, veya tam tersi
mektup = """merhaba begüm
umarım iyisindir"""
#print(mektup)
#print(isim[3]) # değişkenin içindeki sıralama sıfırdan başlar, ilk harf sıfırdır, köşeli parantezle belirtilir
#print(isim[1:3]) # eğer birden fazla harf belirteceksek iki nokta kullanırız soluna başlangıç sağına bitiş sırasını yazarız
print(len(isim)) # değişkenin harf sayısını gösterir
print(isim.title) # metnin ilk harfini büyütür
print(isim.upper()) # değişkenin bütün harflerini büyütür
print(isim.lower()) # metnin bütün harflerini küçültür
print(isim.find("u")) # değişkenin içinde aradığımız harfin kaçıncı satırda olduğunu bulur
print(isim.replace("samur", "sanane"))








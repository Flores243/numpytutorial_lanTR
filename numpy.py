# numpy ile py liste/dizileri arasındaki farklar
# np daha hızlı, np tek veri tipi ama py birden fazla
# 1- numpy giriş
import numpy as np

dizi = np.array(["sercan", "ömer", "fatma", "ayşe"])
print(type(dizi))

sifirlar = np.zeros((5,3))
print(sifirlar)

birler = np.ones((5,3))
print(birler)

deger = np.full((4,4),round(25.6), dtype=int) # round en yakın tam sayıya  yuvarlama
print(deger)

for i in range(0,30,3): #(start, stop,range)
    print(i, end=" ")
print()
print("*"*25)

aralik = np.arange(0,30,3)
print(aralik)

# belli aralıklar içinde sayıları diziye ondalıklı azaltarak eklemek
aralik2 = np.linspace(0.5354,10, 20) # (start, stop, eleman sayısı)
aralik2 = np.round(aralik2, 2)
print(aralik2)

# 2- rastgele sayı işlemleri



rastgele = np.random.randint(0,2, (3,4)) # random tam sayı üretme fonk. random.randint
print(rastgele)
print(rastgele[0])

for i in range(3):
    print(rastgele[i][3] * (2 ** 0) + 
          rastgele[i][2] * (2 ** 1) + 
          rastgele[i][1] * (2 ** 2) + 
          rastgele[i][0] * (2 ** 3), end=" ")

print()
print(rastgele.size)


# 3- numpy özellikleri


dizi = np.random.randint(20, size=9) # size eleman sayısı belirtiyor. 8-1
print(dizi)
print(dizi.ndim, dizi.size, dizi.dtype) # .ndim boyut 
dizi2 = np.array([[5, 2, 8, 5, 8],
       [2, 4, 8, 4, 3],
       [9, 0, 2, 0, 2]])
print(dizi2.dtype)



dizi3 = np.random.randint(1,15, size=16)
print(dizi3)
siniflama = dizi3.reshape((4,4)) 
print("Dizi:\n",siniflama)
print("Satır Sıralı Dizi:\n",np.sort(siniflama, axis=0))
# axis= None: diziyi tek satırda küçükten büyüğe sıralar
# axis= 0: Sütun değerleri küçükten büyüğe sıralar
# axis= 1: Satır değerleri küçükten büyüğe sıralar

# 4- Dizileri Birleştirme İşlemleri

array1 = np.array([10,20,30,40])
array2 = np.array([-20,-50,0,60])
birlestir = np.concatenate([array1, array2]) # önerilen birleştirme
np.array(birlestir)
print(birlestir.reshape((2,4)))

dizi10 = np.array([1, 2, 3])
dizi20 = np.array([4, 5, 6])

birlesmis_dizi = np.hstack((dizi10, dizi20)) # tek satırda birleştiriyor çok önerilmez

print(birlesmis_dizi)


dizi = np.random.randint(10,20, size=12)
# np.split(dizi, sayısal): verilen diziyi "sayısal" değere göre parçalar
# sayısal kısım birden fazlaysa toplamına göre parçalar.
satir1, satir2, satir3, satir4 = np.split(dizi, 4)
print(satir1, satir2, satir3, satir4)
# satır1 herbiri bir satırdan ve bir elemandan olşan diziye böldük
satir1 = np.split(satir1, 3)
# satır1 i sütun olarak artan sıralama yaptık
print(np.sort(satir1))


# dizi içinde 30 dan büyük ve 70 küçük sayıları gösteren python numpy programı yazınız

soru = np.array([15, 25, 35, 45, 55, 65, 75, 85])

for k in soru:
    if k > 30 and k < 70:
        print(k)
    else:
        continue

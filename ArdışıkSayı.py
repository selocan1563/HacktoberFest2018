# Her Türlü Ardışık Dizinin Terimleri Toplamını Veren Program

a = input("İlk Terim:") ##ilk terimi alır
b = input("Son Terim:") ##ikinci terimi alır
c = input("Ardışık İki Terimin Farkı:") ##farklarını alır

sonuç = (((int(a) + int(b)) * (int(b) - int(a) + int(c))) / (2 * int(c)))

print("Sonuç:", int(sonuç)) #sonucu ekrana çıktı verir

# Her Türlü Ardışık Dizinin Terimleri Toplamını Veren Program

a = input("İlk Terim:")
b = input("Son Terim:")
c = input("Artış Miktarı:")

sonuç = (((int(b) + int(a)) * (int(b) - int(a) + int(c))) / (2 * int(c)))

print("Sonuç:", int(sonuç))

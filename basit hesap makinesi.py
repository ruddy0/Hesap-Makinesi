giriş ="""
(1) Toplama
(2) Çıkarma
(3) Çarpma
(4) Bölme
(5) Karekök Hesapla
(6) Karesini Hesapla
"""
print(giriş)

a = 1

while a == 1:
    npmk = input("Yapmak istediğiniz işlemin numarasını girin (Çıkmak için q): ")

    if npmk == "q":
        print("Programdan çıkılıyor...")
        a = 0

    elif npmk == "1":
        s1 = int(input("Toplamak istediğiniz ilk sayıyı girin: "))
        s2 = int(input("Toplamak istediğiniz ikinci sayıyı girin: "))
        print("%s + %s = %s" %(s1, s2, s1+s2))

    elif npmk == "2":
        s1 = int(input("Çıkarma işlemini yapmak istediğiniz ilk sayıyı girin: "))
        s2 = int(input("Çıkarma işlemini yapmak istediğiniz ikinci sayıyı girin: "))
        print("%s - %s = %s" %(s1, s2, s1-s2))

    elif npmk == "3":
        s1 = int(input("Çarpmak istediğiniz ilk sayı: "))
        s2 = int(input("Çarpmak istediğiniz ikinci sayı: "))
        print("%s * %s = %s" %(s1, s2, s1*s2))


    elif npmk == "4":
        s1 = int(input("Bölmek istediğiniz ilk sayı: "))
        s2 = int(input("Bölmek istediğiniz ikinci sayı: "))
        print("%s / %s = %s" %(s1, s2, s1/s2))

    elif npmk == "5":
        s1 = int(input("Karekökünü almak istediğiniz değeri girin: "))
        print("%s sayısının karekökü = %s" %(s1, s1**0.5))

    elif npmk == "6":
        s1 = int(input("Karesini hesaplamak istediğiniz değeri girin: : "))
        print("%s sayısının karesi = %s" %(s1, s1**2))

    else:
        print("Yanlış giriş!")
        print("Aşağıdaki seçeneklerden birini giriniz:", giriş) 

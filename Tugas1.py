print ("---Selamat datang di aplikasi FAKE£opeMeter---")
print ("============================================")

import random

loop = True
while loop:

    tahun = 0
    bulan = 0
    tgl = 0
    confirm = "z"

    cowok = input("\nMasukkan nama anda : ")

    while tahun <=0 or tahun >= 2020 :
        tahun = int(input("masukkan tahun lahir anda : "))

    while bulan <=0 or bulan >= 13 :
        bulan = int(input("masukkan bulan lahir anda ( 1-12 ) : \n1. Januari\n2. Februari\n3. Maret\n4. April\n5. Mei\n6. Juni\n7. Juli\n8. Agustus\n9. September\n10. Oktober\n11. November\n12. Desember\ninput : "))

#    while bulan != 1 and bulan != 2 and bulan != 3 and bulan != 4 and bulan != 5 and bulan != 6 and bulan != 7 and bulan != 8 and bulan != 9 and bulan != 10 and bulan != 11 and bulan != 12 :
#        bulan = int(input("masukkan bulan lahir anda ( 1-12 ) : \n1. Januari\n2. Februari\n3. Maret\n4. April\n5. Mei\n6. Juni\n7. Juli\n8. Agustus\n9. September\n10. Oktober\n11. November\n12. Desember\ninput : "))

    if bulan == 2 :

        if tahun %4 == 0 :
            while tgl <=0 or tgl >=30 :
                tgl = int(input("masukkan tanggal lahir anda ( 1-29 ) : "))


        else :
            while tgl <=0 or tgl >=29 :
                tgl = int(input("masukkan tanggal lahir anda ( 1-28 ) : "))


    elif bulan == 1 or bulan == 3 or bulan == 5 or bulan == 7 or bulan == 8 or bulan == 10 or bulan == 12 :
        while tgl <=0 or tgl >=32 :
            tgl = int(input("masukkan tanggal lahir anda ( 1-31 ) : "))


    else :
        while tgl <=0 or tgl >=31 :
            tgl = int(input("masukkan tanggal lahir anda ( 1-30 ) : "))

    total1 = (tahun - (bulan + tgl))

    while confirm != "ya" and confirm != "tidak" :
        confirm = input ("apakah data yang anda masukkan sudah benar? ya/tidak: ")

    if confirm == "ya":
        loop = False

print("\n")
print ("============================================")
loop = True
while loop:

    tahun = 0
    bulan = 0
    tgl = 0
    confirm = "z"

    cewek = input("\nMasukkan nama pasangan anda : ")

    while tahun <=0 or tahun >= 2020 :
        tahun = int(input("masukkan tahun lahir anda : "))

    while bulan <=0 or bulan >= 13 :
        bulan = int(input("masukkan bulan lahir anda ( 1-12 ) : \n1. Januari\n2. Februari\n3. Maret\n4. April\n5. Mei\n6. Juni\n7. Juli\n8. Agustus\n9. September\n10. Oktober\n11. November\n12. Desember\ninput : "))

    if bulan == 2 :

        if tahun %4 == 0 :
            while tgl <=0 or tgl >=30 :
                tgl = int(input("masukkan tanggal lahir anda ( 1-29 ) : "))


        else :
            while tgl <=0 or tgl >=29 :
                tgl = int(input("masukkan tanggal lahir anda ( 1-28 ) : "))


    elif bulan == 1 or bulan == 3 or bulan == 5 or bulan == 7 or bulan == 8 or bulan == 10 or bulan == 12 :
        while tgl <=0 or tgl >=32 :
            tgl = int(input("masukkan tanggal lahir anda ( 1-31 ) : "))


    else :
        while tgl <=0 or tgl >=31 :
            tgl = int(input("masukkan tanggal lahir anda ( 1-30 ) : "))

    total2 = (tahun - (bulan + tgl))

    while confirm != "ya" and confirm != "tidak" :
        confirm = input ("apakah data yang anda masukkan sudah benar? ya/tidak: ")

    if confirm == "ya":
        loop = False


print("\n")
print ("============================================")
print("\n")

#print(total1)
#print(total2)
a = max(total1, total2)
b = min(total1, total2)

poin = a-b

#print(poin)

if poin >= 8 :
    macth = random.randrange(76, 100)
elif poin >= 3 :
    macth = random.randrange(36, 75)
else :
    macth = random.randrange(0, 35)

print ("\n presentase hubungan", cowok, "dan", cewek, "adalah", macth, "%\n")
if macth > 80 :
    print ("---kalian adalah jodoh---")
elif macth > 60 :
    print ("---kalian sangan cocok---")
elif macth > 40 :
    print ("---pertimbangkan hubungan kalian kedepanya---")
elif macth > 20 :
    print ("---hhmmm sangat disayangkang---")
else :
    print ("---maaf jika hasil ini menyakiti anda---")

print ("============================================")

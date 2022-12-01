
def penjumlahan(per,ked):
    jumlah=per+ked
    return jumlah
def pengurangan(per,ked):
    kurang=per-ked
    return kurang
def perkalian(per,ked):
    kali=per*ked
    return kali
def pembagian(per,ked):
    bagi=per//ked
    return bagi
print("Operasi Matematika")
print("1. Jumlah [+]")
print("2. Kurang [-]")
print("3. Kali   [*]")
print("4. Bagi   [/]")
print("==================")
pilih=input("pilih oprasi(1/2/3/4): ")
per=int(input("Masukkan bilangan pertama :"))
ked=int(input("Masukkan bilangan kedua :"))
if pilih == "1":
    print("Hasil operasi dari",per,"+",ked,"=",penjumlahan(per,ked))
elif pilih == "2":
    print("Hasil operasi dari",per,"-",ked,"=",pengurangan(per,ked))
elif pilih == "3":
    print("Hasil operasi dari",per,"*",ked,"=",perkalian(per,ked))
elif pilih == "4":
    print("Hasil operasi dari",per,"//",ked,"=",pembagian(per,ked))

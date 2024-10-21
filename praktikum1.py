# Inisialisasi nilai variabel MAX dengan minus tak hingga
MAX = float('-inf')
while True:
        # Input N dari pengguna
        N = int(input("Masukkan Nilai N: "))
        
        # Cek apakah nilai yang dimasukkan adalah angka 0, jika iya, maka perulangan akan berakhir dan akan menunjukan angka terbesar yang sudah dimasukkan
        if N == 0:
            break
        
        # Cek apakah bilangan yang diinputkan lebih besar dari MAX 
        if N > MAX:
        # Jika kondisi diatas sudah terpenuhi (N > MAX)
            MAX = N
print("Bilangan Terbesar yang dimasukan adalah: ", MAX)

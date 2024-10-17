MAX = float('-inf')
while True:
        # Input N dari pengguna
        N = int(input("Masukkan Nilai N: "))
        
        # Cek apakah pengguna ingin keluar
        if N == 0:
            print("Proses selesai.")
            break
        
        # Cek apakah bilangan yang diinputkan lebih besar dari MAX 
        if N > MAX:
            MAX = N
print(f"Bilangan Terbesar yang dimasukan adalah: {MAX}")
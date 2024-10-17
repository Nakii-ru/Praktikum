# Praktikum - Tipe Data, Variable, dan Operator

Nama  : RIDHO FHADLY HAMZAH

NIM   : 32410486

KELAS : TI.24.A5

Mata Kuliah : Bahasa Pemrograman

## Mencari Bilangan Terbesar dari Beberapa Bilangan yang Diinput
Program ini dibuat untuk menentukan bilangan Terbesar dari serangkaian Nilai bilangan yang diinput tanpa henti hingga user memasukkan nilai "0".
Program ini menggunakan loop `while` dan kondisi `if` untuk memperbarui nilai terbesar yang diinputkan.

## Flowchart Program
![foto](https://github.com/Nakii-ru/foto/blob/main/Screenshot%202024-10-17%20220558.png?raw=true)

## Penjelasan Kode Program
```python
# Inisialisasi MAX dengan negatif tak hingga
MAX = float('-inf')
while True:

        # Input Nilai Oleh Pengguna
        N = int(input("Masukkan Nilai N: "))

        # Jika Nilai 0 diinputkan maka loop akan berakhir
        if N == 0:
            print("Proses selesai.")
            break

        # Cek apakah bilangan yang diinputkan lebih besar dari MAX 
        if N > MAX:

        # Update MAX bila N Lebih besar dari MAX
        MAX = N

# OUTPUT Nilai N terbesar
print(f"Bilangan Terbesar yang dimasukan adalah: {MAX}")

```

## Contoh Hasil Eksekusi Program
![foto]()

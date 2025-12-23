import time
import random
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(10000)

# =====================================
# Fungsi Membuat Data Pengeluaran Mahasiswa
# =====================================
def generate_pengeluaran(size):
    """
    Menghasilkan list pengeluaran harian mahasiswa secara acak (Rp 5.000 - 50.000)
    """
    return [random.randint(5000, 50000) for _ in range(size)]

# =====================================
# Algoritma Iteratif
# =====================================
def total_pengeluaran_iteratif(data):
    total = 0
    for pengeluaran in data:
        total += pengeluaran
    return total

# =====================================
# Algoritma Rekursif
# =====================================
def total_pengeluaran_rekursif(data, index=0):
    if index == len(data):
        return 0
    return data[index] + total_pengeluaran_rekursif(data, index + 1)

# =====================================
# Fungsi Mengukur Waktu Eksekusi
# =====================================
def hitung_waktu(data):
    # Iteratif
    start = time.perf_counter()
    total_iteratif = total_pengeluaran_iteratif(data)
    end = time.perf_counter()
    waktu_iteratif = end - start

    # Rekursif
    start = time.perf_counter()
    total_rekursif = total_pengeluaran_rekursif(data)
    end = time.perf_counter()
    waktu_rekursif = end - start

    return total_iteratif, total_rekursif, waktu_iteratif, waktu_rekursif

# =====================================
# Program Utama
# =====================================
def main():
    print("ANALISIS KOMPLEKSITAS ALGORITMA")
    print("Studi Kasus: Total Pengeluaran Bulanan Mahasiswa\n")

    ukuran_data = [10, 50, 100, 500, 1000, 2000]
    waktu_iteratif_list = []
    waktu_rekursif_list = []

    for size in ukuran_data:
        data = generate_pengeluaran(size)

        total_i, total_r, waktu_i, waktu_r = hitung_waktu(data)

        waktu_iteratif_list.append(waktu_i)
        waktu_rekursif_list.append(waktu_r)

        print(f"Jumlah Data Pengeluaran : {size}")
        print(f"Total Iteratif  : Rp {total_i}")
        print(f"Total Rekursif  : Rp {total_r}")
        print(f"Waktu Iteratif  : {waktu_i:.6f} detik")
        print(f"Waktu Rekursif  : {waktu_r:.6f} detik\n")

    # =====================================
    # Grafik Perbandingan Waktu Eksekusi
    # =====================================
    plt.figure(figsize=(10, 6))
    plt.plot(ukuran_data, waktu_iteratif_list, marker='o', linestyle='-', color='blue', label='Iteratif')
    plt.plot(ukuran_data, waktu_rekursif_list, marker='x', linestyle='--', color='red', label='Rekursif')

    plt.xlabel("Jumlah Data Pengeluaran")
    plt.ylabel("Waktu Eksekusi (detik)")
    plt.title("Perbandingan Waktu Eksekusi Algoritma Iteratif vs Rekursif")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()

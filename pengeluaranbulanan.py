# app.py
import streamlit as st
import random
import time
import matplotlib.pyplot as plt
from prettytable import PrettyTable
import sys

sys.setrecursionlimit(5000)

# =====================================
# Fungsi Membuat Data Pengeluaran Mahasiswa
# =====================================
def generate_pengeluaran(size, seed=42):
    """
    Menghasilkan list pengeluaran harian mahasiswa secara acak (Rp 5.000 - 50.000)
    Dengan seed agar dataset konsisten
    """
    random.seed(seed)
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
    start = time.perf_counter()
    total_i = total_pengeluaran_iteratif(data)
    end = time.perf_counter()
    waktu_i = end - start

    start = time.perf_counter()
    total_r = total_pengeluaran_rekursif(data)
    end = time.perf_counter()
    waktu_r = end - start

    return total_i, total_r, waktu_i, waktu_r


def print_table(n_values, recursive_times, iterative_times, total_recursive, total_iterative):
    table = PrettyTable()
    table.field_names = ["Jumlah Data", "Total Iteratif", "Total Rekursif", "Waktu Iteratif (s)", "Waktu Rekursif (s)"]
    for i in range(len(n_values)):
        table.add_row([n_values[i], f"Rp {total_iterative[i]}", f"Rp {total_recursive[i]}", f"{iterative_times[i]:.6f}", f"{recursive_times[i]:.6f}"])
    st.text(str(table))

def plot_graph(n_values, recursive_times, iterative_times):
    plt.figure(figsize=(10,6))
    plt.plot(n_values, iterative_times, marker='o', linestyle='-', color='blue', label='Iteratif')
    plt.plot(n_values, recursive_times, marker='x', linestyle='--', color='red', label='Rekursif')
    plt.xlabel("Jumlah Data Pengeluaran")
    plt.ylabel("Waktu Eksekusi (detik)")
    plt.title("Perbandingan Waktu Eksekusi Algoritma Iteratif vs Rekursif")
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)

st.title("Analisis Kompleksitas Algoritma")
st.subheader("Studi Kasus: Total Pengeluaran Bulanan Mahasiswa")
st.write("Kelas: IF-12-02")
st.write("Nama Anggota: Tri Setyono Martyantoro (103112400279) | Rifa Cahya Ariby (103112400268)")

st.write("---")
st.write("Pilih ukuran dataset untuk diuji:")
dataset_sizes = st.multiselect("Jumlah Data Pengeluaran", [10, 50, 100, 500, 1000, 2000], default=[10, 50, 100, 500, 1000, 2000])

if st.button("Mulai Analisis") and dataset_sizes:
    n_values = []
    total_iterative = []
    total_recursive = []
    iterative_times = []
    recursive_times = []

    for size in dataset_sizes:
        data = generate_pengeluaran(size)
        total_i, total_r, waktu_i, waktu_r = hitung_waktu(data)

        n_values.append(size)
        total_iterative.append(total_i)
        total_recursive.append(total_r)
        iterative_times.append(waktu_i)
        recursive_times.append(waktu_r)

    # Tampilkan tabel
    st.write("### Tabel Hasil Analisis")
    print_table(n_values, recursive_times, iterative_times, total_recursive, total_iterative)

    # Tampilkan grafik
    st.write("### Grafik Perbandingan Waktu Eksekusi")
    plot_graph(n_values, recursive_times, iterative_times)


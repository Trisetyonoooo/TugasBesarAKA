# app.py
import streamlit as st
import random
import time
import matplotlib.pyplot as plt
from prettytable import PrettyTable
import sys

# Menambah batas rekursi agar aman untuk dataset agak besar
sys.setrecursionlimit(5000)

# =====================================
# Fungsi Membuat Data Pengeluaran Mahasiswa
# =====================================
def generate_pengeluaran(size, seed=42):
    """Menghasilkan list pengeluaran harian mahasiswa secara acak (Rp 5.000 - 50.000)"""
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

# =====================================
# Fungsi Tampilkan Tabel
# =====================================
def print_table(n_values, recursive_times, iterative_times, total_recursive, total_iterative):
    table = PrettyTable()
    table.field_names = ["Jumlah Data", "Total Iteratif", "Total Rekursif", "Waktu Iteratif (s)", "Waktu Rekursif (s)"]
    for i in range(len(n_values)):
        table.add_row([n_values[i], f"Rp {total_iterative[i]:,}", f"Rp {total_recursive[i]:,}", f"{iterative_times[i]:.6f}", f"{recursive_times[i]:.6f}"])
    st.text(str(table))

# =====================================
# Fungsi Tampilkan Grafik
# =====================================
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

# =====================================
# Streamlit App
# =====================================
st.set_page_config(page_title="Analisis Algoritma Pengeluaran", layout="wide")

st.title("📊 Analisis Kompleksitas Algoritma")
st.subheader("Studi Kasus: Total Pengeluaran Bulanan Mahasiswa")
st.write("**Kelas:** IF-12-02")
st.write("**Nama Anggota:** Tri Setyono Martyantoro (103112400279) | Rifa Cahya Ariby (103112400268)")

# Sidebar untuk kontrol input
st.sidebar.header("Pengaturan Dataset")
dataset_sizes = st.sidebar.multiselect(
    "Pilih jumlah data pengeluaran yang ingin diuji:",
    [10, 50, 100, 500, 1000, 2000],
    default=[10, 50, 100, 500, 1000, 2000]
)

st.sidebar.markdown("---")
st.sidebar.write("Klik tombol di bawah untuk memulai analisis")
start_button = st.sidebar.button("Mulai Analisis")

# =====================================
# Jalankan Analisis
# =====================================
if start_button and dataset_sizes:
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

    # Bagi layout menjadi 2 kolom
    col1, col2 = st.columns(2)

    with col1:
        st.write("### 📋 Tabel Hasil Analisis")
        print_table(n_values, recursive_times, iterative_times, total_recursive, total_iterative)

    with col2:
        st.write("### 📈 Grafik Perbandingan Waktu Eksekusi")
        plot_graph(n_values, recursive_times, iterative_times)

    # Tampilkan ringkasan metrik
    st.write("---")
    st.subheader("Ringkasan Performa")
    for i, size in enumerate(n_values):
        col_i, col_r = st.columns(2)
        col_i.metric(f"Iteratif - Data {size}", f"Rp {total_iterative[i]:,}", f"{iterative_times[i]:.6f} detik")
        col_r.metric(f"Rekursif - Data {size}", f"Rp {total_recursive[i]:,}", f"{recursive_times[i]:.6f} detik")


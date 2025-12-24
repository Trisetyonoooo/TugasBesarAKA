import streamlit as st
import random
import time
import matplotlib.pyplot as plt
import pandas as pd
import sys

sys.setrecursionlimit(5000)

def generate_pengeluaran(size, seed=42):
    random.seed(seed)
    return [random.randint(5000, 50000) for _ in range(size)]

def total_pengeluaran_iteratif(data):
    total = 0
    for pengeluaran in data:
        total += pengeluaran
    return total

def total_pengeluaran_rekursif(data, index=0):
    if index == len(data):
        return 0
    return data[index] + total_pengeluaran_rekursif(data, index + 1)

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

def show_table(n_values, total_iterative, total_recursive, iterative_times, recursive_times):
    df = pd.DataFrame({
        "Jumlah Data": n_values,
        "Total Iteratif (Rp)": [f"{x:,}" for x in total_iterative],
        "Total Rekursif (Rp)": [f"{x:,}" for x in total_recursive],
        "Waktu Iteratif (s)": [f"{x:.6f}" for x in iterative_times],
        "Waktu Rekursif (s)": [f"{x:.6f}" for x in recursive_times],
    })
    st.dataframe(df, use_container_width=True)

def plot_graph(n_values, iterative_times, recursive_times):
    plt.figure(figsize=(10,6))
    plt.plot(n_values, iterative_times, marker='o', linestyle='-', color='blue', label='Iteratif')
    plt.plot(n_values, recursive_times, marker='x', linestyle='--', color='red', label='Rekursif')
    plt.xlabel("Jumlah Data Pengeluaran")
    plt.ylabel("Waktu Eksekusi (detik)")
    plt.title("Perbandingan Waktu Eksekusi Algoritma Iteratif vs Rekursif")
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)


st.set_page_config(page_title="Analisis Algoritma Pengeluaran", layout="wide")

st.title("Analisis Kompleksitas Algoritma")
st.subheader("Studi Kasus: Total Pengeluaran Bulanan Mahasiswa")
st.write("**Kelas:** IF-12-02")
st.write("**Nama Anggota:** Tri Setyono Martyantoro (103112400279) | Rifa Cahya Ariby (103112400268)")

st.sidebar.header("Pengaturan Dataset")
dataset_sizes = st.sidebar.multiselect(
    "Pilih jumlah data pengeluaran:",
    [10, 50, 100, 500, 1000, 2000],
    default=[10, 50, 100, 500, 1000, 2000]
)
start_button = st.sidebar.button("Mulai Analisis")

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

    col1, col2 = st.columns(2)
    with col1:
        st.write("### 📋 Tabel Hasil Analisis")
        show_table(n_values, total_iterative, total_recursive, iterative_times, recursive_times)

    with col2:
        st.write("### 📈 Grafik Perbandingan Waktu Eksekusi")
        plot_graph(n_values, iterative_times, recursive_times)



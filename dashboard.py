import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the bike sharing dataset
# Replace 'bike_data.csv' with the actual file path of your dataset
bike_data = pd.read_csv('hour.csv')

# Set the title of the dashboard
st.title('Dashboard Eksplorasi Bike Sharing Dataset')

# Sidebar section for filtering data
st.sidebar.header("Informasi")
st.sidebar.markdown(
    "Dashboard sebagai media untuk menyampaikan hasil analisis data secara interaktif. Pada proyek ini, Anda dapat membuat dashboard dengan streamlit mirip seperti materi latihan sebelumnya. Selain itu, pastikan bahwa dashboard Anda buat dapat berjalan dengan lancar di local."
)
st.sidebar.markdown(
    "[Github Repository](https://github.com/aryankargwal/capbot2.0)"
)    
    
# Display basic dataset info
st.write("### Bike Sharing Dataset Overview")
st.write(bike_data.head())
st.write("Number of rows:", len(bike_data))

# Summary statistics
st.write('### Summary Statistics')
st.write(bike_data.describe())

cola, colb = st.columns(2)

with cola:
    # Memeriksa korelasi data numerik
    st.write('#### Data Correlation')
    correlation_matrix = bike_data[['temp', 'hum', 'windspeed', 'cnt']].corr()
    fig, ax = plt.subplots(figsize=(10, 6))
    g = sns.heatmap(correlation_matrix, annot=True, linewidth=.5)
    g.set(title='Correlation Matrix')
    st.pyplot(fig)

with colb:
    # Histogram of bike counts
    st.write("#### Histogram Jumlah Peminjaman Sepeda")
    fig, ax = plt.subplots(figsize=(10, 6))
    g = sns.histplot(data=bike_data, x='cnt', bins=30, kde=True)
    g.set(title='Distribution of Bike Counts')
    g.set(xlabel='Count')
    g.set(ylabel='Frequency')
    st.pyplot(fig)

# Data Visualization
st.write("### Data Visualization")

# Gambarkan perbandingan jumlah pemakaian sepeda setiap bulannya dalam 2 tahun terakhir
st.write("#### Perbandingan jumlah pemakaian sepeda setiap bulannya dalam 2 tahun terakhir")
fig, ax = plt.subplots(figsize=(10, 6))
g = sns.lineplot(data=bike_data, x='mnth', y='cnt', hue='yr', style='yr', markers=True, dashes=False)
plt.title('Perbandingan Jumlah Penggunaan Sepeda Setiap Bulannya dalan 2 Tahun Terakhir')
g.set(xlabel='Bulan')
g.set(ylabel='Jumlah')
st.pyplot(fig)

# Gambarkan perbandingan jumlah pemakaian sepeda setiap bulannya dalam 2 tahun terakhir antara pengguna casual dan registered
st.write("#### Perbandingan jumlah pemakaian sepeda setiap bulannya dalam 2 tahun terakhir antara pengguna casual dan registered")
fig, ax = plt.subplots(2, 1, figsize=(10, 6))
g1 = sns.lineplot(data=bike_data, x='mnth', y='casual', hue='yr', style='yr', markers=True, dashes=False, ax=ax[0])
g1.set(title='Perbandingan Jumlah Peminjaman Sepeda Untuk Pengguna Casual dan Registered Dalam 2 Tahun Terakhir')
g1.set(xticklabels=[])
g1.set(xlabel=None)

g2 = sns.lineplot(data=bike_data, x='mnth', y='registered', hue='yr', style='yr', markers=True, dashes=False, ax=ax[1], legend=False)
g2.set(xlabel="Month")
#f.tight_layout()
st.pyplot(fig)

col1, col2 = st.columns(2)
with col1:
    # Mengetahui Jumlah Peminjaman Sepeda Berdasarkan Musim
    st.write("#### Jumlah Peminjaman Sepeda Berdasarkan Musim")
    fig, ax = plt.subplots(figsize=(10, 6))
    g = sns.barplot(data=bike_data, x='season', y='cnt')
    g.set(title='Jumlah Peminjaman Sepeda Berdasarkan Musim')
    g.set(xlabel='Musim')
    g.set(ylabel='Jumlah')
    st.pyplot(fig)

with col2:
    # Mengetahui Jumlah Peminjaman Sepeda Berdasarkan Kondisi Cuaca
    st.write("#### Jumlah Peminjaman Sepeda Berdasarkan Kondisi Cuaca")
    fig, ax = plt.subplots(figsize=(10, 6))
    g = sns.barplot(data=bike_data, x='weathersit', y='cnt')
    g.set(title='Jumlah Peminjaman Sepeda Berdasarkan Kondisi Cuaca')
    g.set(xlabel='Kondisi Cuaca')
    g.set(ylabel='Jumlah')
    st.pyplot(fig)

with col1:
    # Mengetahui Jumlah Peminjaman Sepeda Berdasarkan Hari Kerja
    st.write("#### Jumlah Peminjaman Sepeda Berdasarkan Hari Kerja")
    fig, ax = plt.subplots(figsize=(10, 6))
    g = sns.barplot(data=bike_data, x='workingday', y='cnt')
    g.set(title='Jumlah Peminjaman Sepeda Berdasarkan Kondisi Hari Kerja')
    g.set(xlabel='Hari Kerja')
    g.set(ylabel='Jumlah')
    st.pyplot(fig)

with col2:
    # Mengetahui Jumlah Peminjaman Sepeda Berdasarkan Hari Kerja
    st.write("#### Jumlah Peminjaman Sepeda Berdasarkan Hari")
    fig, ax = plt.subplots(figsize=(10, 6))
    g = sns.barplot(data=bike_data, x='weekday', y='cnt')
    g.set(title='Jumlah Peminjaman Sepeda Berdasarkan Hari')
    g.set(xlabel='Hari')
    g.set(ylabel='Jumlah')
    st.pyplot(fig)
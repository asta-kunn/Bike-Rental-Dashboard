import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from io import StringIO

def download_csv(url):
    response = requests.get(url, verify=False)
    csv_data = StringIO(response.text)
    return csv_data

# URL data
link = lambda x : f"https://raw.githubusercontent.com/myudak/Bike-Exploratory-Data-Analysis/main/data/{x}.csv"

# Mengunduh dan membaca data harian
day_data = pd.read_csv(download_csv(link("day")))

# Mengunduh dan membaca data per jam
hour_data = pd.read_csv(download_csv(link("hour")))

# Set up page layout
st.set_page_config(layout="wide")

# Sidebar
st.sidebar.title('Dashboard Analisis Penyewaan Sepeda')
analysis_choice = st.sidebar.radio('Pilih Analisis:', ('Pengaruh Cuaca', 'Pola Penyewaan'))

# Main content
st.title('Analisis Penyewaan Sepeda')

if analysis_choice == 'Pengaruh Cuaca':
    st.header('Pengaruh Kondisi Cuaca terhadap Penyewaan Sepeda')
    st.write("Cuaca yang lebih cerah cenderung menghasilkan jumlah penyewaan yang lebih tinggi. Ini penting bagi penyedia layanan sepeda untuk mengoptimalkan operasi mereka, seperti menyiapkan lebih banyak sepeda pada hari-hari dengan cuaca cerah.")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='weathersit', y='cnt', data=day_data, ax=ax, palette='coolwarm')
    plt.xticks(ticks=[0, 1, 2], labels=['Cerah', 'Berawan', 'Hujan/Salju'], rotation=45)
    ax.set_xlabel('Kondisi Cuaca')
    ax.set_ylabel('Jumlah Penyewaan')
    ax.set_title('Pengaruh Kondisi Cuaca terhadap Penyewaan Sepeda')
    st.pyplot(fig)

elif analysis_choice == 'Pola Penyewaan':
    st.header('Penyewaan Sepeda per Hari dalam Seminggu')
    st.write("Ada perbedaan pola penyewaan sepeda selama hari dalam seminggu, dengan akhir pekan menunjukkan peningkatan penyewaan dibandingkan hari kerja. Ini dapat membantu dalam perencanaan stok dan pelayanan lebih lanjut.")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='weekday', y='cnt', data=day_data, ax=ax, palette='viridis')
    plt.xticks(ticks=[0, 1, 2, 3, 4, 5, 6], labels=['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu'], rotation=45)
    ax.set_xlabel('Hari dalam Seminggu')
    ax.set_ylabel('Jumlah Penyewaan')
    ax.set_title('Penyewaan Sepeda per Hari dalam Seminggu')
    st.pyplot(fig)

st.sidebar.subheader('Tentang')
st.sidebar.info('Ini adalah dashboard interaktif untuk menganalisis data penyewaan sepeda.')
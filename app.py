#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import requests

API_KEY = '59ea17fdfdb23d1baa3dc61e90050861'

# Data provinsi dan kota
provinces_data = {
    "Aceh": ["Banda Aceh", "Lhokseumawe"],
    "Sumatera Utara": ["Medan", "Binjai"],
    "Sumatera Barat": ["Padang", "Bukittinggi"],
    "Riau": ["Pekanbaru", "Dumai"],
    "Jambi": ["Jambi", "Sungai Penuh"],
    "Sumatera Selatan": ["Palembang", "Lubuklinggau"],
    "Bengkulu": ["Bengkulu"],
    "Lampung": ["Bandar Lampung", "Metro"],
    "Bangka Belitung": ["Pangkalpinang"],
    "Kepulauan Riau": ["Tanjung Pinang", "Batam"],
    "DKI Jakarta": ["Jakarta"],
    "Jawa Barat": ["Bandung", "Bekasi", "Bogor"],
    "Jawa Tengah": ["Semarang", "Surakarta", "Magelang"],
    "DI Yogyakarta": ["Yogyakarta"],
    "Jawa Timur": ["Surabaya", "Malang", "Kediri"],
    "Banten": ["Serang", "Tangerang"],
    "Bali": ["Denpasar"],
    "Nusa Tenggara Barat": ["Mataram", "Bima"],
    "Nusa Tenggara Timur": ["Kupang", "Ende"],
    "Kalimantan Barat": ["Pontianak", "Singkawang"],
    "Kalimantan Tengah": ["Palangka Raya"],
    "Kalimantan Selatan": ["Banjarmasin", "Banjarbaru"],
    "Kalimantan Timur": ["Samarinda", "Balikpapan"],
    "Kalimantan Utara": ["Tarakan"],
    "Sulawesi Utara": ["Manado", "Bitung"],
    "Sulawesi Tengah": ["Palu"],
    "Sulawesi Selatan": ["Makassar", "Parepare"],
    "Sulawesi Tenggara": ["Kendari", "Baubau"],
    "Gorontalo": ["Gorontalo"],
    "Sulawesi Barat": ["Mamuju"],
    "Maluku": ["Ambon"],
    "Maluku Utara": ["Ternate"],
    "Papua": ["Jayapura"],
    "Papua Barat": ["Manokwari"],
}

st.set_page_config(page_title="Cek Cuaca Indonesia", page_icon="☀️")

st.title("☁️ Aplikasi Cuaca Provinsi Indonesia")

# Pilih provinsi
province = st.selectbox("Pilih provinsi", list(provinces_data.keys()))

# Tampilkan kota setelah provinsi dipilih
if province:
    city = st.selectbox("Pilih kota", provinces_data[province])

    # Tampilkan data cuaca ketika tombol diklik
    if st.button("Lihat Cuaca"):
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
        res = requests.get(url).json()

        if "main" in res:
            lat, lon = res["coord"]["lat"], res["coord"]["lon"]
            uv_url = f"http://api.openweathermap.org/data/2.5/uvi?lat={lat}&lon={lon}&appid={API_KEY}"
            uv_res = requests.get(uv_url).json()

            weather = {
                "Suhu": f"{res['main']['temp']}°C",
                "Cuaca": res['weather'][0]['description'].title(),
                "Kelembapan": f"{res['main']['humidity']}%",
                "Angin": f"{res['wind']['speed']} m/s arah {res['wind'].get('deg', 0)}°",
                "UV Index": uv_res.get("value", "N/A")
            }

            st.subheader(f"🌤 Cuaca di {res['name']}")
            st.image(f"http://openweathermap.org/img/wn/{res['weather'][0]['icon']}@2x.png")
            for key, val in weather.items():
                st.write(f"**{key}**: {val}")
        else:
            st.error("Kota tidak ditemukan 😢")


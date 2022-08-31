from datetime import date, datetime
from itertools import groupby
from re import X
from tkinter import Y, font
from turtle import color
import pandas as pd
import datetime
import matplotlib.pyplot as plt


df = pd.read_csv("transaksi_retail_dqlab_v2.csv", delimiter="\t")
print(df.head(5))

# menghitung total jumlah barang yang dibeli berdasarkan produk
print(df["Jumlah"].groupby(df["Nama Produk"]).sum())

# membuat kolom baru bernama "Bulan" yang bertipe datetime dalam format "%m-%Y"
df["Bulan"] = df["Tanggal"].apply(
    lambda x : datetime.datetime.strptime(x, "%d-%m-%Y").strftime("%m-%Y")
)

print(df.groupby(["Bulan", "Nama Produk"])["Jumlah"].sum())

plt.scatter(df["Harga"], df["Jumlah"], alpha=0.2)
plt.xlabel("Harga", fontsize=11)
plt.ylabel("Jumlah", fontsize=11)
plt.tight_layout()
plt.show()



plt.figure(figsize= (8,9))
plt.hist(df["Jumlah"])
plt.grid(color="gray",linewidth=0.5)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

produk_mi = df[df["Nama Produk"] == "Mi Goreng Instant"]

# x adalah bulan transaksi
x = ["04-2020", "05-2020", "06-2020"]

# y jumlah item Mi Goreng Instant yang terjual
y = produk_mi.groupby(["Bulan","Nama Produk"])["Jumlah"].sum()

# membuat line chart menggunakan fungsi plot
plt.plot(x, y)
plt.title("Jumlah Penjualan Mie Goreng Per Bulan", pad=10, fontsize=12, color="Blue")
plt.xlabel("Bulan", fontsize=11)
plt.ylabel("Jumlah", fontsize=11)
plt.grid(color="gray", linewidth=0.5)
plt.tight_layout()
plt.show()

df["Total"] = df["Harga"] * df["Jumlah"]

print(df.groupby(["Bulan","Nama Produk"])["Total"].sum())

produk_kopi = df[df["Nama Produk"] == "Kopi Instant"]
x = ["04-2020","05-2020","06-2020"]
y = produk_kopi.groupby(["Bulan", "Nama Produk"])["Jumlah"].sum()

plt.plot(x, y)
plt.title("Jumlah Penjualan Kopi Instant Per Bulan", pad=10, fontsize=12, color="Blue")
plt.xlabel("Bulan", fontsize=11)
plt.ylabel("Jumlah", fontsize=11)
plt.grid(color="gray", linewidth=0.5)
plt.tight_layout()
plt.show()
"""
Online Shop Sales Analysis
Analisis penjualan online shop menggunakan Pandas & Matplotlib.
Repo: https://github.com/SilverSt4t/online-shop-analisis
"""
import os
import pandas as pd
import matplotlib.pyplot as plt

# Pastikan folder output ada
os.makedirs("images", exist_ok=True)

# --- 1. Load Data ---
df = pd.read_csv("data.csv")
print("=== DATA OVERVIEW ===")
print(df.head())
print(f"\nTotal baris: {len(df)}")
print(f"Kolom: {list(df.columns)}")

# --- 2. Clean / Transform ---
df['Tanggal'] = pd.to_datetime(df['Tanggal'])
df['Bulan'] = df['Tanggal'].dt.to_period('M').astype(str)

# --- 3. Analisis Tren Penjualan Bulanan ---
monthly_sales = df.groupby('Bulan')['Jumlah'].sum()
print("\n=== TREND BULANAN ===")
print(monthly_sales)

plt.figure(figsize=(8, 5))
monthly_sales.plot(kind='line', marker='o', color='#2E86AB', linewidth=2.5)
plt.title('Tren Penjualan Bulanan', fontsize=14, fontweight='bold')
plt.xlabel('Bulan')
plt.ylabel('Total Penjualan (Jumlah)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()
plt.savefig("images/tren_penjualan_bulanan.png", dpi=300)
plt.close()
print("[✓] Grafik: images/tren_penjualan_bulanan.png")

# --- 4. Produk Terlaris ---
top_products = df.groupby('Produk')['Jumlah'].sum().sort_values(ascending=False)
print("\n=== PRODUK TERLARIS ===")
print(top_products)

plt.figure(figsize=(7, 5))
colors = ['#A23B72', '#F18F01', '#C73E1D']
top_products.plot(kind='barh', color=colors)
plt.title('Top Produk Berdasarkan Total Jumlah Terjual', fontsize=14, fontweight='bold')
plt.xlabel('Total Jumlah Terjual')
plt.tight_layout()
plt.savefig("images/produk_terlaris.png", dpi=300)
plt.close()
print("[✓] Grafik: images/produk_terlaris.png")

# --- 5. Hubungan Harga vs Jumlah ---
plt.figure(figsize=(7, 5))
plt.scatter(df['Harga'], df['Jumlah'], alpha=0.7, color='#3B1F2B', edgecolors='white')
plt.title('Hubungan Harga dan Jumlah Terjual', fontsize=14, fontweight='bold')
plt.xlabel('Harga (IDR)')
plt.ylabel('Jumlah Terjual')
plt.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()
plt.savefig("images/harga_vs_jumlah.png", dpi=300)
plt.close()
print("[✓] Grafik: images/harga_vs_jumlah.png")

# --- 6. Penjualan per Wilayah ---
region_sales = df.groupby('Wilayah')['Jumlah'].sum().sort_values(ascending=False)
print("\n=== PENJUALAN PER WILAYAH ===")
print(region_sales)

plt.figure(figsize=(7, 5))
region_sales.plot(kind='bar', color=['#E63946', '#F1FAEE', '#A8DADC'])
plt.title('Penjualan per Wilayah', fontsize=14, fontweight='bold')
plt.xlabel('Wilayah')
plt.ylabel('Total Penjualan')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("images/penjualan_wilayah.png", dpi=300)
plt.close()
print("[✓] Grafik: images/penjualan_wilayah.png")

# --- 7. Insight / Rekomendasi ---
insight = """
=== INSIGHT UTAMA ===
1. Produk C adalah produk terlaris (jumlah terjual tertinggi), namun harganya paling rendah.
2. Jakarta mendominasi volume penjualan dibanding Bandung & Surabaya.
3. Harga yang lebih rendah cenderung berkorelasi dengan jumlah terjual lebih tinggi.
4. Data hanya mencakup 5 hari di Januari 2023 — disarankan menambah periode agar tren lebih kuat.
"""
print(insight)

# --- 8. Export Hasil ---
df.to_csv("hasil_analisis_penjualan.csv", index=False)
print("[✓] Data hasil: hasil_analisis_penjualan.csv")

# --- 9. Simpan Ringkasan Teks ---
with open("laporan_insight.txt", "w") as f:
    f.write("LAPORAN ANALISIS ONLINE SHOP\n")
    f.write("="*40 + "\n")
    f.write(f"Dataset: {len(df)} baris | Periode: {df['Tanggal'].min().date()} sampai {df['Tanggal'].max().date()}\n")
    f.write(f"Wilayah: {', '.join(df['Wilayah'].unique())}\n")
    f.write(f"Produk: {', '.join(df['Produk'].unique())}\n\n")
    f.write("Produkt Terlaris:\n")
    for idx, val in top_products.items():
        f.write(f"  - {idx}: {val}\n")
    f.write("\nWilayah Teratas:\n")
    for idx, val in region_sales.items():
        f.write(f"  - {idx}: {val}\n")
    f.write("\nRekomendasi:\n")
    f.write("  - Fokus stok & promo di Jakarta.\n")
    f.write("  - Evaluasi harga Produk A & B agar lebih kompetitif.\n")
    f.write("  - Perlu data lebih panjang untuk analisis musiman yang valid.\n")

print("[✓] Laporan: laporan_insight.txt")

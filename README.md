# 🛒 Online Shop Sales Analysis
---

## 📊 Dataset

File `data.csv` berisi data penjualan selama **5 hari (1–5 Jan 2023)** dengan kolom:
- `Tanggal` — tanggal transaksi
- `Produk` — nama produk (A, B, C)
- `Harga` — harga satuan (IDR)
- `Jumlah` — jumlah terjual
- `Wilayah` — lokasi (Jakarta, Bandung, Surabaya)

---

## 🚀 Cara Menjalankan

```bash
# 1. Install dependency
pip install -r requirements.txt

# 2. Jalankan analisis
python main.py
```

Output yang dihasilkan:
- `images/tren_penjualan_bulanan.png`
- `images/produk_terlaris.png`
- `images/harga_vs_jumlah.png`
- `images/penjualan_wilayah.png`
- `hasil_analisis_penjualan.csv`
- `laporan_insight.txt`

---

## 📈 Insight Utama

1. **Produk C** adalah terlaris (jumlah terjual tertinggi) meski harga paling rendah.
2. **Jakarta** mendominasi volume, tapi Surabaya memiliki total terjual tertinggi (530 vs 260 Jakarta) karena harga produk C lebih murah dan volume besar.
3. Ada korelasi negatif sederhana antara harga dan jumlah terjual.
4. **Data masih sangat kecil** (14 baris, 1 bulan). Perlu data lebih panjang untuk analisis musiman dan prediksi yang valid.

---

## 🛠 Tech Stack

- Python 3
- Pandas
- Matplotlib
- Seaborn (optional styling)

---

## 📁 Struktur Folder

```
├── data.csv
├── main.py
├── requirements.txt
├── hasil_analisis_penjualan.csv
├── laporan_insight.txt
└── images/
    ├── tren_penjualan_bulanan.png
    ├── produk_terlaris.png
    ├── harga_vs_jumlah.png
    └── penjualan_wilayah.png
```

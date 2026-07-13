# WS-13: Data Preprocessing

> **Bab 13 — Preprocessing & Persiapan Data untuk Analisis**

---

## Ringkasan Materi

### Data Refinement Pipeline

```
Raw Data → Cleaning → Transformation → Normalization → Processed Data → Analysis Ready
```

Setiap tahap memiliki tujuan berbeda. **Preprocessing bukan langkah teknis biasa** — setiap keputusan preprocessing adalah keputusan riset yang bisa mengubah kesimpulan.

### Empat Prinsip Preprocessing

| Prinsip | Deskripsi |
|---------|----------|
| **Consistency** | Metode sama untuk data yang sama |
| **Transparency** | Setiap langkah terdokumentasi |
| **Reproducibility** | Orang lain bisa mengulang dengan hasil sama |
| **Minimal Distortion** | Ubah sesedikit mungkin; jika normalisasi tidak perlu, jangan lakukan |

### Cleaning Triad

| Masalah | Strategi | Risiko |
|---------|---------|--------|
| **Missing values** | | |
| — Listwise deletion | Missing < 5%, random | Data loss |
| — Mean/median imputation | Sedikit missing, dist. normal | Mengurangi variabilitas |
| — Model-based imputation | Banyak missing, pola sistematis | Introduces dependency |
| — Flag & separate | Missing karena alasan substantif | Kompleksitas analisis |
| **Duplikat** | Identifikasi → verifikasi → hapus | False positive (data mirip ≠ duplikat) |
| **Error format** | Standardisasi tipe, encoding | Kehilangan informasi saat konversi |

### Normalisasi — Kapan & Metode Mana

| Metode | Formula | Output | Sensitif Outlier? |
|--------|---------|--------|-------------------|
| Min-max | (x-min)/(max-min) | [0, 1] | Ya |
| Z-score | (x-mean)/std | Unbounded | Lebih robust |
| Robust scaling | (x-median)/IQR | Unbounded | Paling robust |

**Kunci:** Parameter normalisasi harus dihitung dari **training set saja** — bukan seluruh data. Pelanggaran = **data leakage**.

### Data Leakage Prevention

Data leakage terjadi ketika informasi dari test set "bocor" ke preprocessing:
- Normalisasi parameter dari seluruh dataset ← **SALAH**
- Cross-validation dilakukan sebelum split ← **SALAH**
- Feature selection menggunakan label test set ← **SALAH**

### Jebakan Kognitif

1. "Preprocessing cuma teknis — tidak perlu detail" → bisa ubah kesimpulan
2. "Lebih banyak preprocessing = lebih bersih = lebih baik" → over-processing distorsi data
3. "Normalisasi selalu diperlukan" → belum tentu, tergantung metode analisis
4. "Imputation sama untuk semua situasi" → strategi harus sesuai konteks

---

## Template A.13 — Preprocessing Documentation Log

```
PREPROCESSING LOG

Dataset           : ____________________
Jumlah data awal  : ____________________

Cleaning:
| Masalah | Jumlah Kasus | Penanganan | Justifikasi |
|---------|-------------|------------|-------------|
| Missing |             |            |             |
| Duplikat|             |            |             |
| Error   |             |            |             |

Transformation:
| Transformasi | Variabel | Detail | Alasan |
|-------------|----------|--------|--------|
|             |          |        |        |

Normalization:
  Metode    : ____________________
  Alasan    : ____________________
  Parameter : (dihitung dari: training set / seluruh data)

Leakage Check:
  [ ] Parameter normalisasi dari training set saja
  [ ] Tidak ada informasi test set dalam preprocessing
  [ ] Cross-validation dilakukan setelah split

Jumlah data akhir : ____________________
Script tersedia   : [ ] Ya → path: ____ | [ ] Belum
```

---

## Latihan 1 — Cleaning Plan

Periksa dataset Anda (atau dataset contoh) dan dokumentasikan masalah yang ditemukan.

| Masalah | Jumlah Kasus | Penanganan | Justifikasi |
|---------|-------------|------------|-------------|
| Nilai ekstrem / *Outlier* (Run 5 Chrome: 2100.50 MB) | 1 dari 80 (1.25%) | *Flag & separate* (Ditandai tanpa dihapus) | Penurunan drastis ini bukan *error* format, melainkan intervensi *disk swapping* OS Windows 11. Menghapusnya akan menghilangkan bukti perilaku riil sistem. |
| *Missing values* | 0 dari 80 (0%) | Tidak ada tindakan | Seluruh eksekusi skrip otomatisasi berhasil merekam data log hingga selesai. |
| Duplikat data | 0 dari 80 (0%) | Tidak ada tindakan | Setiap iterasi (*run*) memiliki rentang nilai RAM yang unik sesuai perilaku dinamis *browser*. |

**Jumlah data sebelum cleaning:** 80
**Jumlah data setelah cleaning:** 80
**Persentase data yang hilang/berubah:** 0%

---

## Latihan 2 — Normalisasi Decision

Tentukan apakah data Anda perlu normalisasi, dan jika ya, metode apa yang tepat.

| Variabel | Range Asli | Distribusi | Outlier? | Metode Normalisasi | Alasan |
|----------|-----------|-----------|----------|-------------------|--------|
| Kapasitas RAM Terpakai | 2100.50 – 6078.18 MB | Cenderung normal dengan sedikit *skew* | Ya (Run 5) | Tidak perlu | Analisis komparasi statistik menggunakan besaran mutlak (MB), bukan melatih model algoritma. |
| | | | | | |

**Apakah normalisasi diperlukan?** [ ] Ya / [x] Tidak
**Justifikasi:**
> Pengukuran kapasitas memori menggunakan satuan mutlak (Megabytes) untuk analisis statistik deskriptif dan uji beda rata-rata (komparasi dua kelompok). Eksperimen ini tidak ditujukan untuk melatih algoritma *Machine Learning* yang sangat sensitif terhadap skala data. Menerapkan normalisasi justru akan mendistorsi makna besaran memori aslinya.

**Leakage check:**
- [x] Parameter dihitung dari training set saja *(N/A - Eksperimen komparasi non-ML)*
- [x] Normalisasi diterapkan setelah train-test split *(N/A - Tidak ada split)*

---

## Latihan 3 — Preprocessing Report

Buat ringkasan preprocessing lengkap — dokumentasi yang cukup bagi orang lain untuk mereplikasi.

PREPROCESSING SUMMARY

1. Dataset: Log Utilisasi Memori RAM Browser (Chrome vs Firefox)
2. Data awal: 80 records, 3 features (Browser, Run_ID, RAM_MB)
3. Cleaning:
   - Missing values: 0 kasus, metode: -
   - Duplikat: 0 kasus, tindakan: -
   - Error (Outlier): 1 kasus, tindakan: Ditandai (flagged) untuk analisis spesifik mengenai disk swapping OS.
4. Transformation: Data dipertahankan dalam nilai absolut (Megabytes).
5. Normalisasi: Tidak diterapkan (metode), parameter dari N/A.
6. Data akhir: 80 records, 3 features
7. Leakage check: [x] Lulus / [ ] Ada masalah

---

## Refleksi

> Apakah Anda pernah melakukan normalisasi "karena biasa dilakukan" tanpa mempertimbangkan apakah benar-benar diperlukan? Apa risiko over-preprocessing?

**Pengalaman sebelumnya:**
> Pada pengolahan data sebelumnya, langkah normalisasi seperti *Min-Max scaling* sering kali langsung diterapkan secara mekanis pada seluruh kumpulan kolom angka tanpa memahami tujuan akhirnya. 
**Risiko over-preprocessing:**
> Memaksa menghapus data pencilan atau menormalkan seluruh kolom pada eksperimen komputasi berisiko menghilangkan karakteristik murni dari objek yang diteliti. Membuang *outlier* pada kasus uji RAM ini sama saja dengan menutup mata terhadap fenomena *bottleneck* atau *disk swapping* yang secara nyata terjadi di lingkungan sistem operasi.
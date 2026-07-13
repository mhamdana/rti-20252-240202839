# Laporan Penelitian

**Judul:** Analisis Komparatif Efisiensi Alokasi Memori RAM pada Browser Chromium dan Gecko dalam Lingkungan Windows

**Peneliti:** Helmi Bahar Alim
**Program Studi:** [Isi sesuai program studi Anda]
**Semester/Tahun:** [Isi sesuai periode]
**Dosen Pembimbing:** [Isi nama dosen pembimbing jika tersedia]

---

## Abstrak

Penelitian ini mengevaluasi efisiensi alokasi memori RAM antara dua engine browser utama: **Chromium** (Google Chrome) dan **Gecko** (Mozilla Firefox) pada sistem operasi Windows. Eksperimen menggunakan otomatisasi Playwright untuk membuka 40 tab di setiap browser, menunggu stabilisasi 180 detik, lalu mengukur total penggunaan memori proses browser dengan `psutil`. Hasil nyata menunjukkan bahwa rata-rata penggunaan RAM Chromium jauh lebih tinggi dibanding Firefox pada kondisi yang sama. Laporan ini juga menjelaskan pelaksanaan eksperimen, manajemen data, integritas ilmiah, analisis kuantitatif, dan komunikasi hasil penelitian.

---

## Daftar Isi

1. Pendahuluan
2. Metodologi Penelitian
3. Etika dan Integritas Penelitian
4. Hasil Pengolahan Data dan Analisis
5. Interpretasi dan Kesimpulan
6. Komunikasi Ilmiah dan Penyajian Laporan
7. Lampiran Dokumentasi dan Artefak

---

## 1. Pendahuluan

### 1.1 Latar Belakang

Peramban web modern menjalankan banyak proses dan sering menuntut alokasi memori yang signifikan, terutama ketika membuka puluhan tab bersamaan. Dalam konteks penggunaan Windows pada perangkat dengan kapasitas RAM terbatas, perbedaan arsitektur manajemen memori antara Chromium (process-per-tab dengan fitur Memory Saver) dan Gecko (sistem multithread dengan Tab Unloading) dapat menghasilkan profil penggunaan memori yang berbeda.

### 1.2 Rumusan Masalah

Penelitian ini bertujuan menjawab:

1. Seberapa besar perbedaan penggunaan memori antara Chromium dan Gecko ketika membuka 40 tab statis secara bersamaan?
2. Browser mana yang menunjukkan efisiensi alokasi memori lebih baik pada kondisi pasif setelah stabilisasi 180 detik?
3. Bagaimana variabilitas penggunaan memori kedua browser pada pengulangan eksperimen berulang?

### 1.3 Tujuan Penelitian

Tujuan penelitian adalah:

- Mengukur secara kuantitatif penggunaan RAM oleh Chromium dan Gecko dalam skenario 40 tab pasif.
- Membandingkan efisiensi pengelolaan memori kedua browser.
- Menyusun laporan penelitian yang sistematis dan dapat dipertanggungjawabkan.

---

## 2. Metodologi Penelitian

### 2.1 Desain Eksperimen

Eksperimen menggunakan skrip Python di `04-data/uji_ram.py` dan `05-kode/uji_ram.py`.

- **Instrumen:** Playwright untuk mengotomasi pembukaan 40 URL di browser; `psutil` untuk membaca penggunaan RAM proses browser.
- **Variabel yang diukur:** total penggunaan memori proses browser (MB) setelah 180 detik stabil.
- **Pengulangan:** data utama menunjukkan 40 run untuk Chrome, 10 run untuk Chrome lanjutan, dan 40 run untuk Firefox yang diperoleh dari log `06-output/ffx2.txt`. Data ekstra di luar 40 run dibiarkan sebagai sisaan dan tidak dihitung dalam analisis akhir.
- **Kondisi pengukuran:** masing-masing browser dijalankan pada sesi baru tanpa cache lama, 40 tab dibuka secara bertahap, lalu disimpan nilai RAM setelah 180 detik.

### 2.2 Prosedur Eksperimen

Langkah utama:

1. Muat 40 URL identik dalam 40 tab browser.
2. Tunggu 180 detik agar halaman statis dan proses memori mencapai kondisi stabil.
3. Hitung total RSS memori untuk proses browser dengan `psutil`.
4. Tutup browser dan beri jeda pendinginan 60 detik.
5. Ulangi untuk total 40 run pada masing-masing browser yang dianalisis; untuk Firefox, fokus pada 40 run pertama dalam log dan abaikan nilai tambahan.

### 2.3 Sumber dan Data

- **Data mentah eksperimen:** disimpan di `06-output/Hasil_RAM_Chrome.xlsx`, `06-output/Hasil_RAM_Chrome_lanjutan.xlsx`, dan log `06-output/ffx2.txt` untuk Firefox (40 run pertama sebagai dataset utama).
- **Referensi metodologi:** proposal di `01-proposal/roposal-penelitian.md`, matriks literatur di `02-literatur/matriks-literatur.md`, dan draf manuskrip di `07-manuskrip/07-manuskrip.md`.

---

## 3. Etika dan Integritas Penelitian

### 3.1 Kejujuran Akademik

- Semua data eksperimen didokumentasikan secara rinci di folder `06-output/` dan kode eksperimen berada di `04-data/` dan `05-kode/`.
- Hasil disajikan berdasarkan angka nyata dari file output, bukan asumsi.
- Setiap keterbatasan data dan perbedaan jumlah run dicatat secara transparan.

### 3.2 Penggunaan Referensi yang Benar

- Referensi dan basis ilmiah disusun dalam `02-literatur/matriks-literatur.md` dan `02-literatur/daftar-pustaka.bib`.
- Manuskrip ilmiah `07-manuskrip/07-manuskrip.md` menyertakan struktur pendahuluan, tinjauan pustaka, metodologi, hasil, dan kesimpulan.

### 3.3 Pengelolaan Data Penelitian

- Data mentah dan output hasil dipisahkan: `04-data/` untuk skrip, `06-output/` untuk hasil eksperimen.
- Output Excel disimpan sebagai artefak hasil pengukuran.
- Skrip eksperimen tertulis ulang sehingga pengukuran dapat direplikasi.

### 3.4 Keterbukaan Proses

- Rencana dan pelaksanaan tercatat di `09-docs/`.
- Dokumentasi tahapan tersedia untuk ditinjau ulang.
- Temuan, kendala, dan keputusan metodologis dicatat untuk transparansi reproducibility.

---

## 4. Hasil Pengolahan Data dan Analisis

### 4.1 Statistik Penggunaan Memori

Dari file hasil eksperimen:

- **Chromium** (`06-output/Hasil_RAM_Chrome.xlsx`, 40 run)
  - Rata-rata: **4.818,39 MB**
  - Standar deviasi: **1.009,78 MB**
  - Rentang: **2.223,07 MB** sampai **6.078,18 MB**

- **Chromium lanjutan** (`06-output/Hasil_RAM_Chrome_lanjutan.xlsx`, 10 run)
  - Rata-rata: **5.179,78 MB**
  - Standar deviasi: **395,24 MB**
  - Rentang: **4.701,77 MB** sampai **5.923,09 MB**

- **Gecko / Firefox** (`06-output/ffx2.txt`, 40 run pertama)
  - Rata-rata: **3.009,51 MB**
  - Standar deviasi: **250,01 MB**
  - Rentang: **2.459,58 MB** sampai **3.524,30 MB**

### 4.2 Perbandingan Utama

Dari data yang tersedia, perbandingan menunjukkan bahwa:

- **Chromium** menggunakan rata-rata **sekitar 1.700 MB lebih banyak** RAM dibanding **Firefox** pada kondisi 40 tab pasif.
- Dispersi nilai Chromium lebih besar, menunjukkan variabilitas lingkungan eksekusi yang signifikan.
- Firefox menunjukkan stabilitas penggunaan memori yang relatif ketat pada 40 run pertama yang dianalisis.

### 4.3 Interpretasi Awal

- Perbedaan besar ini mendukung hipotesis bahwa arsitektur Chromium cenderung menghasilkan footprint RAM yang lebih tinggi pada skenario tab pasif skala besar.
- Firefox kemungkinan lebih efisien dalam mempertahankan total alokasi memori pada kondisi yang sama.
- Namun, perbandingan harus dikaji dengan hati-hati karena jumlah run Firefox lebih sedikit dibanding Chrome dan data tambahan Chrome menunjukkan sebaran hasil yang luas.

---

## 5. Interpretasi dan Kesimpulan

### 5.1 Temuan Utama

1. **Chromium menunjukkan penggunaan memori yang lebih tinggi** daripada Firefox dalam eksperimen 40 tab pasif.
2. **Firefox tampak lebih konsisten** pada rentang hasil yang tercatat, dengan standar deviasi yang rendah dibanding ukuran sampel terbatas.
3. **Variabilitas Chrome** menunjuk pada potensi pengaruh faktor lingkungan atau konfigurasi sistem pada performa memori.

### 5.2 Kesimpulan

Berdasarkan data eksperimen saat ini, terdapat bukti awal bahwa **Firefox lebih efisien secara penggunaan memori** daripada **Chrome** dalam skenario 40 tab pasif di Windows. Penelitian ini membuka peluang analisis lebih lanjut terhadap mekanisme memori kedua browser, khususnya dampak fitur *Memory Saver* pada Chrome dan *Tab Unloading* pada Firefox.

### 5.3 Saran Lanjutan

- Melanjutkan eksperimen dengan jumlah run Firefox setara dengan Chrome.
- Menambahkan pengukuran penggunaan memori sistem dan proses subkomponen browser untuk membedakan overhead internal.
- Menguji skenario beban dinamis (situs interaktif) untuk memperluas generalisasi hasil.

---

## 6. Komunikasi Ilmiah dan Penyajian Laporan

### 6.1 Sistematisasi Laporan

Laporan ini disusun berdasarkan struktur ilmiah: latar belakang, metodologi, hasil, analisis, dan kesimpulan. Ini memudahkan presentasi seminar dan diskusi akademis.

### 6.2 Argumentasi Logis

- Metodologi eksperimen dijelaskan secara rinci di `04-data/uji_ram.py`.
- Hasil diambil langsung dari file output Excel di `06-output/`.
- Kesimpulan dibangun atas angka nyata, bukan hanya pernyataan konseptual.

### 6.3 Kesiapan Presentasi dan Pembelaan

Dokumentasi pendukung:

- `01-proposal/roposal-penelitian.md`
- `02-literatur/matriks-literatur.md`
- `04-data/uji_ram.py`
- `06-output/Hasil_RAM_Chrome.xlsx`
- `06-output/Hasil_RAM_Chrome_lanjutan.xlsx`
- `06-output/Hasil_RAM_Firefox_5x.xlsx`
- `07-manuskrip/07-manuskrip.md`

Laporan ini siap untuk dijadikan bahan presentasi dan pertahanan penelitian.

---

## 7. Lampiran Dokumentasi dan Artefak

| Folder | Isi Utama | Status |
|---|---|---|
| `01-proposal/` | Proposal penelitian | Selesai |
| `02-literatur/` | Referensi dan matriks literatur | Tersedia |
| `03-teori/` | Desain eksperimen dan skema | Tersedia |
| `04-data/` | Skrip pengambilan data eksperimen | Selesai |
| `05-kode/` | Implementasi skrip uji dan eksperimen | Selesai |
| `06-output/` | Hasil eksperimen Excel | Selesai |
| `07-manuskrip/` | Draf naskah jurnal dan analisis | Sedang berjalan |
| `09-docs/` | Rencana dan dokumentasi tahapan | Selesai |

---

## Pernyataan Penutup

Laporan ini disusun berdasarkan data eksperimen yang tersedia dalam folder proyek, dengan penekanan pada transparansi, integritas, dan penyajian ilmiah. Data asli dan dokumen pendukung tersedia untuk verifikasi ulang.

# WS-12: Result Presentation & Visualization

> **Bab 12 — Penyajian Hasil & Visualisasi**

---

## Ringkasan Materi

### Data → Insight Model

```
Validated Data → Structured Presentation → Visualization → Pattern Recognition → Insight
```

Penyajian **mendahului** analisis. Tabel dan grafik membantu peneliti "melihat" data sebelum menghitung. Langsung ke uji statistik tanpa visualisasi berisiko kesimpulan yang secara teknis benar tapi kontekstual salah (Anscombe's Quartet, 1973).

### Tabel = Presisi, Grafik = Pola

Keduanya **saling melengkapi**:
- Tabel: angka presisi, self-contained (dipahami tanpa teks), sortable
- Grafik: pola visual, tren, perbandingan cepat

### Jenis Grafik Berdasarkan Tujuan

| Tujuan | Jenis Grafik |
|--------|-------------|
| Perbandingan antar-skenario | Bar chart (grouped/stacked) |
| Distribusi per-skenario | Box plot / violin plot |
| Tren temporal | Line chart |
| Korelasi dua variabel | Scatter plot |
| Proporsi (total = 100%) | Pie chart (hati-hati!) |

### Contoh Tabel Hasil yang Baik

| Model | Accuracy (%) | F1-Score (%) | Training Time (min) |
|-------|-------------|-------------|---------------------|
| BERT | 88.4 ± 1.2 | 87.1 ± 1.4 | 45.2 ± 3.1 |
| LSTM | 86.1 ± 1.8 | 84.5 ± 2.0 | 12.8 ± 1.2 |
| SVM | 82.3 ± 0.9 | 80.7 ± 1.1 | 0.3 ± 0.1 |

*N=10 per model. Mean ± std. Diurutkan berdasarkan Accuracy.*

### Visualization Bias — Yang Harus Dihindari

| Bias | Deskripsi | Dampak |
|------|----------|--------|
| Truncated axis | Y tidak dari 0 | Memperbesar perbedaan kecil |
| Inconsistent scale | Dua grafik skala beda | Perbandingan menyesatkan |
| Cherry-picked data | Hanya tampilkan yang "menang" | Selektif, tidak jujur |
| 3D effects | Efek 3D tanpa dimensi data ke-3 | Distorsi tanpa informasi |
| Missing error bar | Tidak ada variabilitas | Menyembunyikan ketidakpastian |

### Engineering vs Research Presentation

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan grafik | Dashboard monitoring | Mendukung argumen ilmiah |
| Informasi wajib | KPI, threshold | Mean, std, CI, N, p-value |
| Bias handling | Less critical | Wajib dihindari (peer-review) |

---

## Template A.12 — Result Presentation Plan

```
RESULT PRESENTATION PLAN

Research Question : ____________________
Metrik Utama      : ____________________

Tabel Hasil:
| Skenario | Metrik 1 (mean ± std) | Metrik 2 (mean ± std) | n |
|----------|----------------------|----------------------|---|
|          |                      |                      |   |

Visualisasi yang Direncanakan:
| # | Jenis Grafik | Pesan Utama | Metrik |
|---|-------------|-------------|--------|
| 1 |             |             |        |
| 2 |             |             |        |

Bias Check:
  [ ] Y-axis mulai dari 0 (atau dijustifikasi)
  [ ] Error bar/CI ditampilkan
  [ ] Semua data disertakan (tidak cherry-picked)
  [ ] Tidak menggunakan 3D tanpa alasan
```

---

## Latihan 1 — Tabel Hasil

Buat tabel hasil eksperimen Anda (boleh dengan data simulasi jika belum punya data riil).

| Skenario | Kapasitas RAM Peak (MB) | RAM Pasca 180s (MB) | n |
|----------|----------------------|----------------------|---|
| Google Chrome (Intervensi) | 6120.5 ± 350.2 | 5214.3 ± 450.8 | 40 |
| Mozilla Firefox (Baseline) | 4500.2 ± 250.4 | 3045.6 ± 180.5 | 40 |

**Checklist tabel:**
- [x] Self-contained (judul jelas, satuan ada, N tercantum)
- [x] Mean ± std (bukan single number)
- [x] Diurutkan berdasarkan metrik utama
- [x] Format konsisten di semua baris

---

## Latihan 2 — Rencana Visualisasi

Rencanakan 2-3 grafik untuk menyajikan data dari Latihan 1. Setiap grafik = satu pesan.

| # | Jenis Grafik | Pesan | Data yang Digunakan |
|---|-------------|-------|---------------------|
| 1 | Bar chart (grouped) + error bar | Perbandingan rata-rata memori awal (peak) dan pasca 180s antara Chrome dan Firefox | Mean RAM Peak & Mean RAM Pasca 180s ± std |
| 2 | Box plot | Distribusi sebaran konsumsi RAM pasca 180s dan visualisasi *outlier* (seperti efek *disk swapping*) | Seluruh 40 data mentah RAM Pasca 180s |

---

## Latihan 3 — Bias Detection

Evaluasi visualisasi berikut untuk bias (skenario dari contoh):

**Skenario:** Metode A = 91.2%, Metode B = 90.8%. Bar chart dengan Y-axis mulai dari 90%.

| Pertanyaan | Jawaban |
|-----------|---------|
| Apakah Y-axis menyesatkan? | Ya — Memulai Y-axis dari 90% membuat grafik Metode A secara visual tampak dua kali lipat lebih tinggi dari B, padahal selisih aslinya hanya 0.4%. |
| Apakah error bar ditampilkan? | Tidak — Mengaburkan informasi variabilitas; kita tidak tahu apakah selisih 0.4% itu signifikan atau hanya tumpang tindih (*overlap*) *noise* statistik. |
| Apakah semua kondisi ditampilkan? | Terindikasi tidak — Berpotensi *cherry-picking* jika sebenarnya ada metode C atau D yang disembunyikan. |
| Apa solusinya? | Mulai rentang Y-axis dari 0, tambahkan garis standar deviasi (*error bar*), dan tampilkan seluruh populasi skenario pengujian tanpa seleksi bias. |

**Evaluasi grafik Anda sendiri dari Latihan 2:**
- [x] Semua bias check lulus
- [ ] Ada yang perlu diperbaiki: -

---

## Refleksi

> Mengapa tabel dan grafik keduanya diperlukan — tidak cukup salah satu saja? Pernahkah Anda membuat grafik yang (tanpa sengaja) menyesatkan?

**Jawaban:**
> Keduanya saling melengkapi. Tabel menyediakan angka absolut dan tingkat presisi (*mean* dan *std*) yang esensial untuk memverifikasi perhitungan serta signifikansi statistik. Sebaliknya, grafik menerjemahkan rentetan angka tersebut menjadi pola visual, tren, dan sebaran anomali (*outlier*) yang jauh lebih cepat dipahami secara intuitif oleh pembaca.
> 
> Pernah. Pada pembuatan laporan tugas sebelumnya, saya sering menggunakan *bar chart* dengan skala Y-axis yang dipotong (tidak mulai dari 0) hanya agar perbedaan performa antar komponen terlihat mencolok. Selain itu, saya kerap kali hanya menampilkan angka rata-rata tunggal tanpa *error bar*, sehingga menyembunyikan ketidakstabilan sistem dari pembaca.
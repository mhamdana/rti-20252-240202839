# WS-07: Experimental Design & Validity

> **Bab 7 — Experimental Design & Validity**

---

## Ringkasan Materi

### Correlation ≠ Causality

Kausalitas membutuhkan 3 syarat:
1. **Covariance** — X dan Y bergerak bersama
2. **Temporal precedence** — X berubah sebelum Y
3. **Elimination of alternatives** — Tidak ada faktor lain yang menjelaskan Y

Controlled experiment adalah satu-satunya metode yang bisa membuktikan kausalitas.

### Empat Jenis Validitas

| Jenis | Pertanyaan | Ancaman Umum |
|-------|-----------|-------------|
| **Internal** | Apakah hubungan IV→DV nyata? | Confounding variable, selection bias |
| **External** | Apakah bisa digeneralisasi? | Dataset terlalu spesifik |
| **Construct** | Apakah mengukur konsep yang benar? | Metrik tidak sesuai |
| **Conclusion** | Apakah kesimpulan statistik valid? | Sample size kecil, uji salah |

Internal dan external validity sering berkonflik: semakin terkontrol (internal kuat) → semakin artificial (external lemah).

### Tiga Tipe Eksperimen dalam Riset TI

| Tipe | Deskripsi | Kapan Digunakan |
|------|----------|----------------|
| **Comparison Study** | Metode A vs B pada kondisi identik | Membandingkan pendekatan berbeda |
| **Ablation Study** | Full system → lepas komponen satu per satu | Mengukur kontribusi tiap komponen |
| **Parameter Study** | Variasikan satu parameter, amati dampak | Uji sensitifitas/robustness |

### Fairness dalam Perbandingan

Perbandingan yang adil = **kondisi identik** untuk semua metode: dataset sama, preprocessing sama, tuning effort sebanding, environment sama, metrik sama.

Contoh tidak adil: Transformer (30 fitur tambahan + Bayesian optimization) vs RF (default params) → hasilnya misleading.

### Threats to Validity = Diidentifikasi Sebelum Eksperimen

Ancaman validitas harus diidentifikasi **sebelum** eksperimen dan mitigasinya dirancang sebagai bagian dari desain — bukan ditulis sebagai boilerplate setelah selesai.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan testing | Memastikan sistem memenuhi requirement | Membuktikan hubungan kausal antar variabel |
| Baseline | Versi sebelumnya (last release) | Metode tervalidasi dari literatur |
| Kegagalan | Bug → fix → release | H₀ tidak ditolak → tetap kontribusi ilmiah |
| Sukses | 100% test pass | Evidence valid — mendukung atau menolak hipotesis |

### Istilah Penting

- **Causality** — Hubungan sebab-akibat (covariance + temporal + elimination)
- **Controlled Experiment** — Ubah satu variabel, kontrol sisanya, amati efek
- **Fairness** — Semua metode diuji pada kondisi yang benar-benar identik
- **Threats to Validity** — Faktor yang bisa melemahkan kesimpulan jika tidak dimitigasi
- **Conclusion Validity** — Validitas statistik: power, sample size, uji yang tepat

---

## Template A.7 — Desain Eksperimen Lengkap

```
EXPERIMENT DESIGN

Research Question : ____________________
Hypothesis        : ____________________
Tipe Eksperimen   : [ ] Comparison  [ ] Ablation  [ ] Parameter

Kondisi Eksperimen:
| Kondisi | Deskripsi | IV Value | CV Settings |
|---------|-----------|----------|-------------|
| Control |           |          |             |
| Treatment |         |          |             |

Fairness Checklist:
  [ ] Dataset identik untuk semua kondisi
  [ ] Preprocessing setara
  [ ] Tuning effort setara
  [ ] Environment identik
  [ ] Metrik evaluasi sama

Threat Analysis:
| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| Internal    |                 |          |
| External    |                 |          |
| Construct   |                 |          |
| Conclusion  |                 |          |

Statistical Plan:
  Uji statistik   : ____________________
  Justifikasi      : ____________________
  Alpha            : ____________________
  Effect size min  : ____________________
```

---
## Latihan 1 — Desain Eksperimen

Susun desain eksperimen berdasarkan RQ, variabel, dan sistem dari WS-04 sampai WS-06.

**RQ:** Apakah fitur Memory Saver pada Google Chrome menghasilkan retensi kapasitas memori RAM yang lebih besar dibandingkan fitur Tab Unloading pada Mozilla Firefox saat menangani 35 tab pasif?
**Tipe eksperimen:** [x] Comparison / [ ] Ablation / [ ] Parameter

| Kondisi | Deskripsi | IV Value | CV Settings |
|---------|-----------|----------|-------------|
| Control | Pengujian alokasi memori pada *browser* Mozilla Firefox menggunakan arsitektur independen berbasis mesin pembekuan bawaan Gecko. | Gecko Tab Unloading | Lingkungan OS Windows 11 desktop, 35 alamat URL identik kaya media, interval waktu tunggu pasif 15 menit, seluruh aplikasi latar belakang dinonaktifkan, kondisi sesi bersih (*clean session*). |
| Treatment | Pengujian alokasi memori pada *browser* Google Chrome menggunakan arsitektur isolasi terpisah berbasis mesin Chromium. | Chromium Memory Saver | Lingkungan OS Windows 11 desktop, 35 alamat URL identik kaya media, interval waktu tunggu pasif 15 menit, seluruh aplikasi latar belakang dinonaktifkan, kondisi sesi bersih (*clean session*). |

---

## Latihan 2 — Fairness Checklist

Evaluasi apakah desain eksperimen di Latihan 1 sudah fair.

| Kriteria | Status | Detail |
|----------|--------|--------|
| Dataset identik | ✅ | Kedua kondisi menggunakan 35 alamat URL situs web bermuatan kaya media yang sama persis dan diakses secara bersamaan. |
| Preprocessing setara | ✅ | Seluruh *cache* sistem dan riwayat penjelajah pada kedua aplikasi dibersihkan total (*clean session*) sebelum eksekusi pengujian dijalankan. |
| Tuning effort setara | ✅ | Kedua penjelajah web dijalankan murni menggunakan konfigurasi otomatis bawaan pabrikan (*mature default configurations*) tanpa modifikasi kode internal atau ekstensi tambahan. |
| Environment identik | ✅ | Eksperimen dijalankan pada unit komputer desktop yang sama dengan spesifikasi perangkat keras konstan dan seluruh *background apps* komersial dinonaktifkan. |
| Metrik evaluasi sama | ✅ | Kedua arsitektur dievaluasi menggunakan dua metrik kuantitatif yang identik: volume memori RAM terbebas (MB) dan durasi pelepasan (detik). |

**Ada yang tidak fair?** [ ] Ya / [x] Tidak
> Jika ya, bagaimana cara memperbaikinya? ________________

---

## Latihan 3 — Threat Analysis

Identifikasi ancaman validitas untuk desain eksperimen ini.

| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| Internal | Lonjakan utilisasi memori RAM acak akibat sub-proses latar belakang dinamis (*background noise*) milik OS host. | Menonaktifkan aplikasi non-esensial dan menerapkan metodologi pengujian kuantitatif berulang (*3x repeated run*) untuk mereduksi bias data. |
| External | Karakteristik pemuatan elemen *web page* yang dinamis berubah di sisi server saat pergantian jadwal pengujian antar-browser. | Menggunakan alamat URL rujukan dengan muatan data statis kaya media yang stabil atau membekukan skrip halaman web secara lokal. |
| Construct | Perkakas ukur pemantau internal (*internal profiler*) masing-masing aplikasi memiliki standar kalkulasi jejak RAM yang berbeda. | Mengandalkan instrumen netral **Windows Performance Monitor (PerfMon)** terintegrasi kernel OS untuk menangkap counter Private Bytes secara objektif. |
| Conclusion | Bias penarikan kesimpulan akibat anomali atau fluktuasi statistik dari satu kali eksekusi pengujian acak. | Menerapkan evaluasi kinerja ketat (*rigorous performance evaluation*) dengan menghitung rata-rata nilai penurunan dari data *repeated runs*. |

**Ancaman mana yang paling sulit dimitigasi?** Internal Validity (*Background Noise* OS Windows 11).
**Mengapa?**
> Karena kernel sistem operasi Windows 11 secara inheren selalu mengeksekusi sub-proses dinamis latar belakang (seperti skedul berkala kernel atau *indexing* berkas) yang tidak bisa dihentikan seutuhnya secara manual, sehingga potensi bias pengukuran skala kecil akan selalu ada pada level runtime sistem.

---

## Refleksi

> Sebuah paper melaporkan "metode kami mengalahkan semua baseline." Apa 3 pertanyaan pertama yang harus diajukan untuk mengevaluasi klaim ini?

**Jawaban:**
1. **Apakah baseline yang dipilih merepresentasikan standar teknologi terbaik saat ini (State-of-the-Art / SOTA)?** Perlu dipastikan bahwa peneliti tidak melakukan *straw man comparison* dengan sengaja membandingkan metode barunya dengan baseline yang usang, lemah, atau sengaja tidak dioptimalkan konfigurasinya.
2. **Apakah seluruh metode pembanding diuji di bawah kondisi lingkungan (environment) dan beban kerja yang benar-benar identik?** Perlu divalidasi apakah isolasi variabel kontrol, pembersihan sesi (*clean session*), dan spesifikasi hardware diberlakukan secara adil dan merata tanpa menguntungkan metode yang diajukan peneliti.
3. **Apakah keunggulan performa tersebut konsisten dan signifikan secara statistik melalui skenario pengujian berulang (repeated runs)?** Harus dipertanyakan apakah klaim keunggulan didukung oleh pengujian yang tangguh atau sekadar hasil manipulasi selektif data pencilan (*cherry-picking*) dari satu kali running eksperimen yang kebetulan menguntungkan.

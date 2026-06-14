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
| Control | Pengujian alokasi memori pada *browser* Mozilla Firefox (Gecko Engine) dengan parameter bawaan. | Gecko Tab Unloading | Lingkungan OS Windows 11 desktop, 35 alamat URL identik kaya media, interval waktu tunggu pasif 15 menit, *background applications* dinonaktifkan, *clean session*. |
| Treatment | Pengujian alokasi memori pada *browser* Google Chrome (Chromium Engine) dengan parameter bawaan. | Chromium Memory Saver | Lingkungan OS Windows 11 desktop, 35 alamat URL identik kaya media, interval waktu tunggu pasif 15 menit, *background applications* dinonaktifkan, *clean session*. |

---

## Latihan 2 — Fairness Checklist

Evaluasi apakah desain eksperimen di Latihan 1 sudah fair.

| Kriteria | Status | Detail |
|----------|--------|--------|
| Dataset identik | ✅ | Sama-sama memuat 35 alamat URL situs kaya media yang identik secara simultan. |
| Preprocessing setara | ✅ | Kedua *browser* dibersihkan seluruh *cache* sistemnya (*clean session*) sebelum pengujian dimulai. |
| Tuning effort setara | ✅ | Kedua objek uji menggunakan konfigurasi parameter otomatis bawaan yang sudah dioptimalkan oleh masing-masing vendor browser. |
| Environment identik | ✅ | Dieksekusi pada unit komputer desktop yang sama (Windows 11) dengan kondisi aplikasi latar belakang dinonaktifkan. |
| Metrik evaluasi sama | ✅ | Menggunakan parameter ukur yang sama: total kapasitas RAM terbebas (MB) dan kecepatan eksekusi pelepasan memori (detik). |

**Ada yang tidak fair?** [ ] Ya / [x] Tidak
> Jika ya, bagaimana cara memperbaikinya? ________________

---

## Latihan 3 — Threat Analysis

Identifikasi ancaman validitas untuk desain eksperimen ini.

| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| Internal | Lonjakan acak konsumsi RAM akibat proses latar belakang (*background noise*) dari OS Windows. | Menonaktifkan seluruh aplikasi latar belakang non-esensial dan menerapkan skenario pengujian berulang (*3x repeated run*). |
| External | Karakteristik muatan halaman web dinamis berubah di tingkat server saat pengujian antar-browser. | Menggunakan alamat rujukan web dengan muatan statis kaya media yang stabil atau membekukan skrip lokal. |
| Construct | Alat ukur performa internal masing-masing browser memiliki standarisasi pelaporan data yang berbeda. | Memakai **Windows Performance Monitor (PerfMon)** API terintegrasi pada kernel OS untuk menjamin kenetralan data. |
| Conclusion | Bias penarikan kesimpulan akibat anomali pembacaan log RAM dari satu kali pengujian acak. | Menerapkan metodologi *rigorous performance evaluation* dengan menarik rata-rata persentase penurunan dari data *repeated runs*. |

**Ancaman mana yang paling sulit dimitigasi?** Internal Validity (*Background Noise* OS Windows 11).
**Mengapa?**
> Karena kernel sistem operasi Windows 11 secara inheren selalu menjalankan sub-proses dinamis latar belakang (seperti skedul sistem atau indeks file) yang tidak dapat dimatikan seutuhnya, sehingga potensi bias pengukuran skala kecil akan selalu ada pada level runtime.

---

## Refleksi

> Sebuah paper melaporkan "metode kami mengalahkan semua baseline." Apa 3 pertanyaan pertama yang harus diajukan untuk mengevaluasi klaim ini?

**Jawaban:**
1. **Apakah baseline yang dipilih merepresentasikan standar industri terbaik (*State-of-the-Art*)?** Perlu dipastikan penelitian tidak melakukan *straw man comparison* dengan sengaja memilih pembanding lemah atau versi browser usang yang tidak dioptimalkan.
2. **Apakah seluruh kondisi lingkungan uji (*environment*) dijaga benar-benar identik tanpa menguntungkan salah satu pihak?** Harus divalidasi apakah proses pembersihan sistem (*clean session*) dan isolasi variabel kontrol diterapkan secara setara pada metode baru maupun baseline.
3. **Apakah keunggulan performa yang dilaporkan konsisten dan signifikan secara statistik melalui pengujian berulang (*repeated runs*)?** Kita harus mempertanyakan apakah hasil tersebut murni kapabilitas metode atau sekadar kebetulan statistik dari satu kali running eksperimen.

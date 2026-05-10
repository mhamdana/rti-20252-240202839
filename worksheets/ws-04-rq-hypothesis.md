# WS-04: Research Question & Hypothesis

> **Bab 4 — Research Question, Contribution & Hypothesis**

---

## Ringkasan Materi

### RQ Bukan Pertanyaan Biasa

Research Question yang baik secara implisit mengandung cetak biru eksperimen: subjek, baseline, metrik, domain, dataset.

| Kualitas | Contoh |
|----------|--------|
| **Buruk** | "Bagaimana pengaruh deep learning terhadap deteksi malware?" |
| **Baik** | "Apakah CNN menghasilkan F1-Score lebih tinggi dari RF pada CIC-MalMem-2022?" |

Perbedaan: RQ yang baik menyebutkan **metode spesifik**, **metrik terukur**, **baseline**, dan **dataset**.

### Tiga Jenis RQ

| Jenis | Pola | Kebutuhan |
|-------|------|-----------|
| **Comparison** | A vs B → mana lebih baik? | ≥ 2 metode, metrik sama |
| **Improvement** | A' vs A → modifikasi lebih baik? | Pre/post, bukti perbaikan |
| **Exploratory** | Faktor X₁...Xₙ → pengaruh terhadap Y? | Multi-variabel, korelasi/regresi |

### Contribution Statement

Tiga jenis kontribusi: **Improvement** (metode terbukti lebih baik), **Comparison** (perbandingan sistematis yang belum ada), **Novel Approach** (pendekatan baru). Kontribusi harus terhubung langsung dengan gap — kontribusi tanpa gap = klaim tanpa justifikasi.

### Hypothesis H₀ / H₁

- **H₀** (Null) = Tidak ada perbedaan signifikan — asumsi default, harus dibuktikan salah
- **H₁** (Alternative) = Ada perbedaan signifikan — diterima hanya jika H₀ ditolak
- Harus **falsifiable**, mengandung **metrik terukur**, dirumuskan **SEBELUM eksperimen**

### Rantai Operasionalisasi

```
RQ → Variable → Metric → Data → Analysis
```

Jika rantai ini tidak lengkap, RQ belum mature. Bi-directional: RQ yang tidak bisa jadi hipotesis testable harus direvisi mundur.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan pertanyaan | Apa yang harus dibangun? | Apa yang harus dibuktikan? |
| Bentuk jawaban | Sistem yang berfungsi | Bukti empiris terukur |
| Sukses diukur oleh | User satisfaction, uptime | Signifikansi statistik, effect size |
| Jika gagal | Debug dan perbaiki | Laporkan, analisis mengapa |

### Istilah Penting

- **Research Question (RQ)** — Pertanyaan spesifik: variabel terukur + metrik + konteks
- **Contribution Statement** — Apa yang diketahui setelah riset selesai yang sebelumnya belum ada
- **H₀ / H₁** — Null vs Alternative Hypothesis
- **Falsifiability** — Kondisi hipotesis ditolak harus bisa didefinisikan sebelum eksperimen
- **Operationalization** — Proses mewujudkan konsep abstrak menjadi variabel terukur

---

## Template A.4 — RQ-Contribution-Hypothesis

```
RQ-CONTRIBUTION-HYPOTHESIS

Gap Statement  : ____________________

Research Question:
  Tipe         : [ ] Comparison  [ ] Improvement  [ ] Exploratory
  Formulasi    : ____________________
  Variabel IV  : ____________________
  Variabel DV  : ____________________
  Metrik       : ____________________
  Dataset      : ____________________
  Baseline     : ____________________

Quality Check RQ:
  [ ] Variabel spesifik
  [ ] Metrik jelas
  [ ] Baseline ada
  [ ] Konteks disebutkan
  [ ] Memerlukan eksperimen (bukan hanya survei literatur)

Contribution Statement:
  Apa yang baru diketahui : ____________________
  Jenis kontribusi        : [ ] Improvement  [ ] Comparison  [ ] Novel approach
  Gap yang diisi          : ____________________

Hypothesis Pair:
  H₀ : ____________________
  H₁ : ____________________
  Threshold              : ____________________
  Justifikasi threshold  : ____________________
```

---

## Latihan 1 — Dari Gap ke RQ

Gunakan gap yang ditemukan di WS-03. Transformasikan menjadi Research Question.

**Gap dari WS-03:** Akurasi prediksi ETA sering meleset karena model gagal mendeteksi lonjakan durasi di lampu merah dan titik balik ojek online.

**RQ versi pertama (tulis bebas):**
> Bagaimana pengaruh lampu merah terhadap akurasi ojek online?

**Evaluasi RQ:**

| Komponen | Ada? | Isi |
|----------|------|-----|
| Metode spesifik | ya | XGBoost Regressor |
| Metrik terukur | ya | MAPE |
| Baseline | ya | XGBoost Standar |
| Dataset/konteks | ya | Data ojek online urban |

**Tipe RQ:** [ ] Comparison / [x] Improvement / [ ] Exploratory

**RQ versi revisi (setelah evaluasi):**
> "Apakah modifikasi model XGBoost dengan penambahan variabel durasi hambatan mikro dapat meningkatkan akurasi prediksi (menurunkan MAPE) dibandingkan dengan model XGBoost standar pada rute padat ojek online?"

---

## Latihan 2 — Hypothesis Pair

Rumuskan pasangan hipotesis dari RQ di Latihan 1.

| Komponen | Isi |
|----------|-----|
| H₀ | Tidak ada penurunan signifikan pada MAPE setelah penambahan fitur hambatan mikro pada model. |
| H₁ | Model dengan fitur hambatan mikro menghasilkan MAPE yang lebih rendah secara signifikan (p < 0.05). |
| Metrik | MAPE (Mean Absolute Percentage Error) |
| Threshold | Penurunan MAPE ≥ 5% |
| Justifikasi threshold | Batas minimal efisiensi yang dianggap berdampak pada kepuasan pengguna di industri transportasi. |

**Apakah hipotesis ini falsifiable?** [x] Ya / [ ] Tidak
> Bagaimana cara membuktikannya salah? Jika hasil pengujian menunjukkan p-value > 0.05 atau MAPE model baru justru lebih tinggi/sama dengan baseline.

---

## Latihan 3 — Rantai Operasionalisasi

Lengkapi rantai dari RQ hingga metode analisis.

| Tahap | Isi |
|-------|-----|
| RQ | Apakah integrasi fitur hambatan mikro meningkatkan akurasi ETA? |
| Variable (IV) | Fitur hambatan mikro (titik koordinat lampu merah & U-turn). |
| Variable (DV) | Error prediksi (MAPE).|
| Metric | Persentase selisih waktu prediksi vs waktu aktual.|
| Data source | GPS history logs & OpenStreetMap (untuk data lampu merah).|
| Analysis method | Uji komparatif performa model (T-Test pada hasil MAPE).|

**Apakah rantai lengkap?** [x] Ya / [ ] Tidak
> Jika tidak, tahap mana yang perlu direvisi? ______________

---

## Refleksi

> Ambil satu judul skripsi/paper yang pernah dibaca. Coba ekstrak RQ-nya. Apakah RQ tersebut memenuhi semua komponen (metode, metrik, baseline, konteks)? Jika tidak, apa yang hilang?

**Judul:** Optimasi Akurasi ETA Ojek Online melalui Integrasi Hambatan Mikro (Lampu Merah & Putar Balik) di Indonesia (Ahmad Fauzi, 2024)
**RQ yang diekstrak:** "Bagaimana meningkatkan akurasi prediksi permintaan dan rute ojek online menggunakan Machine Learning?"
**Komponen yang hilang:** RQ tersebut kehilangan metrik terukur yang spesifik (seperti MAPE atau RMSE) dan tidak menyebutkan baseline secara eksplisit dalam pertanyaannya, sehingga sulit untuk menentukan kapan riset tersebut dianggap berhasil secara kuantitatif.

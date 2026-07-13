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

**Gap dari WS-03:** Belum ada evaluasi empiris independen berskala masif (beban 40 tab) yang membandingkan secara langsung efisiensi reduksi RAM antara fitur bawaan mutakhir Google Chrome dan Mozilla Firefox menggunakan instrumen netral tingkat sistem operasi.

**RQ versi pertama (tulis bebas):**
> Apakah Google Chrome lebih efektif dalam menghemat RAM dibandingkan Firefox?

**Evaluasi RQ:**

| Komponen | Ada? | Isi |
|----------|------|-----|
| Metode spesifik | ya | Arsitektur Chromium (*Memory Saver*) |
| Metrik terukur | ya | Kapasitas RAM terbebas/terlepas (MB) |
| Baseline | ya | Arsitektur Gecko (*Tab Unloading* Firefox) |
| Dataset/konteks | ya | Lingkungan Windows 11, beban statis 40 tab pasif |

**Tipe RQ:** [x] Comparison / [ ] Improvement / [ ] Exploratory

**RQ versi revisi (setelah evaluasi):**
> "Apakah aktivasi fitur *Memory Saver* pada Google Chrome menghasilkan penghematan utilitas memori RAM absolut (MB) yang lebih besar dibandingkan *Tab Unloading* pada Mozilla Firefox ketika dieksekusi menangani 40 tab pasif secara serentak?"

---

## Latihan 2 — Hypothesis Pair

Rumuskan pasangan hipotesis dari RQ di Latihan 1.

| Komponen | Isi |
|----------|-----|
| H₀ | Tidak terdapat perbedaan rata-rata penghematan kapasitas memori RAM (MB) yang signifikan antara Google Chrome dan Mozilla Firefox pada beban 40 tab pasif. |
| H₁ | Google Chrome menghasilkan penghematan memori RAM absolut (MB) yang lebih besar secara signifikan (p < 0.05) dibandingkan Mozilla Firefox. |
| Metrik | Kapasitas RAM (*Private Bytes*) yang berhasil dibebaskan pasca mode *idle* (Megabytes). |
| Threshold | Signifikansi statistik *p-value* < 0.05. |
| Justifikasi threshold | Menggunakan standar interval kepercayaan 95% untuk memastikan bahwa selisih memori yang terjadi benar-benar akibat perbedaan arsitektur, bukan karena fluktuasi acak (*background noise*) sistem operasi. |

**Apakah hipotesis ini falsifiable?** [x] Ya / [ ] Tidak
> Bagaimana cara membuktikannya salah? H₀ akan dipertahankan (dan hipotesis awal terbantahkan) jika uji beda statistik menunjukkan nilai *p-value* > 0.05, atau jika data justru menunjukkan Firefox membebaskan RAM jauh lebih besar daripada Chrome.

---

## Latihan 3 — Rantai Operasionalisasi

Lengkapi rantai dari RQ hingga metode analisis.

| Tahap | Isi |
|-------|-----|
| RQ | Apakah *Memory Saver* Chrome menghemat RAM lebih besar dari Firefox pada beban 40 tab pasif? |
| Variable (IV) | Jenis Arsitektur *Browser* (Chromium vs Gecko). |
| Variable (DV) | Kapasitas utilitas memori RAM perangkat. |
| Metric | Selisih *Private Bytes* memori dalam satuan Megabytes (MB). |
| Data source | Log ekstraksi *counter* Windows Performance Monitor (PerfMon) dari 80 *repeated runs*. |
| Analysis method | Uji komparatif beda rata-rata dua kelompok independen (*Independent Sample T-Test*). |

**Apakah rantai lengkap?** [x] Ya / [ ] Tidak
> Jika tidak, tahap mana yang perlu direvisi? -

---

## Refleksi

> Ambil satu judul skripsi/paper yang pernah dibaca. Coba ekstrak RQ-nya. Apakah RQ tersebut memenuhi semua komponen (metode, metrik, baseline, konteks)? Jika tidak, apa yang hilang?

**Judul:** Evaluation of Rust and WebAssembly when building a Progressive Web Application: An analysis of performance and memory usage (Asegehegn, 2022).
**RQ yang diekstrak:** "Bagaimana performa dan penggunaan memori aplikasi PWA berbasis Rust/Wasm dibandingkan dengan kerangka kerja berbasis JavaScript?"
**Komponen yang hilang:** RQ dalam literatur tersebut kehilangan metrik terukur yang spesifik (tidak menyebutkan *Lighthouse FCP* atau ukuran blok *Heap* dalam pertanyaan utamanya) serta gagal mendefinisikan batasan konteks beban kerja (seperti besaran *DOM nodes* atau jenis *environment*), sehingga parameter pembuktian keberhasilannya menjadi ambigu di awal.
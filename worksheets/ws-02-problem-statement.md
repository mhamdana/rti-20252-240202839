# WS-02: Problem Statement

> **Bab 2 — Problem Formulation & System Context**

---

## Ringkasan Materi

### Problem Formation Model

Masalah riset melewati 5 tahap transformasi. Melompat langsung dari Reality ke Variable adalah kesalahan paling umum.

```
Reality → Observed Issue (Symptom) → Diagnosed Problem (Root Cause)
→ Researchable Problem (Scoped) → Measurable Variable (Operationalized)
```

### Topic ≠ Problem ≠ Research Problem

| Level | Contoh | Status |
|-------|--------|--------|
| **Topik** | Keamanan IoT | Terlalu luas, tidak bisa diuji |
| **Problem** | MQTT tidak terenkripsi | Spesifik tapi belum riset |
| **Research Problem** | Belum ada studi membandingkan overhead TLS 1.3 vs DTLS pada MQTT di IoT RAM < 64KB | Bisa dirancang eksperimennya |

### Symptom vs Root Cause

Apa yang diamati (gejala) ≠ mengapa terjadi (akar masalah). Gunakan **5 Whys** atau **Fishbone Diagram** untuk menggali.

Contoh: "User meninggalkan checkout" (symptom) → "Waktu loading > 8 detik karena API call sequential" (root cause).

### System Thinking

Setiap masalah riset TI harus terikat pada komponen sistem: **Input → Process → Output → Outcome → Constraints → Stakeholders**.

### Problem Quality Check

Masalah riset yang layak harus memenuhi 5 kriteria:
- **Clarity** — Satu orang membaca akan paham
- **Measurability** — Ada metrik kuantitatif
- **Relevance** — Penting untuk domain
- **Testability** — Bisa gagal (falsifiable)
- **Impact** — Ada kontribusi jika terjawab

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan | Menyelesaikan masalah (*solve*) | Memahami dan membuktikan (*understand & prove*) |
| Masalah | Bug, error, fitur belum ada | Gap dalam pengetahuan |
| Scope | Selesaikan semua yang perlu | Batasi agar bisa dibuktikan |
| Output | Working system | Evidence, paper, replicable findings |

### Istilah Penting

- **Problem Statement** — Formulasi tertulis: konteks sistem + gap + dampak + justifikasi
- **System Context** — Deskripsi lengkap: input, proses, output, outcome, constraints, stakeholders
- **Problem Drift** — Masalah "bermutasi" dari pendahuluan ke metodologi karena statement awal tidak presisi
- **Solution-First Thinking** — Memulai dari solusi tanpa masalah yang jelas — berbahaya dalam riset
- **Operational Definition** — Definisi variabel yang cukup jelas agar peneliti lain bisa mengukur hal yang sama

---

## Template A.2 — Problem Statement Builder

```
PROBLEM STATEMENT BUILDER

Domain & Konteks
  Domain   : ____________________
  Konteks  : ____________________

System Context
  Input       : ____________________
  Process     : ____________________
  Output      : ____________________
  Outcome     : ____________________
  Constraints : ____________________
  Stakeholders: ____________________

Fenomena → Problem
  Fenomena yang diamati             : ____________________
  Gejala (symptom) yang terukur     : ____________________
  Masalah yang didiagnosis          : ____________________
  Masalah riset (researchable)      : ____________________
  Variabel yang terukur             : ____________________

Problem Quality Check
  [ ] Clarity — Apakah satu orang membaca akan paham?
  [ ] Measurability — Apakah ada metrik kuantitatif?
  [ ] Relevance — Apakah penting untuk domain?
  [ ] Testability — Apakah bisa gagal?
  [ ] Impact — Apakah ada kontribusi jika terjawab?

Problem Statement (1 paragraf):
  ____________________
```

---

## Latihan 1 — Dari Topik ke Masalah Riset

Pilih satu topik di bidang TI yang diminati. Transformasikan melalui 5 tahap Problem Formation Model.

**Topik awal:** Analisis Performa dan Manajemen Memori pada Aplikasi Web Browser Modern.

| Tahap | Hasil |
|-------|-------|
| Reality | Pengguna laptop dengan spesifikasi perangkat keras standar sering mengalami kelambatan sistem saat membuka puluhan tab penjelajah web secara bersamaan. |
| Observed Issue (Symptom) | Terjadi penurunan responsivitas sistem (lag/hang) yang dipicu oleh lonjakan utilisasi RAM hingga menyentuh batas kapasitas maksimal perangkat. |
| Diagnosed Problem (Root Cause) | Perbedaan arsitektur manajemen memori (*sandboxing* pada Chromium vs *multithreading* pada Gecko) menghasilkan beban konsumsi RAM yang berbeda, di mana belum diketahui secara pasti seberapa efektif fitur penghemat bawaan masing-masing bekerja pada skala masif. |
| Researchable Problem | Evaluasi dan analisis komparatif mengenai tingkat efisiensi reduksi memori RAM secara absolut antara fitur *Memory Saver* (Google Chrome) dan *Tab Unloading* (Mozilla Firefox) saat dibebani puluhan tab pasif. |
| Measurable Variable | Kapasitas RAM yang terpakai dan terbebas pasca-jeda waktu stabilisasi (*Private Bytes* dalam satuan Megabytes/MB). |

**Apakah terjebak solution-first thinking?** [ ] Ya / [x] Tidak
> Jika ya, kembali ke tahap mana? Tidak. Analisis berakar dari fenomena kebuntuan performa (bottleneck) komputasi fisik di lapangan akibat beban kerja *multi-tab*, bukan berangkat dari keinginan sekadar memvalidasi satu *browser* tertentu.

---

## Latihan 2 — System Context Decomposition

Gambarkan konteks sistem dari masalah riset di Latihan 1.

| Komponen | Deskripsi |
|----------|----------|
| Input | 40 URL situs web bermuatan kaya media (statis) yang dieksekusi secara otomatis, serta kondisi memori awal dari sistem operasi. |
| Process | Pemuatan halaman web secara serentak oleh *engine browser* dan pemicuan fitur manajemen memori latar belakang (*Memory Saver* / *Tab Unloading*) selama fase pasif 180 detik. |
| Output | Log perekaman nilai *Private Bytes* (MB) yang diekstrak secara berkala melalui instrumen Windows Performance Monitor. |
| Outcome | Tersedianya acuan empiris dan objektif bagi pengguna laptop berspesifikasi pas-pasan dalam memilih arsitektur *browser* yang paling stabil untuk beban kerja ekstrem. |
| Constraints | Batasan memori RAM fisik (16 GB), intervensi proses latar belakang acak dari sistem operasi (Windows 11), serta fenomena peralihan beban ke *disk swapping*. |
| Stakeholders | Pengguna Akhir (*End-Users*) dengan perangkat spesifikasi standar, Pengembang Perangkat Lunak, dan Vendor Web Browser. |

**Komponen mana yang paling relevan dengan masalah riset?** Process (Pemicuan fitur manajemen memori latar belakang dari masing-masing arsitektur *browser* selama fase pasif).

---

## Latihan 3 — Problem Quality Check

Evaluasi problem statement yang sudah dibuat menggunakan 5 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Clarity | 5 | Sangat jelas; langsung memetakan korelasi antara perilaku fitur penghemat memori aplikasi dan beban komputasi tingkat kernel. |
| Measurability | 5 | Menggunakan satuan ukuran absolut yang eksak (Megabytes) melalui instrumen perekam OS bawaan yang netral (PerfMon). |
| Relevance | 5 | Amat relevan dengan kebiasaan komputasi modern di mana pengguna sering membiarkan banyak *tab* terbuka sebagai bentuk *multitasking*. |
| Testability | 5 | Dapat diuji secara empiris melalui metodologi *comparison study* pada lingkungan eksperimen laboratorium dengan *clean session*. |
| Impact | 5 | Memberikan wawasan arsitektural untuk menghindari klaim sepihak dari vendor *browser* mengenai efisiensi alokasi memori. |

**Skor total:** 25 / 25

**Problem statement versi final (1 paragraf):**
> Penggunaan aplikasi penjelajah web dalam skenario *multi-tab* masif sering memicu lonjakan konsumsi memori yang mengakibatkan penurunan performa sistem (*lag/hang*) secara menyeluruh, terutama bagi pengguna laptop berspesifikasi standar. Meskipun Google Chrome dan Mozilla Firefox telah mengimplementasikan fitur manajemen memori bawaan (*Memory Saver* dan *Tab Unloading*), terdapat kesenjangan data evaluatif empiris mengenai perbedaan efektivitas reduksi RAM secara nyata di antara arsitektur Chromium dan Gecko saat menangani beban kerja berat. Penelitian ini bertujuan untuk menginvestigasi apakah fitur *Memory Saver* pada Chrome mampu menghasilkan retensi memori RAM yang lebih efisien dibandingkan *Tab Unloading* pada Firefox saat dieksekusi menangani 40 tab pasif. Pemetaan performa memori secara kuantitatif ini krusial guna memberikan rekomendasi arsitektur yang paling kebal terhadap kelambatan sistem akibat *bottleneck* komputasi.

---

## Refleksi

> Bandingkan "masalah" yang biasa ditemui saat coding (bug, error) dengan masalah riset. Apa perbedaan fundamental dalam cara mendefinisikan dan mendekati keduanya?

**Jawaban:**
> Perbedaan fundamentalnya terletak pada objektivitas akhir. Masalah saat *coding* (seperti galat *Out of Memory* atau *crash*) adalah masalah teknis yang menuntut perbaikan perbaikan instan agar program kembali berjalan normal (*engineering mindset*). Di sisi lain, masalah riset mendefinisikan fenomena tersebut sebagai celah pengetahuan (*knowledge gap*). Saat OS menjadi lambat karena RAM penuh, riset tidak mencari cara menambal kodenya saat itu juga, melainkan merancang eksperimen terkontrol dengan instrumen *logging* yang ketat (seperti perekaman 40 *repeated runs* pasca-jeda 180 detik) untuk memahami pola aslinya. Pendekatannya adalah observasi tanpa memihak demi menghasilkan kesimpulan statistik yang valid dan dapat diandalkan oleh komunitas ilmiah.
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

**Topik awal:** Analisis Performa dan Manajemen Memori Runtime pada Aplikasi Web Modern.

| Tahap | Hasil |
|-------|-------|
| Reality | Pengguna perangkat desktop dengan kapasitas memori terbatas sering mengalami kelambatan sistem saat membuka banyak tab browser sekaligus. |
| Observed Issue (Symptom) | Terjadi penurunan responsivitas sistem operasi secara menyeluruh (lag/hang) dan lonjakan utilisasi RAM hingga mendekati batas maksimal. |
| Diagnosed Problem (Root Cause) | Tingginya overhead footprint dan kebocoran memori (memory leak) pada sub-proses mesin rendering runtime saat mengeksekusi framework web modern yang sarat skrip berat. |
| Researchable Problem | Evaluasi dan analisis komparatif dampak penggunaan WebAssembly (Wasm) vs JavaScript terhadap efisiensi manajemen alokasi heap memory dan execution performance aplikasi web. |
| Measurable Variable | Jejak memori runtime (JSHeapUsedSize/Private Bytes dalam MB) dan metrik performa (Largest Contentful Paint/LCP dalam detik). |

**Apakah terjebak solution-first thinking?** [ ] Ya / [x] Tidak
> Jika ya, kembali ke tahap mana? Tidak, karena analisis berakar dari fenomena degradasi performa hardware akibat beban kerja aplikasi web secara riil di lapangan.

---

## Latihan 2 — System Context Decomposition

Gambarkan konteks sistem dari masalah riset di Latihan 1.

| Komponen | Deskripsi |
|----------|----------|
| Input | Source code aplikasi web (skrip JavaScript / modul biner WebAssembly), interaksi user (pembukaan komponen halaman), dan alokasi resource awal hardware. |
| Process | Eksekusi engine runtime penjelajah web, manajemen daur hidup heap memory, serta isolasi pemrosesan latar belakang (background process). |
| Output | Visualisasi antarmuka halaman web interaktif dan visualisasi log tracing konsumsi resource memori. |
| Outcome | Terwujudnya arsitektur aplikasi web modern lintas platform yang ringan, hemat daya, dan responsif tanpa membebani memori sistem. |
| Constraints | Batasan kapasitas fisik memori RAM perangkat target (khususnya perangkat mobile/spesifikasi standar) dan limitasi kapabilitas pelaporan alat ukur memori internal browser. |
| Stakeholders | Web Developers (Pengembang Perangkat Lunak), Penyedia Framework Web, dan End-Users (Pengguna Perangkat Spesifikasi Standar). |

**Komponen mana yang paling relevan dengan masalah riset?** Process (Manajemen daur hidup heap memory dan eksekusi sub-proses engine runtime).

---

## Latihan 3 — Problem Quality Check

Evaluasi problem statement yang sudah dibuat menggunakan 5 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Clarity | 5 | Sangat jelas; mendefinisikan batas tegas antara konsumsi resource komputasi runtime dan hambatan performa sistem fisik. |
| Measurability | 5 | Menggunakan satuan ukuran data yang eksak (Megabytes) dan standar metrik audit performa web (detik) secara objektif. |
| Relevance | 5 | Amat relevan dengan tren migrasi arsitektur aplikasi native menuju ekosistem Progressive Web Applications (PWA). |
| Testability | 5 | Dapat diuji secara empiris melalui komparasi prototype fungsional di bawah kondisi beban kerja laboratorium terkontrol. |
| Impact | 5 | Memberikan acuan arsitektural yang valid bagi pengembang dalam memitigasi isu kebocoran memori pada eksekusi runtime modern. |

**Skor total:** 25 / 25

**Problem statement versi final (1 paragraf):**
> Tren pengembangan aplikasi web modern lintas platform yang sarat akan skrip berat sering memicu lonjakan konsumsi heap memory pada sub-proses mesin rendering penjelajah web. Bagi pengguna perangkat berspesifikasi standar atau mobile, tingginya footprint runtime ini mengakibatkan degradasi performa komputasi di tingkat kernel berupa kelambatan sistem secara menyeluruh (lag/hang) akibat operasi disk swapping. Meskipun teknologi WebAssembly (Wasm) hadir menawarkan Lightweight Isolation dan Secure Memory Sandbox, belum ada data evaluatif empiris yang komprehensif mengenai tingkat efisiensi alokasi memori nyata dan responsivitas pemulihannya dibandingkan dengan JavaScript di bawah kondisi beban kerja yang identik. Penelitian ini bertujuan untuk memetakan performa jejak memori (memory traces) kedua arsitektur runtime secara kuantitatif guna meminimalkan nilai overhead footprint sistem penjelajah web.

---

## Refleksi

> Bandingkan "masalah" yang biasa ditemui saat coding (bug, error) dengan masalah riset. Apa perbedaan fundamental dalam cara mendefinisikan dan mendekati keduanya?

**Jawaban:**
> Perbedaan fundamentalnya terletak pada status operasional sistem, tujuan akhir, dan metodologi penyelesaiannya. Masalah saat coding berupa bug atau error teknis ditandai dengan kegagalan crash atau berhentinya fungsionalitas sistem (sistem tidak berjalan), sehingga pendekatannya adalah perbaikan kode secara instan atau local debugging agar fitur kembali berfungsi normal. Sebaliknya, masalah riset (research problem) berfokus pada gap performa, ketidakstabilan alokasi resource, atau ketidakoptimalan sistem (sistem sudah berjalan dengan baik, tetapi perilakunya belum dipahami sepenuhnya). Pendekatannya tidak melulu memperbaiki error saat itu juga, melainkan mengisolasi variabel, mengunci konfigurasi kontrol, dan mengumpulkan data kuantitatif melalui eksperimen berulang (repeated runs) demi menghasilkan kontribusi pengetahuan empiris yang terstandarisasi dan dapat direplikasi oleh peneliti lain.

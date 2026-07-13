# WS-09: Implementation & Environment

> **Bab 9 — Implementasi Riset & Kontrol Lingkungan**

---

## Ringkasan Materi

### Implementasi Riset ≠ Coding Biasa

Tujuan implementasi riset bukan membuat software yang berfungsi, melainkan membangun **instrumen pengukuran yang konsisten**. Setiap modul harus di-mapping ke variabel (dari Bab 6), parameter harus config-driven, dan logging aktif dari hari pertama.

> **Mengapa reproducibility penting?** Sains dibangun di atas prinsip verifikasi — temuan harus bisa dikonfirmasi oleh peneliti lain. _Replicability crisis_ yang terjadi di banyak paper riset ML/AI disebabkan oleh environment tidak terdokumentasi: orang lain tidak bisa reproduksi, hasil diragukan, kepercayaan terhadap temuan hilang. Prinsip: **dokumentasi environment = snapshot kredibilitas riset Anda.**

### Reproducible Implementation Model

```
Design → Implementation → Environment Setup → Execution Consistency → Reproducibility → Trustworthy Result
```

Setiap transisi memiliki syarat:
- Design → Implementation: kode sesuai mapping variabel-ke-komponen
- Implementation → Environment: versi, dependency, seed, path, OS eksplisit
- Environment → Consistency: seed terkunci, urutan deterministik
- Consistency → Reproducibility: dokumentasi lengkap
- Reproducibility → Trust: siapa pun ikuti dokumentasi → hasil sama/serupa

### Repeatability vs Reproducibility

| Level | Peneliti | Environment | Hasil |
|-------|---------|-------------|-------|
| **Repeatability** | Sama | Sama | Sama persis |
| **Reproducibility** | Berbeda | Berbeda (ikuti docs) | Sama/serupa |

Capai **repeatability** dulu, baru **reproducibility**.

### Engineering vs Research Perspective

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan | Sistem berfungsi untuk user | Instrumen pengukuran konsisten |
| Dependency | Update ke terbaru | Lock di versi spesifik |
| Testing | Unit, integration, E2E | Repeatability test (run ulang → sama?) |
| Dokumentasi | User guide, API docs | Environment spec, execution steps, expected output |
| Config | Default masuk akal | Setiap parameter eksplisit & adjustable |

### Jebakan Kognitif

1. Menunda environment setup → bug sulit dilacak
2. Tidak pakai version control → hasil tidak bisa direkonstruksi
3. Menolak Docker/container → "di laptop saya bisa" saat review
   - **Docker** = teknologi container yang "membungkus" aplikasi beserta seluruh dependency-nya dalam satu unit terisolasi. Hasilnya: kode berjalan identik di laptop, server, maupun reviewer lain. Intro singkat: `docker run -v $(pwd):/workspace environment-image python run_experiment.py`
4. 3× hasil sama ≠ repeatable (bisa cache/state tersimpan)

### Dependency Locking

Mengandalkan "install library terbaru" berbahaya: versi berbeda = perilaku berbeda = hasil tidak reproducible. Praktik:
- **Python**: buat `requirements.txt` dengan versi eksplisit: `scikit-learn==1.3.2`, lalu kunci dengan `pip freeze > requirements.txt`
- **Conda**: gunakan `conda env export > environment.yml` untuk snapshot lengkap
- **Node.js/R/Julia**: gunakan `package-lock.json` / `renv.lock` / `Project.toml` — semua fungsi serupa: lock versi + hash

### Istilah Penting

- **Environment Specification** — Deskripsi lengkap: hardware, OS, runtime, library + versi, config, seed
- **Dependency** — Komponen eksternal yang harus di-lock versinya
- **Config-driven** — Parameter dieksternalisasi ke file konfigurasi, bukan hardcode

---

## Template A.9 — Dokumentasi Setup Eksperimen

```
EXPERIMENT SETUP DOCUMENTATION

Hardware:
  CPU     : ____________________
  RAM     : ____________________
  GPU     : ____________________
  Storage : ____________________

Software:
  OS        : ____________________
  Runtime   : ____________________
  Framework : ____________________

Dependencies:
| Library | Version | Sumber | Hash/Checksum |
|---------|---------|--------|---------------|
|         |         |        |               |
|         |         |        |               |

Konfigurasi:
  Config file     : ____________________
  Random seed     : ____________________
  Hyperparameters : ____________________

Reproducibility Check:
  [ ] Dependency terdokumentasi (requirements.txt / lock file)
  [ ] Seed ditetapkan di semua level (Python, NumPy, framework)
  [ ] Config di version control
  [ ] README instruksi reproduksi lengkap
```

---

## Tugas 1 — Environment Specification

Dokumentasikan environment untuk eksperimen Anda (boleh environment saat ini atau yang direncanakan).

| Komponen | Spesifikasi |
|----------|------------|
| CPU | AMD Ryzen (Laptop Advan Workplus) |
| RAM | 16 GB LPDDR5 |
| GPU | AMD Radeon Integrated Graphics |
| OS | Windows 11 Desktop (64-bit) |
| Runtime | Python 3.10 (untuk agregasi dan analisis data CSV) |
| Framework | N/A (Pengujian native di tingkat OS) |
| Random Seed | N/A (Eksperimen tidak melibatkan model stokastik) |

**Dependencies (minimal 5):**

| Library/Software | Version | Alasan Dibutuhkan |
|---------|---------|-------------------|
| Google Chrome | Stable Terbaru | Objek eksperimen intervensi (pengujian fitur *Memory Saver*) |
| Mozilla Firefox | Stable Terbaru | Objek eksperimen baseline (pengujian fitur *Tab Unloading*) |
| Windows PerfMon | Bawaan OS | Instrumen utama perekam *Private Bytes* memori sistem secara objektif |
| Pandas (Python) | 2.1.0 | Membersihkan dan mengagregasi data log dari 40 *repeated runs* |
| Matplotlib (Python) | 3.8.0 | Memvisualisasikan grafik tren penurunan RAM sebelum dan sesudah 15 menit |

---

## Tugas 2 — Repeatability Test Plan

Rancang tes repeatability sederhana: jalankan kode yang sama 3× di environment yang sama.

| Run | Seed | Metrik Utama | Hasil Sama? |
|-----|------|-------------|-------------|
| 1 | N/A | Kapasitas RAM Terbebas (MB) | — |
| 2 | N/A | Kapasitas RAM Terbebas (MB) | [ ] Ya / [x] Tidak (Akan ada deviasi nilai MB) |
| 3 | N/A | Kapasitas RAM Terbebas (MB) | [ ] Ya / [x] Tidak (Akan ada deviasi nilai MB) |

**Jika hasil berbeda, kemungkinan penyebab:**

> Penyebab umum non-repeatability dalam pengukuran sistem memori:
> - **Background process** — Layanan latar belakang Windows 11 (seperti *indexing*, pembaruan senyap, atau *antivirus*) aktif dan memakan/melepas RAM saat *run* berlangsung.
> - **Thermal throttling** — CPU laptop mengalami panas berlebih setelah mengeksekusi puluhan tab secara berulang, sehingga menurunkan *clock speed* dan memperlambat waktu eksekusi pelepasan memori.
> - **Cache dari run sebelumnya** — Data sisa dari sesi web sebelumnya belum terhapus sempurna, membuat beban *rendering* pada *run* berikutnya menjadi lebih ringan.

___________________________________________________

**Checklist kontrol yang sudah diterapkan:**
- [ ] Random seed di-set di semua level *(Tidak relevan untuk eksperimen ini)*
- [x] Tidak ada background process yang mengganggu *(Aplikasi non-esensial dinonaktifkan)*
- [x] Cache dibersihkan antar-run *(Menerapkan prosedur Clean Session)*
- [x] Config file yang sama untuk semua run *(Menggunakan 40 URL identik)*

---

## Tugas 3 — README Eksperimen

Tulis README minimum untuk eksperimen Anda (6 komponen wajib).

# Judul Eksperimen: Analisis Komparatif Efisiensi Alokasi Memori RAM Berbasis Mekanisme Pembekuan Tab Pasif

## 1. Environment
> Hardware: Advan Workplus (AMD Ryzen, 16 GB RAM).
> OS: Windows 11 Desktop (64-bit).
> Software: Google Chrome (Stable) dan Mozilla Firefox (Stable).

## 2. Installation
> 1. Unduh dan instal rilis stabil terbaru dari Google Chrome dan Mozilla Firefox tanpa ekstensi tambahan.
> 2. Pastikan fitur Memory Saver (Chrome) dan Tab Unloading (Firefox) dalam keadaan aktif (enabled) di pengaturan.
> 3. Siapkan Python 3.10 dan jalankan `pip install pandas matplotlib` untuk kebutuhan analisis log.

## 3. Data
> Input berupa file teks berisi 40 URL situs web bermuatan kaya media (portal berita, aplikasi web). Data output berupa file CSV log rekaman RAM dari Windows Performance Monitor.

## 4. Execution
> 1. Jalankan Windows PerfMon dan mulai rekam counter *Private Bytes*.
> 2. Buka Browser A pada kondisi *clean session*.
> 3. Buka ke-40 URL secara bersamaan dan tunggu hingga seluruh elemen termuat.
> 4. Biarkan browser berada di latar belakang selama 15 menit.
> 5. Ekstrak data CSV, tutup browser, bersihkan riwayat dan cache, lalu ulangi iterasi hingga mencapai 40 putaran (*repeated runs*). Lakukan hal yang sama untuk Browser B.

## 5. Configuration
> Tidak ada aplikasi komersial pihak ketiga yang berjalan di latar belakang (seperti platform game atau pemutar musik). Jendela browser tidak dijalankan dalam mode Incognito/Private agar mekanisme caching bawaan tetap berjalan normal.

## 6. Expected Output
> Dua set dataset CSV yang merekam metrik konsumsi memori (MB). Data akan menampilkan nilai puncak (peak memory) saat pemuatan awal dan nilai terendah pasca 15 menit tab dibekukan.

---

## Refleksi

> Apakah eksperimen Anda saat ini bisa direproduksi oleh orang lain tanpa bantuan Anda? Komponen apa yang masih hilang?

**Level saat ini:** [ ] Repeatability / [x] Reproducibility / [ ] Belum keduanya
**Komponen yang belum terdokumentasi:**
> Skrip otomatisasi (misalnya menggunakan Selenium atau alat makro UI). Saat ini, pembukaan 40 tab diasumsikan dilakukan secara manual yang dapat memicu perbedaan jeda latensi akibat faktor manusia antar-putaran (*run*). Hal ini berisiko menciptakan bias mikro pada metrik pengukuran durasi (detik).
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

**Topik awal:** Optimasi Akurasi Estimasi Waktu (ETA) pada Aplikasi Mobile.

| Tahap | Hasil |
|-------|-------|
| Reality | Masyarakat sering merasa estimasi waktu di aplikasi ojek online tidak akurat saat macet |
| Observed Issue (Symptom) | Terjadi delay kedatangan driver yang signifikan dibandingkan angka di aplikasi |
| Diagnosed Problem (Root Cause) | Model gagal memprediksi perlambatan di titik-titik putar balik (U-Turn) yang padat |
| Researchable Problem | Analisis pengaruh penambahan variabel "U-Turn Penalty" pada algoritma rute terhadap akurasi ETA |
| Measurable Variable | Selisih waktu (menit) dan RMSE (Root Mean Square Error) |

**Apakah terjebak solution-first thinking?** [ ] Ya / [ ] Tidak
> Jika ya, kembali ke tahap mana? Tidak, karena analisis dimulai dari gejala keterlambatan di lapangan.

---

## Latihan 2 — System Context Decomposition

Gambarkan konteks sistem dari masalah riset di Latihan 1.

| Komponen | Deskripsi |
|----------|----------|
| Input | Koordinat GPS Driver & User, peta digital, data kemacetan, jam operasional, dan data cuaca |
| Process | Pengolahan rute tercepat dan kalkulasi beban waktu pada setiap titik hambatan jalan |
| Output | Tampilan numerik waktu tunggu di layar aplikasi pengguna (Contoh: "5 Menit Lagi") |
| Outcome | Peningkatan kepastian waktu bagi penumpang dan efisiensi manajemen jadwal driver |
| Constraints | Akurasi sinyal GPS (GPS Drift) di area gedung tinggi dan update data trafik yang tidak instan |
| Stakeholders | Penumpang, Mitra Driver, dan Tim Pengembang Sistem (Engineer) |

**Komponen mana yang paling relevan dengan masalah riset?** Process (Logika algoritma prediksinya).

---

## Latihan 3 — Problem Quality Check

Evaluasi problem statement yang sudah dibuat menggunakan 5 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Clarity | 5 | Sangat jelas; membedakan antara "janji" aplikasi dan realita kedatangan |
| Measurability | 5 | Menggunakan satuan menit dan metrik statistik (MAE) yang objektif |
| Relevance | 5 | Sangat relevan bagi industri transportasi digital di Indonesia |
| Testability | 5 | Bisa diuji dengan membandingkan data aktual vs prediksi model baru |
| Impact | 4 | Berdampak besar pada kepuasan pelanggan dan reputasi platform |

**Skor total:** 24 / 25

**Problem statement versi final (1 paragraf):**
> Ketidakakuratan estimasi waktu kedatangan (ETA) pada layanan ojek online sering menyebabkan ketidakpastian bagi pengguna, di mana selisih waktu aktual di lapangan sering kali jauh lebih lama dibanding prediksi aplikasi. Hal ini disebabkan oleh keterbatasan model prediksi saat ini yang belum secara dinamis mengintegrasikan hambatan lokal seperti durasi lampu merah dan kepadatan di titik putar balik. Penelitian ini bertujuan untuk mengoptimalkan akurasi ETA dengan menambahkan variabel bobot hambatan mikro secara real-time ke dalam algoritma rute guna meminimalkan nilai Mean Absolute Error (MAE) pada sistem navigasi.

---

## Refleksi

> Bandingkan "masalah" yang biasa ditemui saat coding (bug, error) dengan masalah riset. Apa perbedaan fundamental dalam cara mendefinisikan dan mendekati keduanya?

**Jawaban:**
> Perbedaan fundamentalnya adalah pada tujuan dan cakupan. Saat coding dan bertemu bug/error, masalahnya adalah kegagalan sistem untuk berjalan (teknis); pendekatannya adalah perbaikan langsung agar fitur berfungsi kembali. Sedangkan dalam riset, masalahnya adalah gap performa atau ketidakakuratan (sistem sudah jalan, tapi tidak optimal). Pendekatannya adalah pembuktian melalui eksperimen. Sesuai prinsip saya, karena tidak ada akurasi yang mutlak, riset dilakukan bukan untuk mencari "kebenaran sempurna", melainkan untuk menemukan model dengan tingkat ketidakpastian paling kecil berdasarkan data empiris.

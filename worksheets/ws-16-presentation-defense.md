# WS-16: Presentation & Defense (UAS)

> **Bab 16 — Presentasi & Pertahanan Ilmiah**

---

## Ringkasan Materi

### Scientific Defense Model

```
Research Work → Presentation → Questioning → Defense → Evaluation → Acceptance
```

### Presentasi ≠ Ringkasan Paper

| Paper | Presentasi |
|-------|-----------|
| Dibaca (self-paced) | Didengar (presenter-paced) |
| Detail lengkap | Ide kunci + highlight |
| Tabel numerik detail | Grafik visual + angka kunci |
| Pembaca bisa re-read | Audiens dengar sekali |

**Prinsip:** Presentasi membutuhkan **reformulasi**, bukan kompresi. Medium berbeda = pendekatan berbeda.

### Claim-Evidence-Reasoning (CER)

Setiap jawaban defense harus memiliki:
1. **Claim** — Pernyataan yang dijawab
2. **Evidence** — Data/fakta pendukung
3. **Reasoning** — Logika yang menghubungkan evidence ke claim

**Contoh:**
| Pertanyaan | Bad Answer | Good Answer (CER) |
|-----------|-----------|-------------------|
| "Kenapa hanya 3 dataset?" | "Tiga sudah cukup" | "3 dataset mewakili variasi: small-clean, medium-clean, medium-noisy [E]. Generalisasi perlu validasi lanjut — listed as limitation [R]" |
| "Hasil DS-3 menurun?" | "Itu outlier" | "Ya, karena distribusi heavy-tail melanggar asumsi Gaussian [E]. Ini menunjukkan boundary condition metode [R]" |
| "Effect size?" | "p=0.003, jadi signifikan" | "Cohen's d=1.2 (large effect) [E] — bukan hanya signifikan tapi substansial [R]" |

### Slide Design — One Slide, One Message

**Optimal 9-Slide Plan (15 menit):**

| # | Slide | Waktu | Pesan |
|---|-------|-------|-------|
| 1 | Title + context | 1 min | Apa ini tentang apa |
| 2 | Problem + motivation | 2 min | Mengapa penting |
| 3 | Gap + RQ | 1.5 min | Apa yang belum terjawab |
| 4 | Method overview | 2 min | Bagaimana dijawab (diagram) |
| 5 | Key result — tabel | 2 min | Temuan utama |
| 6 | Key result — grafik | 2 min | Pola visual |
| 7 | Interpretation + failure | 2 min | Apa artinya |
| 8 | Limitation + future | 1.5 min | Batasan & arah |
| 9 | Conclusion + contribution | 1 min | Closing message |

### Anticipatory Defense

Prediksi pertanyaan berdasarkan kategori:

| Kategori | Contoh Pertanyaan |
|---------|------------------|
| Problem | "Mengapa masalah ini penting?" |
| Gap | "Bagaimana dengan studi X yang sudah menjawab ini?" |
| Method | "Mengapa metode ini, bukan Y?" |
| Results | "Bagaimana menjelaskan anomali di DS-3?" |
| Generalization | "Apakah bisa diterapkan di domain lain?" |

### Tiga Prinsip Jawaban

1. **Direct** — Jawab dulu, elaborasi kemudian
2. **Data-based** — Tunjuk evidence spesifik
3. **Honest** — Akui limitasi jika memang ada

### Jebakan Kognitif

1. "Presentasi = semua yang ada di paper" → terlalu padat
2. "Slide cantik = presentasi bagus" → konten > estetika
3. "Tidak bisa jawab = gagal" → "I don't know, but..." menunjukkan kejujuran
4. "Tidak perlu latihan — saya paham riset saya" → latihan = menemukan celah

---

## Template A.16 — Defense Preparation Sheet

```
DEFENSE PREPARATION

Slide Deck Plan:
  Total slides   : ____ (target: 10-12 konten + title/closing)
  Time per slide : ~2 min
  Total time     : ____ menit

Slide Outline:
| # | Pesan Utama | Visual | Waktu |
|---|-------------|--------|-------|
| 1 | Title       |        | 30s   |
| 2 | Problem     |        | 2min  |
| 3 | Gap + RQ    |        | 2min  |
| ..|             |        |       |

Anticipatory Defense Matrix:
| Kategori | Pertanyaan Potensial | Jawaban (CER) |
|----------|---------------------|---------------|
| Problem  |                     |               |
| Gap      |                     |               |
| Method   |                     |               |
| Results  |                     |               |
| Generalization |               |               |

Latihan:
  Latihan 1: [tanggal] — [catatan timing & feedback]
  Latihan 2: [tanggal] — [catatan timing & feedback]
  Latihan 3: [tanggal] — [catatan timing & feedback]
```

---

## Latihan 1 — Slide Outline

Rencanakan presentasi 15 menit untuk riset Anda.

| # | Pesan Utama | Visual yang Digunakan | Waktu |
|---|-------------|----------------------|-------|
| 1 | Judul + Konteks: Evaluasi komparatif efisiensi memori browser | *Title slide*, logo Chrome & Firefox | 1 min |
| 2 | Problem: Lag sistem akibat beban kerja *multi-tab* pada memori terbatas | Grafik ilustrasi RAM penuh (*bottleneck*) | 2 min |
| 3 | Gap + RQ: Kurangnya data empiris performa *Memory Saver* vs *Tab Unloading* | Tabel gap literatur arsitektur browser | 1.5 min |
| 4 | Method Overview: Otomatisasi Python, 40 tab statis, jeda 180s, Windows PerfMon | Diagram alur eksekusi (*pipeline*) | 2 min |
| 5 | Key Result (Tabel): Firefox menghemat memori rata-rata ~2.1 GB lebih banyak dari Chrome | Tabel komparasi mean ± std | 2 min |
| 6 | Key Result (Grafik): Pola visual ketimpangan efisiensi yang sangat masif | *Bar chart* dengan *error bar* | 2 min |
| 7 | Interpretation + Failure Analysis: Hipotesis ditolak akibat beban isolasi *sandboxing* Chrome | Diagram arsitektur Chromium vs Gecko | 2 min |
| 8 | Limitation + Future Work: Hanya menguji web statis dan metrik memori absolut (mengabaikan CPU) | *Bullet points* | 1.5 min |
| 9 | Conclusion: Firefox lebih direkomendasikan untuk stabilitas sistem saat beban masif | *Summary highlight* | 1 min |

**Total waktu estimasi:** 15 menit

---

## Latihan 2 — Anticipatory Defense

Prediksi 5 pertanyaan yang mungkin diajukan penguji, lalu siapkan jawaban CER.

| # | Kategori | Pertanyaan | Claim | Evidence | Reasoning |
|---|----------|-----------|-------|----------|-----------|
| 1 | Problem | Mengapa harus menguji skenario ekstrem hingga 40 tab? | Menguji batas operasional (*stress test*) arsitektur. | Pengguna akademisi sering membuka puluhan tab referensi sekaligus. | Pengujian batas ekstrem membongkar kelemahan manajemen memori yang tidak terlihat pada beban ringan. |
| 2 | Method | Mengapa ada jeda waktu konstan 180 detik sebelum pengukuran? | Memberikan *window time* yang adil untuk fitur penghematan. | Dokumentasi resmi fitur mensyaratkan status tab dalam keadaan pasif/*idle*. | Jika diukur langsung saat *loading*, kita hanya merekam beban *rendering*, bukan hasil reduksi memori latar belakang. |
| 3 | Results | Mengapa hipotesis awal Anda bisa salah total? | Limitasi bawaan dari mesin Chromium. | Selisih 2.1 GB meskipun *Memory Saver* aktif. | *Memory Saver* membersihkan *cache*, tapi gagal mematikan overhead proses mandiri (*sandboxing*) dari setiap tab yang terbuka. |
| 4 | Generalization | Apakah kesimpulan ini berlaku untuk sistem operasi Linux atau macOS? | Belum tentu, riset ini spesifik di lingkungan Windows. | Instrumen pengukur menggunakan *Private Bytes* di kernel Windows 11. | OS lain memiliki sistem *swap* atau *zRAM* yang berbeda, sehingga terdaftar sebagai *external validity limitation*. |
| 5 | Method | Mengapa tidak menggunakan ekstensi penghemat RAM pihak ketiga saja? | Menjaga validitas konstruk dan kemurnian variabel bebas. | Eksperimen dilakukan pada mode *vanilla* (tanpa add-on). | Ekstensi pihak ketiga akan memasukkan variabel perancu (*confounder*) yang merusak objektivitas komparasi fitur bawaan. |

---

## Latihan 3 — Simulasi Q&A

Minta teman/kolega mengajukan 3 pertanyaan tentang riset Anda. Catat pertanyaan dan evaluasi jawaban Anda.

| # | Pertanyaan | Jawaban Saya | Evaluasi |
|---|-----------|-------------|---------|
| 1 | Mengapa memilih laptop berspesifikasi RAM 16 GB untuk eksperimen ini? | Laptop dengan RAM 16 GB adalah standar perangkat kelas menengah yang relevan dengan target populasi riset (mahasiswa/pekerja). Ini memastikan efek penghematan RAM terasa nyata secara praktis, tidak seperti pengujian di server berspesifikasi raksasa. | [x] Direct [x] Data-based [x] Honest |
| 2 | Bagaimana Anda yakin bahwa penurunan memori bukan akibat OS yang menutup paksa program? | Saya mengontrol eksperimen ini secara ketat. Selama 80 *runs* berjalan, skrip otomatisasi mendeteksi tidak ada satu pun proses penjelajah web yang mengalami *crash/force close*, dan grafik metrik hanya menunjukkan reduksi bertahap yang terkendali, bukan *drop* ke nol. | [x] Direct [x] Data-based [x] Honest |
| 3 | Mengapa hanya fokus ke RAM, padahal performa laptop juga dipengaruhi CPU? | Benar, ini adalah salah satu limitasi utama riset saya. Saya membatasi cakupan hanya pada metrik memori agar eksperimen tetap *feasible* dan fokus menjawab isu *bottleneck* memori. Analisis beban CPU saat tab dibangunkan (*wake up*) saya rekomendasikan untuk *future work*. | [x] Direct [x] Data-based [x] Honest |

**Pertanyaan yang paling sulit dijawab:**
> Menjelaskan mengapa mengabaikan beban CPU (Pertanyaan 3). Karena dalam realitanya, pelepasan RAM besar-besaran sering kali diimbangi dengan lonjakan kerja prosesor (*processor spike*) saat tab kembali diklik oleh pengguna.

**Apa yang perlu disiapkan lebih baik:**
> Memperdalam penguasaan literatur terkait *trade-off* antara utilisasi Memory vs CPU pada komputasi penjelajah web, sehingga ketika diserang di poin kelemahan konstruk ini, saya bisa merespons dengan landasan teori komputasi yang kuat.

---

## Refleksi

> Dari seluruh proses WS-01 sampai WS-16 — dari paradigma riset hingga presentasi — bagian mana yang paling mengubah cara Anda berpikir tentang riset? Apa satu hal yang akan selalu Anda terapkan di riset berikutnya?

**Insight terbesar:**
> Kegagalan hipotesis sama sekali bukan aib penelitian. Melalui proses *Failure Analysis* (WS-14), saya menyadari bahwa data yang menolak asumsi awal justru menyajikan kontribusi yang jauh lebih jujur dan kritis. Riset bukan ajang pembuktian bahwa "saya benar", melainkan metodologi terstruktur untuk menemukan objektivitas.

**Yang akan selalu diterapkan:**
> Pendekatan *Reproducibility* dan *Data Logging* yang ketat (WS-09 & WS-10). Menyadari betapa rentannya *single run* terhadap bias OS, saya akan selalu membiasakan penggunaan skrip otomatisasi dan *repeated runs* berskala besar pada eksperimen komputasi apapun di masa depan agar hasilnya benar-benar kebal dari anomali sesaat.
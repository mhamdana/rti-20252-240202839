# WS-01: Distorsi & Paradigma

> **Bab 1 — Research Mindset in IT**

---

## Ringkasan Materi

### Research Trust Model

Pengetahuan ilmiah tidak muncul langsung dari kenyataan. Ia melewati **6 tahap transformasi** yang masing-masing rawan distorsi:

```
Reality → Data → Processing → Analysis → Inference → Knowledge
```

Etika mencegah distorsi yang disengaja (fabrikasi, cherry-picking). Validitas mendeteksi distorsi yang tidak disengaja (confounding variable, sampling bias).

### Tiga Jenis Validitas

| Jenis | Pertanyaan | Contoh Ancaman |
|-------|-----------|----------------|
| **Internal Validity** | Apakah hubungan kausal benar ada? | Confounding variable |
| **External Validity** | Apakah bisa digeneralisasi? | Dataset terlalu homogen |
| **Construct Validity** | Apakah mengukur hal yang benar? | Metrik tidak sesuai klaim |

### Paradigma Riset

Mata kuliah ini menggunakan pendekatan **Positivist** (fenomena TI bisa diukur objektif melalui eksperimen terkontrol) diperkuat **Design Science Research** (artefak dibuat sebagai instrumen pengujian hipotesis, bukan tujuan akhir).

### Mode Berpikir Peneliti

**Curious** (mempertanyakan fenomena) → **Critical** (mengevaluasi klaim berdasarkan bukti) → **Systematic** (merancang investigasi terstruktur dan reproducible).

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan | Membuat sistem yang bekerja | Menghasilkan pengetahuan yang valid |
| Pertanyaan khas | "Bagaimana membuatnya jalan?" | "Apakah klaim ini benar?" |
| Ukuran sukses | Sistem berfungsi, client puas | Hipotesis terjawab, temuan tervalidasi |
| Kegagalan | Harus dihindari | Harus dilaporkan (negative result = kontribusi) |

### Istilah Penting

- **Research Mindset** — Pola pikir yang menuntut bukti dan mempertanyakan asumsi
- **Research Ethics** — Prinsip perilaku: kejujuran, objektivitas, keterbukaan, akuntabilitas
- **HARKing** — Hypothesizing After Results are Known — merumuskan hipotesis setelah melihat data
- **Falsifiability** — Hipotesis harus bisa dibuktikan salah

---

## Template A.1 — Research Mindset Self-Assessment

```
Nama Peneliti    : ____________________
Tanggal          : ____________________

1. Ketika membaca klaim "metode X 95% akurat":
   - Pertanyaan pertama saya: ____________________
   - Data yang dibutuhkan untuk verifikasi: ____________________

2. Posisi paradigma:
   - Pendekatan: [ ] Positivis  [ ] Interpretivis  [ ] Design Science  [ ] Mixed
   - Alasan: ____________________

3. Identifikasi distorsi:
   - Asumsi tersembunyi: ____________________
   - Sumber bias potensial: ____________________
   - Langkah mitigasi: ____________________

4. Komitmen etika:
   - Data yang tidak akan dimanipulasi: ____________________
   - Batasan yang diakui sejak awal: ____________________
```

---

## Latihan 1 — Identifikasi Distorsi

Pilih satu paper riset di bidang TI yang mengklaim "metode X meningkatkan performa." Telusuri setiap tahap Research Trust Model.

**Paper yang dipilih:**
> Judul: _Penerapan Algoritma Klasifikasi Naive Bayes dan Support Vector Machine untuk Analisis Sentimen Cyberbullying Bilingual di Aplikasi X.
> Penulis (Tahun): Novita Sari (2025).
> Link: https://repository.uin-suska.ac.id/85934/1/LAPORAN%20REPOSITORY%20NOVITA%20SARI.pdf

| Tahap | Apa yang Dilakukan | Potensi Distorsi |
|-------|-------------------|-----------------|
| Reality → Data | Mengumpulkan data tweet terbaru dari aplikasi X menggunakan teknik crawling dengan kata kunci "Cyberbullying" | Sampling Bias: Hanya mengambil tweet yang mengandung kata kunci spesifik; tweet bullying yang menggunakan bahasa sarkasme tanpa kata kunci tersebut tidak tertangkap |
| Data → Processing | Melakukan pembersihan data (cleaning), penyeragaman huruf (case folding), penghapusan kata umum (stopword), dan stemming | Semantic Distortion: Proses stemming pada bahasa Indonesia seringkali menghilangkan imbuhan penting yang bisa mengubah nada atau makna asli dari sebuah keluhan atau hinaan |
| Processing → Analysis | Menggunakan metode TF-IDF untuk pembobotan kata dan memberikan label sentimen secara otomatis menggunakan library TextBlob | Labeling Bias: Penggunaan library otomatis (TextBlob) untuk bahasa Indonesia sering kurang akurat dibandingkan pelabelan manual karena keterbatasan kamus bahasa gaul/lokal |
| Analysis → Inference | Membandingkan performa akurasi antara algoritma Naive Bayes dan SVM untuk data bilingual | Assumptive Bias: Naive Bayes mengasumsikan setiap kata berdiri sendiri (independen), padahal dalam cyberbullying, urutan kata sangat menentukan apakah itu hinaan atau bukan |
| Inference → Knowledge | Menyimpulkan Naive Bayes lebih unggul (87%) dibanding SVM (86%) untuk klasifikasi sentimen bilingual | Overgeneralization: Klaim keunggulan ini mungkin hanya berlaku pada dataset kecil (502 data Indonesia) dan belum tentu stabil jika diterapkan pada jutaan data real-time |

**Distorsi paling besar di tahap:** Data → Processing.

**Dua distorsi spesifik yang teridentifikasi:**
1. Context Loss (Bilingual): Proses penerjemahan atau pengolahan data bilingual berisiko menghilangkan konteks budaya lokal Indonesia yang sulit diterjemahkan secara harfiah ke model mesin.
2. Algorithm Simplification: Penggunaan Naive Bayes yang "naif" mendistorsi kompleksitas bahasa manusia yang seharusnya saling berkaitan antar kata dalam satu kalimat bullying.

---

## Latihan 2 — Analisis Kasus Etika

Skenario: Seorang peneliti menemukan bahwa jika 3 data point outlier dihapus, hasil eksperimennya menjadi signifikan. Dengan outlier, hasilnya tidak signifikan.

| Perspektif | Analisis |
|------------|---------|
| Kejujuran ilmiah | Peneliti harus tetap melaporkan temuan asli termasuk data outlier tersebut, karena menyembunyikan data demi hasil yang signifikan merupakan bentuk manipulasi informasi |
| Transparansi | Peneliti wajib memaparkan kriteria objektif dalam pembersihan data di bab metodologi sehingga pembaca tahu apakah penghapusan data didasarkan pada kesalahan instrumen atau hanya keinginan subjektif |
| Peer review | Penelaah (reviewer) memerlukan data yang jujur untuk menguji ketangguhan (robustness) metode; jika outlier dihapus tanpa alasan valid, maka validitas temuan tersebut patut dipertanyakan |

**Keputusan akhir dan justifikasi:**
> Keputusan: Peneliti harus melaporkan hasil analisis dalam dua versi (dengan outlier dan tanpa outlier).
Justifikasi: Mengikuti prinsip kejujuran ilmiah, melaporkan kedua kondisi tersebut mencegah terjadinya distorsi pada tahap Analysis dan Inference. Hal ini memberikan gambaran yang jujur kepada pembaca mengenai batasan performa algoritma (Naive Bayes/SVM) ketika menghadapi anomali data, sesuai dengan temuan Novita Sari yang secara transparan melaporkan perbedaan akurasi yang kontras antara data Bahasa Indonesia dan Inggris.

---

## Latihan 3 — Posisi Paradigma

**Topik riset:** Penerapan Algoritma Klasifikasi Naive Bayes dan Support Vector Machine untuk Analisis Sentimen Cyberbullying Bilingual di Aplikasi X.

| Kriteria | Positivis | Interpretivis | Design Science |
|----------|-----------|---------------|----------------|
| Kesesuaian dengan topik (1–5) | 4 | 2 | 5 |
| Jenis data yang dikumpulkan | Data kuantitatif berupa nilai akurasi (87%), precision, dan recall | Pemahaman kontekstual terhadap ulasan teks pengguna | Artefak berupa model sistem klasifikasi sentimen otomatis |
| Limitasi paradigma | Angka statistik tidak bisa menjelaskan motif psikologis pelaku bullying | Sangat sulit untuk mengklasifikasi ribuan data tweet secara manual | Terlalu fokus pada efektivitas alat deteksi daripada solusi sosialnya |

**Paradigma yang dipilih:** Design Science Research
**Alasan:** Riset ini berfokus pada pengembangan sebuah artefak teknologi (model klasifikasi) sebagai solusi praktis untuk mendeteksi cyberbullying. Proses pengembangannya dilakukan melalui tahapan yang sistematis (Gambar 1) dan dievaluasi kinerjanya menggunakan standar objektif.

---

## Refleksi

> Sebelum membaca materi ini, apakah pernah mempertanyakan klaim "95% akurat"? Setelah memahami rantai distorsi, pertanyaan apa yang sekarang akan diajukan saat membaca paper?

**Jawaban:**
> Sebelumnya, saya cenderung skeptis terhadap klaim akurasi tinggi karena hasil tersebut seringkali tidak berlaku umum di setiap situasi. Melalui pemahaman tentang rantai distorsi, saya menyadari bahwa meskipun komputer memiliki presisi tinggi, hasil akhirnya sangat bergantung pada bagaimana data tersebut dipilih dan dimodifikasi pada tahap Processing.
> Setelah memahami rantai distorsi, pertanyaan yang akan saya ajukan saat membaca paper adalah:
> "Bagaimana karakteristik asli data mentah yang digunakan dan di titik mana algoritma ini mengalami kegagalan atau penurunan akurasi?".

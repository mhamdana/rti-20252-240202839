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

| Tahap | Apa yang Dilakukan | Potensi Distorsi |
|-------|-------------------|-----------------|
| Reality → Data | Mengumpulkan data tweet terbaru dari aplikasi X menggunakan teknik crawling dengan kata kunci "Cyberbullying". | Sampling Bias: Hanya mengambil tweet yang mengandung kata kunci spesifik; tweet bullying yang menggunakan bahasa sarkasme tanpa kata kunci tersebut tidak tertangkap. |
| Data → Processing | Melakukan pembersihan data (cleaning), penyeragaman huruf (case folding), penghapusan kata umum (stopword), dan stemming. | Semantic Distortion: Proses stemming pada bahasa Indonesia seringkali menghilangkan imbuhan penting yang bisa mengubah nada atau makna asli dari sebuah keluhan atau hinaan. |
| Processing → Analysis | Menggunakan metode TF-IDF untuk pembobotan kata dan memberikan label sentimen secara otomatis menggunakan library TextBlob. | Labeling Bias: Penggunaan library otomatis (TextBlob) untuk bahasa Indonesia sering kurang akurat dibandingkan pelabelan manual karena keterbatasan kamus bahasa gaul/lokal. |
| Analysis → Inference | Membandingkan performa akurasi antara algoritma Naive Bayes dan SVM untuk data bilingual. | Assumptive Bias: Naive Bayes mengasumsikan setiap kata berdiri sendiri (independen), padahal dalam cyberbullying, urutan kata sangat menentukan apakah itu hinaan atau bukan. |
| Inference → Knowledge | Menyimpulkan Naive Bayes lebih unggul (87%) dibanding SVM (86%) untuk klasifikasi sentimen bilingual. | Overgeneralization: Klaim keunggulan ini mungkin hanya berlaku pada dataset kecil (502 data Indonesia) dan belum tentu stabil jika diterapkan pada jutaan data real-time. |

**Distorsi paling besar di tahap:** Data → Processing.

**Dua distorsi spesifik yang teridentifikasi:**
1. Context Loss (Bilingual): Proses penerjemahan atau pengolahan data bilingual berisiko menghilangkan konteks budaya lokal Indonesia yang sulit diterjemahkan secara harfiah ke model mesin.
2. Algorithm Simplification: Penggunaan Naive Bayes yang "naif" mendistorsi kompleksitas bahasa manusia yang seharusnya saling berkaitan antar kata dalam satu kalimat bullying.

---

## Latihan 2 — Analisis Kasus Etika

Skenario: Seorang peneliti menemukan bahwa jika 3 data point outlier dihapus, hasil eksperimennya menjadi signifikan. Dengan outlier, hasilnya tidak signifikan.

| Perspektif | Analisis |
|------------|---------|
| Kejujuran ilmiah | *Contoh: Laporkan kedua versi (dengan dan tanpa outlier)* |
| Transparansi | |
| Peer review | |

**Keputusan akhir dan justifikasi:**
> ___________________________________________________

---

## Latihan 3 — Posisi Paradigma

**Topik riset:** ________________________________________

| Kriteria | Positivis | Interpretivis | Design Science |
|----------|-----------|---------------|----------------|
| Kesesuaian dengan topik (1–5) | *Contoh: 4* | *Contoh: 2* | *Contoh: 5* |
| Jenis data yang dikumpulkan | | | |
| Limitasi paradigma | | | |

**Paradigma yang dipilih:** _____________________________
**Alasan:** ____________________________________________

---

## Refleksi

> Sebelum membaca materi ini, apakah pernah mempertanyakan klaim "95% akurat"? Setelah memahami rantai distorsi, pertanyaan apa yang sekarang akan diajukan saat membaca paper?

**Jawaban:**
> ___________________________________________________
> ___________________________________________________

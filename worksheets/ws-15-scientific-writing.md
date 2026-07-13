# WS-15: Scientific Writing

> **Bab 15 — Penulisan Ilmiah**

---

## Ringkasan Materi

### Scientific Argument Flow

```
Problem → Gap → RQ → Method → Result → Analysis → Conclusion → Contribution
```

Paper ilmiah adalah **satu argumen utuh** dari masalah ke kontribusi. Setiap node harus terhubung logis ke node sebelum dan sesudahnya.

### Struktur IMRAD

| Section | Peran | Pertanyaan Kunci |
|---------|-------|-----------------|
| **Introduction** | Motivasi + frame | Why is this needed? |
| **Method** | Deskripsi (reproducible) | How was it done? |
| **Results** | Laporan objektif | What was found? |
| **Discussion** | Interpretasi + refleksi | What does it mean? |
| **Conclusion** | Ringkasan + kontribusi | So what? |

### Logical Flow — "Red Thread"

Setiap paragraf menjawab satu pertanyaan dan memicu pertanyaan berikutnya. Alur logis ini harus terasa di tiga level:
1. **Antar-kalimat** dalam paragraf
2. **Antar-paragraf** dalam section
3. **Antar-section** dalam paper

### Internal Consistency

Setiap elemen yang dijanjikan di Introduction harus hadir di Discussion/Conclusion.

**Consistency Matrix:**
```
           Intro  Method  Result  Discuss  Conclude
RQ1          ✓      ✓       ✓       ✓        ✓
RQ2          ✓      ✓       ✓       ✗ ←      ✓
Metrik-X     ✗      ✗       ✓ ←     ✗        ✗
```
**Masalah:** RQ2 dibahas di semua bagian kecuali Discussion. Metrik-X muncul di Result tapi tidak diperkenalkan di Method.

### Writing Quality Triad

| Kualitas | Deskripsi | Contoh Buruk → Baik |
|----------|----------|---------------------|
| **Clarity** | Dipahami sekali baca | "Performa meningkat" → "Accuracy meningkat dari 85.3% ke 89.7%" |
| **Precision** | Istilah eksak, tanpa ambiguitas | "signifikan" → "signifikan secara statistik (p=0.003, d=1.2)" |
| **Conciseness** | Setiap kata menambah informasi | Hapus kalimat redundan, filler words |

### Urutan Penulisan yang Disarankan

1. **Method & Results** — paling stabil, tulis pertama
2. **Discussion** — interpretasi berdasarkan hasil
3. **Introduction** — frame sesuai temuan aktual
4. **Abstract & Conclusion** — terakhir

### Target Jumlah Kata

| Section | Target |
|---------|--------|
| Introduction | 500–700 |
| Related Work | 700–1000 |
| Method | 800–1200 |
| Results | 500–800 |
| Discussion | 600–900 |
| Conclusion | 200–400 |

### Jebakan Kognitif

1. "Lebih panjang = lebih lengkap" → conciseness lebih berharga
2. "Introduction harus ditulis pertama" → justru ditulis terakhir
3. "Jargon teknis = lebih ilmiah" → clarity lebih penting
4. "Discussion = ringkasan Results" → Discussion = interpretasi + konteks

---

## Template A.15 — Paper Structure Checklist

```
PAPER STRUCTURE CHECKLIST

Title   : ____________________
Target  : [ ] Jurnal  [ ] Konferensi  [ ] Laporan

Section Check:
  [ ] Abstract — masalah, metode, hasil utama, kontribusi (max 250 kata)
  [ ] Introduction — konteks → gap → RQ → kontribusi → struktur paper
  [ ] Related Work — concept-centric, gap positioning
  [ ] Method — reproducible: desain, variabel, metrik, setup, prosedur
  [ ] Results — tabel + grafik + observasi (tanpa interpretasi)
  [ ] Discussion — interpretasi, perbandingan, implikasi, limitation
  [ ] Conclusion — jawaban RQ, kontribusi, future work

Consistency Matrix:
  [ ] RQ di Introduction = RQ di Method = RQ di Conclusion
  [ ] Variabel di Method = variabel di Results
  [ ] Klaim di Discussion didukung data di Results
  [ ] Limitasi di Discussion di-address di Conclusion/Future Work

Writing Quality:
  [ ] Clarity — mudah dipahami tanpa re-read
  [ ] Precision — tidak ada istilah ambigu
  [ ] Conciseness — tidak ada kalimat redundan
```

---

## Latihan 1 — Paper Outline

Buat outline paper untuk riset Anda menggunakan struktur IMRAD.

| Section | Konten Utama (2-3 kalimat) | Target Kata |
|---------|---------------------------|------------|
| Abstract | Eksperimen komparatif menguji efisiensi reduksi RAM antara fitur *Memory Saver* Chrome dan *Tab Unloading* Firefox pada skenario beban 40 tab. Hasil pengujian menunjukkan Firefox secara signifikan menghemat kapasitas RAM 2.1 GB lebih besar dibandingkan Chrome. | 200-250 |
| Introduction | Konteks: Lonjakan utilisasi RAM memicu perlambatan sistem pada beban kerja *multi-tab*. Gap: Kurangnya evaluasi empiris independen mengenai efektivitas reduksi memori Chrome berhadapan dengan Firefox. RQ: Apakah *Memory Saver* Chrome membebaskan kapasitas RAM lebih besar dibandingkan Firefox saat menangani 40 tab pasif? | 500-700 |
| Related Work | Kajian arsitektur manajemen memori *Chromium* (*sandboxing* proses isolasi mandiri) berhadapan dengan *Gecko* (*multithreading* terpusat). Pembahasan mekanisme pertukaran data *virtual memory* (*disk swapping*) pada tingkat kernel Windows. | 700-1000 |
| Method | Desain pengujian menggunakan skrip otomatisasi Python untuk memuat 40 URL identik secara serentak di lingkungan Windows 11. Pengukuran absolut *Private Bytes* memori direkam oleh *Windows PerfMon* setelah jeda stabilisasi konstan selama 180 detik. | 800-1200 |
| Results | Google Chrome mencatatkan rata-rata retensi memori pasca-jeda sebesar 5214.3 ± 450.8 MB. Mozilla Firefox mencatatkan retensi memori yang jauh lebih efisien di angka 3045.6 ± 180.5 MB dengan perbedaan signifikan secara statistik (p < 0.001). | 500-800 |
| Discussion | Isolasi proses mandiri pada *Chromium* membatasi efisiensi penghematan RAM secara masif pada batas atas (40 tab). Firefox menahan alokasi memori secara sentralistik sehingga lebih ideal untuk laptop berspesifikasi standar. | 600-900 |
| Conclusion | Hipotesis awal ditolak; Firefox terbukti jauh lebih efisien mereduksi RAM. Kontribusi riset ini membongkar keterbatasan skalabilitas fitur *Memory Saver* Chrome dan menyajikan referensi arsitektur penjelajah web yang objektif. | 200-400 |

---

## Latihan 2 — Consistency Matrix

Buat consistency matrix untuk memverifikasi internal consistency paper Anda.

| | Intro | Method | Result | Discussion | Conclusion |
|--|-------|--------|--------|-----------|-----------|
| RQ1: Efisiensi memori Chrome vs Firefox | ✓ | ✓ | ✓ | ✓ | ✓ |
| Metrik Waktu Eksekusi Pelepasan RAM | ✓ | ~ | ✗ | ✗ | ✗ |
| Metrik Utama: Selisih RAM Terbebas (MB) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Variabel IV: Arsitektur Browser | ✓ | ✓ | ✓ | ✓ | ✓ |
| Variabel DV: Kapasitas Memori | ✓ | ✓ | ✓ | ✓ | ✓ |
| Klaim: Firefox lebih hemat RAM | ✗ | ✗ | ✓ | ✓ | ✓ |

**Isi setiap sel:** ✓ (ada & konsisten), ✗ (missing), ~ (ada tapi inkonsisten)

**Inkonsistensi yang ditemukan:**
> Rancangan metrik waktu (durasi pelepasan RAM dalam detik) sempat tercatat di kerangka awal (Introduction dan Method), namun data ini didrop pada tahap eksekusi karena tertutupi oleh waktu jeda konstan 180 detik dari skrip otomatisasi. Data ini sama sekali absen di bagian Result dan Discussion.

**Tindakan perbaikan:**
> Menghapus seluruh penyebutan variabel metrik waktu/detik dari draf Introduction dan Method untuk menjaga *red thread* tetap konsisten, serta memfokuskan alur argumen murni pada selisih kapasitas absolut RAM (Megabytes).

---

## Latihan 3 — Writing Quality Check

Ambil satu paragraf dari tulisan Anda (atau tulis paragraf baru) dan evaluasi kualitasnya.

**Paragraf asli:**
> Pada pengujian yang dilakukan, Chrome memiliki performa yang kurang baik dibanding Firefox. Memori yang dipakai masih sangat besar setelah ditunggu. Hal ini membuktikan bahwa fitur dari Chrome tidak berhasil menurunkan beban laptop saat buka banyak tab.

| Kriteria | Evaluasi | Perbaikan |
|----------|---------|-----------|
| Clarity | Kalimat pertama ambigu; kata "performa" tidak merujuk pada metrik terukur. | Ubah menjadi perbandingan langsung nilai kapasitas memori pasca-jeda. |
| Precision | Frasa "kurang baik", "sangat besar", dan "setelah ditunggu" tidak eksak dan terlalu kasual. | Cantumkan angka rata-rata MB, parameter waktu 180 detik, dan nilai signifikansi statistik. |
| Conciseness | Kalimat terakhir bertele-tele dan berisi kata *filler*. | Padatkan penjelasan keterkaitan fitur dengan arsitektur penjelajah web. |

**Paragraf setelah perbaikan:**
> Google Chrome mencatat retensi kapasitas RAM pasca-jeda 180 detik sebesar 5214.3 MB, lebih tinggi secara signifikan (p < 0.001) dibandingkan Mozilla Firefox (3045.6 MB). Arsitektur isolasi proses pada Chromium menahan pelepasan memori sistem secara masif, sehingga fitur penghematan bawaan kurang optimal saat menangani skala 40 tab.

---

## Refleksi

> Apa perbedaan antara menulis "tentang" riset dan menulis sebagai "argumen" riset? Bagaimana urutan penulisan (Method → Discussion → Introduction) mengubah kualitas tulisan?

**Jawaban:**
> Menulis "tentang" riset hanya menghasilkan laporan kronologis yang menyerupai buku harian—mencatat apa yang dilakukan dari awal hingga akhir tanpa benang merah yang mengikat. Sebaliknya, menulis sebagai "argumen" berarti menyusun setiap paragraf, data, dan uji statistik secara strategis untuk mendukung atau menyanggah satu klaim sentral yang bermuara pada kontribusi spesifik.
>
> Menerapkan urutan penulisan (Method → Results → Discussion → Introduction) secara drastis mencegah bias kognitif. Dengan mengunci fakta objektif (Method & Results) di awal, interpretasi data di tahap Discussion menjadi lebih murni dan rasional. Introduction kemudian dirakit paling akhir semata-mata untuk membingkai fenomena yang paling relevan dengan temuan aktual, mencegah janji berlebihan di bab pendahuluan yang tidak sanggup dipenuhi oleh data di bab akhir.
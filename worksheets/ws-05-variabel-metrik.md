# WS-05: Variabel & Metrik

> **Bab 5 — Metric, Measurement & Data**

---

## Ringkasan Materi

### Measurement Alignment Model

Setiap pengukuran yang valid harus bisa ditelusuri melalui rantai ini tanpa lompatan logis:

```
Problem → Concept → Variable → Metric → Data → Result
```

### Operationalization = Keputusan Desain

Menerjemahkan konsep abstrak menjadi variabel terukur bukan proses mekanis. "Code quality" yang diukur via SonarQube code smells membawa asumsi implisit. Setiap operasionalisasi harus didokumentasikan dan dijustifikasi.

### Empat Tipe Data (NOIR)

| Tipe | Ciri | Contoh | Operasi Valid |
|------|------|--------|---------------|
| **Nominal** | Kategori, tanpa urutan | Jenis algoritma (RF, SVM, CNN) | Modus, chi-square |
| **Ordinal** | Urutan, interval tidak sama | Skala Likert (1-5) | Median, Spearman |
| **Interval** | Jarak bermakna, tanpa nol absolut | Suhu Celsius | Mean, Pearson, t-test |
| **Ratio** | Jarak bermakna + nol absolut | Waktu eksekusi (ms) | Semua operasi |

Tipe data menentukan uji statistik yang valid. Kebanyakan metrik performa TI = ratio; persepsi pengguna = ordinal.

### Kriteria Pemilihan Metrik

- **Representative** — Mewakili konsep yang diteliti
- **Sensitive** — Cukup peka menangkap perbedaan bermakna (hindari ceiling effect)
- **Feasible** — Bisa dikumpulkan dalam batasan waktu dan biaya

### Pre-registration

Metrik harus ditentukan **sebelum** eksperimen. Memilih metrik setelah melihat data = **p-hacking**. Metrik tambahan yang ditemukan kemudian dilaporkan sebagai *exploratory*, bukan *confirmatory*.

### Primary vs Secondary Metric

- **Primary Metric** — Langsung terikat ke hipotesis, menentukan kesimpulan
- **Secondary Metric** — Pendukung, dilaporkan di samping primary; statusnya suplementer

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Pemilihan metrik | Berdasarkan kebiasaan/tool yang ada | Berdasarkan construct validity |
| Anomali | Dihapus untuk laporan bersih | Diinvestigasi — bisa jadi temuan |
| Kapan dipilih | Setelah sistem jadi (monitoring) | Sebelum eksperimen (by design) |

### Istilah Penting

- **Operationalization** — Transformasi konsep abstrak menjadi variabel terukur
- **Construct Validity** — Sejauh mana pengukuran benar-benar mengukur konsep yang dimaksud
- **Measurement Scale** — Klasifikasi data (NOIR) yang menentukan analisis valid
- **Multi-metric Evaluation** — Menggunakan beberapa metrik untuk menangkap konsep kompleks

---

## Template A.5 — Definisi Variabel, Metrik & Justifikasi

```
VARIABLE & METRIC DEFINITION

Research Question: ____________________

| Variabel | Tipe | Konsep | Metrik | Skala | Satuan | Cara Mengukur | Justifikasi |
|----------|------|--------|--------|-------|--------|---------------|-------------|
|          | IV   |        |        |       |        |               |             |
|          | DV   |        |        |       |        |               |             |
|          | CV   |        |        |       |        |               |             |

Alignment Check:
  RQ → Concept → Variable → Metric → Data → Result
  [ ] Setiap langkah terdokumentasi
  [ ] Tidak ada "lompatan logis"
  [ ] Metrik mengukur apa yang dimaksud (construct validity)
```

---

## Latihan 1 — Operationalization Chain

Gunakan RQ dari WS-04. Definisikan variabel dan metriknya.

**RQ:** Apakah aktivasi fitur *Memory Saver* pada Google Chrome menghasilkan penghematan utilitas memori RAM absolut (MB) yang lebih besar dibandingkan *Tab Unloading* pada Mozilla Firefox ketika dieksekusi menangani 40 tab pasif secara serentak?

| Variabel | Tipe | Konsep Abstrak | Metrik Konkret | Skala (NOIR) | Satuan |
|----------|------|---------------|----------------|-------------|--------|
| Arsitektur Browser | IV | *Memory Engine* | Chromium (*Memory Saver*) vs Gecko (*Tab Unloading*) | Nominal | — |
| Utilitas RAM Sistem | DV | *Memory Footprint* | Rentang alokasi *Private Bytes* pasca-jeda 180 detik | Ratio | Megabytes (MB) |
| Beban Kerja Tab | CV | Stabilitas Tekanan | Pemuatan 40 alamat URL statis kaya media yang identik | Ratio | Unit Tab |
| Durasi Fase Pasif | CV | Jendela Waktu | Batas waktu diam sebelum *counter* dicatat | Ratio | Detik |

**Apakah ada lompatan logis dalam rantai?** [ ] Ya / [x] Tidak
> Jika ya, di mana? Rantai sudah sinkron sepenuhnya dari konsep abstrak (*memory footprint*) menuju variabel terukur yang eksak (*Private Bytes*) melalui perkakas ukur netral di level kernel OS Windows 11.

---

## Latihan 2 — Evaluasi Metrik

Evaluasi metrik DV yang dipilih di Latihan 1 menggunakan 3 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Representative | 5 | *Private Bytes* sangat mewakili kapasitas RAM murni yang dialokasikan khusus oleh sistem operasi untuk sub-proses *browser*, bebas dari bias *shared memory*. |
| Sensitive | 5 | Peka menangkap fluktuasi pelepasan ruang memori hingga tingkat desimal terkecil (Kilobytes), meminimalkan risiko terjadinya *ceiling effect*. |
| Feasible | 5 | Sangat mudah diekstraksi secara terprogram dan berkala melalui jembatan performa *counter* Windows PerfMon ke dalam format berkas log. |

**Apakah perlu secondary metric?** [x] Ya / [ ] Tidak
> Jika ya, apa dan mengapa? *Page File Bytes* (Utilisasi *Virtual Memory*). Karena penurunan drastis pada RAM fisik (*Private Bytes*) bisa jadi menipu jika sistem ternyata mengalihkan beban memori tersebut ke media penyimpanan lokal (*disk swapping*). Metrik sekunder ini diperlukan untuk memastikan pelepasan RAM benar-benar murni berupa efisiensi, bukan kompresi paksa.

**Contoh kasus ceiling effect untuk metrik ini:**
> Jika laptop yang digunakan memiliki RAM fisik yang sangat longgar (misalnya 64 GB) dan beban 40 tab hanya memakan <10% kapasitas, fitur penghemat memori dari kedua browser mungkin tidak akan menunjukkan perbedaan penurunan yang radikal karena tekanan *resource* belum menyentuh batas kritis sistem.

---

## Latihan 3 — Data Quality Check

Bayangkan data yang akan dikumpulkan dari eksperimen. Evaluasi 4 dimensi kualitas data.

| Dimensi | Pertanyaan | Jawaban | Strategi Mitigasi |
|---------|-----------|---------|------------------|
| Completeness | *Apakah semua data point terkumpul?* | Ada risiko skrip otomatisasi terhenti (*hang*) di tengah iterasi akibat kehabisan memori. | Mengonfigurasi skrip dengan mekanisme *error-handling* ketat untuk mendeteksi *crash*, mencatat titik kegagalan, dan melakukan *restart session*. |
| Consistency | *Apakah ada kontradiksi internal?* | Nilai RAM awal terbaca lebih rendah dari nilai RAM pasca-pembebasan pada *run* tertentu. | Menerapkan waktu pendinginan (*cooldown interval*) selama 60 detik antar-run agar kondisi alokasi memori OS kembali ke status *baseline* yang bersih. |
| Validity | *Apakah benar-benar mengukur yang dimaksud?* | Metrik RAM terdistorsi oleh aktivitas sub-proses eksternal OS host yang berjalan acak. | Menutup seluruh aplikasi non-esensial (*background apps*) secara total dan mematikan fitur *Windows Update* selama jendela pengujian berlangsung. |
| Representativeness | *Apakah sampel mewakili populasi target?* | Karakteristik beban 40 tab hanya mewakili situs statis, bukan aplikasi web dinamis yang berat. | Melakukan stratifikasi pemilihan 40 URL agar mencakup kombinasi seimbang antara situs berita, portal media kaya gambar, dan dokumen statis. |

---

## Refleksi

> Mengapa memilih metrik setelah melihat data dianggap p-hacking? Apa bedanya dengan eksplorasi data yang sah?

**Jawaban:**
> Memilih metrik setelah melihat data dikategorikan sebagai *p-hacking* karena membuka celah bagi peneliti untuk bertindak tidak jujur dengan cara "menggeser gawang" pengukuran. Peneliti dapat secara selektif memilah metrik mana saja yang secara kebetulan memunculkan nilai signifikansi statistik (*p-value* < 0.05) untuk memaksakan pembenaran hipotesisnya, sementara metrik yang menggagalkan hipotesis disembunyikan.
> 
> Perbedaan mendasar dengan eksplorasi data yang sah terletak pada tujuannya. Eksplorasi data bersifat terbuka (*exploratory*) dan dilakukan di awal untuk mengenali karakteristik data, memetakan anomali, serta merumuskan hipotesis baru tanpa menarik klaim final. Sementara itu, dalam pengujian hipotesis (*confirmatory*), metrik wajib dikunci sejak awal melalui desain eksperimen agar proses penarikan kesimpulan ilmiah berjalan objektif dan bebas dari bias konfirmasi.
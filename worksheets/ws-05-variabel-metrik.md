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

**RQ:** Apakah integrasi fitur hambatan mikro meningkatkan akurasi ETA pada model XGBoost?

| Variabel | Tipe | Konsep Abstrak | Metrik Konkret | Skala (NOIR) | Satuan |
|----------|------|---------------|----------------|-------------|--------|
| Algoritma | IV | Model Prediktif | XGBoost Standar vs XGBoost + Mikro | Nominal | — |
| Densitas Hambatan| IV | Intensitas gangguan | Jumlah titik lampu merah per Km | Ratio| Titik/Km|
| Akurasi ETA | DV | Error estimasi | MAPE | Ratio| % |
| Waktu Aktual | CV | Realitas durasi | Total detik perjalanan | Ratio | Detik |
 
**Apakah ada lompatan logis dalam rantai?** [ ] Ya / [x] Tidak
> Jika ya, di mana? Rantai sudah sinkron dari konsep abstrak (gangguan) ke hitungan konkret (jumlah titik/Km).

---

## Latihan 2 — Evaluasi Metrik

Evaluasi metrik DV yang dipilih di Latihan 1 menggunakan 3 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Representative | 5 | Sangat mewakili karena dalam transportasi, selisih 2 menit pada rute 10 menit lebih fatal dibanding rute 60 menit. |
| Sensitive |4 | Peka terhadap perubahan kecil di level detik, namun bisa terdistorsi jika data aktual sangat kecil (mendekati nol).|
| Feasible | 5 | Data waktu aktual tersedia di log GPS dan prediksi keluar dari model XGBoost; kalkulasi sangat mudah. |

**Apakah perlu secondary metric?** [x] Ya / [ ] Tidak
> Jika ya, apa dan mengapa? RMSE (Root Mean Square Error). Karena MAPE tidak memberikan penalti besar pada outlier, RMSE diperlukan untuk mendeteksi jika ada error prediksi yang sangat ekstrem (misal: prediksi 10 menit tapi aslinya 40 menit).

**Contoh kasus ceiling effect untuk metrik ini:**
> Jika model sudah sangat akurat (error < 1%), penambahan fitur hambatan mikro mungkin tidak akan menunjukkan penurunan error lagi karena sudah mencapai batas limit akurasi data GPS itu sendiri.

---

## Latihan 3 — Data Quality Check

Bayangkan data yang akan dikumpulkan dari eksperimen. Evaluasi 4 dimensi kualitas data.

| Dimensi | Pertanyaan | Jawaban | Strategi Mitigasi |
|---------|-----------|---------|------------------|
| Completeness | *Apakah semua data point terkumpul?* | Ada risiko signal loss di area gedung tinggi (urban canyon). | Interpolasi titik koordinat yang hilang atau eliminasi perjalanan dengan gap > 30 detik. |
| Consistency | *Apakah ada kontradiksi internal?* | Koordinat GPS melompat sehingga kecepatan terbaca tidak masuk akal. | Filtering data dengan ambang batas kecepatan maksimal ojek (misal: 80-100 km/jam). |
| Validity | *Apakah benar-benar mengukur yang dimaksud?* | Data lampu merah di OSM mungkin tidak mencakup semua titik terbaru. | Sampling acak 10-20 titik menggunakan Google Street View untuk validasi keberadaan fisik hambatan. |
| Representativeness | *Apakah sampel mewakili populasi target?* | Dataset mungkin didominasi perjalanan siang hari saja. | Melakukan stratifikasi pengambilan data agar mencakup jam sibuk (rush hour) dan jam sepi. |

---

## Refleksi

> Mengapa memilih metrik setelah melihat data dianggap p-hacking? Apa bedanya dengan eksplorasi data yang sah?

**Jawaban:**
> Memilih metrik setelah melihat data dianggap p-hacking karena peneliti bisa secara selektif memilih metrik yang secara kebetulan memberikan hasil signifikan (p-value rendah) untuk mendukung hipotesisnya, padahal itu mungkin hanya kebetulan statistik (noise). Ini mencederai integritas riset karena kesimpulan tidak lagi objektif.
> Perbedaannya dengan eksplorasi data yang sah adalah tujuannya. Eksplorasi dilakukan di awal untuk memahami pola dan mencari anomali tanpa menarik kesimpulan final (hipotesis dibentuk di sini). Sedangkan dalam pengujian hipotesis (confirmatory), metrik harus dikunci di awal agar peneliti tidak bisa "menggeser gawang" untuk mendapatkan skor gol.

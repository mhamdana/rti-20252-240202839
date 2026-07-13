# WS-03: Literature Mapping & Gap

> **Bab 3 — Literature Review, Research Gap & Baseline**

---

## Ringkasan Materi

### Literature Review = Positioning, Bukan Ringkasan

Literature review bukan merangkum paper satu per satu. Pendekatan yang benar adalah **concept-centric** — organisasi berdasarkan tema, metode, atau variabel. Tujuan: menemukan **pola, kontradiksi, dan gap**.

**Perbandingan pendekatan Author-centric vs Concept-centric:**

| Aspek | Author-centric (Hindari) | Concept-centric (Gunakan) |
|-------|--------------------------|---------------------------|
| Struktur | Per penulis/paper ("Rahman et al. menyatakan...") | Per konsep/metode ("Pendekatan berbasis transformer") |
| Tujuan | Ringkasan isi paper | Perbandingan metode & identifikasi gap |
| Contoh paragraph | "Rahman (2023) pakai CNN. Lee (2022) pakai LSTM. Zhang (2021) pakai RF." | "Tiga pendekatan dominan: CNN digunakan oleh 4 paper untuk representasi fitur visual; LSTM untuk data sekuensial; RF sebagai baseline klasik." |
| Hasil akhir | Daftar paper | Peta pengetahuan + gap yang teridentifikasi |

### Empat Jenis Research Gap

| Jenis Gap | Deskripsi | Contoh |
|-----------|----------|--------|
| **Performance Gap** | Performa belum memadai | Akurasi deteksi hanya 78% pada kasus tertentu |
| **Method Gap** | Pendekatan belum diterapkan | Belum ada yang pakai transformer untuk task ini |
| **Data Gap** | Dataset terbatas/tidak representatif | Semua studi pakai dataset sintetis |
| **Context Gap** | Belum diuji pada konteks berbeda | Belum ada evaluasi di negara berkembang |

Gap terkuat = kombinasi 2+ jenis.

### Systematic Search Strategy

1. **Database utama**: IEEE Xplore, ACM DL, Scopus
   - Akses IEEE/ACM melalui jaringan kampus atau VPN institusi
   - Alternatif bebas biaya: Google Scholar, ResearchGate ([researchgate.net](https://www.researchgate.net)), arXiv ([arxiv.org](https://arxiv.org))
2. **Boolean query** yang terdokumentasi eksplisit
   - Contoh: `("anomaly detection" OR "intrusion detection") AND ("deep learning" OR "neural network") NOT ("medical imaging")`
   - Gunakan tanda kutip untuk frasa eksak; AND/OR/NOT mengontrol scope
3. **Snowballing** — dua arah:
   - **Backward snowballing**: buka daftar referensi di paper kunci → telusuri paper yang dikutip
   - **Forward snowballing**: di Google Scholar, klik "Cited by" di bawah paper kunci → temukan paper yang mengutipnya
   - Ulangi 1–2 tingkat untuk membangun cakupan komprehensif
4. Klaim "belum ada penelitian" harus didukung **bukti pencarian**

### Baseline Selection — 3 Kriteria

| Kriteria | Pertanyaan |
|----------|-----------|
| **Relevan** | Apakah menyelesaikan masalah yang sama? |
| **Representatif** | Apakah mewakili common practice? |
| **State-of-the-Art** | Apakah terbaru/terbaik? |

Membandingkan deep learning 2024 dengan decision tree sederhana tanpa justifikasi = **straw man comparison** (perbandingan tidak jujur).

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan baca literatur | Mencari solusi yang sudah ada | Memahami apa yang belum terjawab |
| Cara membaca paper | Tutorial, how-to | Metode, limitasi, gap |
| Baseline | Framework terpopuler | State-of-the-art yang rigorous |
| Dokumentasi pencarian | Tidak diperlukan | Wajib (reproducible) |

### Istilah Penting

- **Concept-centric** — Organisasi literatur berdasarkan konsep/metode, bukan per penulis
- **Snowballing** — Backward (telusuri referensi) + Forward (cari yang mengutip paper kunci)
- **Research Position** — Pernyataan eksplisit posisi riset terhadap studi sebelumnya
- **Straw man comparison** — Memilih baseline lemah agar metode sendiri terlihat lebih baik

---

## Template A.3 — Literature Mapping & Gap Identification

```
LITERATURE MAPPING

Topik      : ____________________
Database   : ____________________
Query      : ____________________
Tahun      : ____________________
Hasil awal : ____ paper → Screening → ____ paper final

Literature Matrix (concept-centric):

| Study | Tahun | Method | Data | Result | Limitation |
|-------|-------|--------|------|--------|------------|
|       |       |        |      |        |            |

Pola yang ditemukan:
  Metode dominan     : ____________________
  Dataset umum       : ____________________
  Limitasi berulang  : ____________________

GAP IDENTIFICATION

Gap 1: [Jenis: performance / method / data / context]
  Deskripsi    : ____________________
  Bukti        : ____________________
  Signifikansi : ____________________

Gap 2: [Jenis: ____]
  Deskripsi    : ____________________
  Bukti        : ____________________
  Signifikansi : ____________________

Baseline Selection:
| Baseline | Relevansi | Representatif | Source |
|----------|-----------|---------------|--------|
|          |           |               |        |
```

---

## Latihan 1 — Concept-Centric Literature Table

Gunakan topik riset dari WS-02. Cari minimal 5 paper relevan menggunakan database akademik.

**Topik riset:** Optimasi Akurasi ETA Ojek Online melalui Integrasi Hambatan Mikro (Lampu Merah & Putar Balik) di Indonesia.
**Query pencarian:** `("ETA prediction" OR "travel time estimation") AND ("machine learning" OR "XGBoost") AND ("traffic delay" OR "intersection")`
**Database:** Google Scholar

| # | Study | Tahun | Method | Dataset | Result | Limitasi |
|---|-------|-------|--------|---------|--------|----------|
| 1 | *Ahmad Fauzi* | 2024 | Random Forest & XGBoost | Data rute ojek online lokal (Jakarta) | Metode ensemble mampu memprediksi tren makro perjalanan secara efisien. | Belum mendalami variabel hambatan mikro spesifik seperti durasi lampu merah dan antrean *U-turn*. |
| 2 | *Raja Joko Musridho* | 2025 | Dijkstra vs Google Maps API | Log perjalanan rute nyata di Pekanbaru | Navigasi komersial jauh lebih adaptif terhadap dinamika kemacetan dibanding graf statis. | Mekanisme pembobotan penalti waktu internal bersifat tertutup (*black-box*). |
| 3 | *ByeoungDo Kim (PAtt)* | 2026 | Pattern Attention Network | 294 Juta log GPS perjalanan (Korea Selatan) | Model berhasil mencapai nilai MAPE 8.78% dalam menangkap profil kecepatan spasio-temporal. | Fokus pada pola kecepatan berkendara makro, bukan pada interupsi statis di titik putar balik. |
| 4 | *Sanjaya & Supangkat* | 2020 | Predictive Analytics | Data log operasional keterlambatan transportasi | Model sukses memetakan klasifikasi keterlambatan berdasarkan riwayat insiden eksternal. | Karakteristik jalur rel tunggal yang linier tidak sekompleks dinamika jalan raya perkotaan. |
| 5 | *Riskiyah et al.* | 2024 | Extreme Learning Machine | Kumpulan teks ulasan ulasan kepuasan pengguna | Validasi menunjukkan kesalahan nilai ETA adalah pemicu utama sentimen negatif konsumen. | Berfokus pada analisis opini pasca-perjalanan, bukan pada optimasi rute waktu nyata (*real-time*). |

**Pola yang terlihat — Metode dominan:** Penggunaan algoritma *ensemble* (*XGBoost*/*Random Forest*) untuk data tabular dan penerapan mekanisme *Attention* untuk menangkap dependensi spasio-temporal sekuensial perjalanan.
**Limitasi yang berulang:** Keterbatasan model dalam menangkap dinamika hambatan non-linier pada titik mikro (seperti waktu tunggu lampu merah yang tidak sinkron dan antrean *U-turn*), yang sering memicu deviasi tinggi pada estimasi akhir.

---

## Latihan 2 — Gap Identification

Berdasarkan tabel di Latihan 1, identifikasi gap.

| Jenis Gap | Ditemukan? | Gap Statement |
|-----------|-----------|---------------|
| Performance Gap | [x] Ya / [ ] Tidak | Akurasi prediksi sering meleset karena model cenderung melakukan perataan (*smoothing*) data, sehingga gagal mendeteksi lonjakan durasi radikal di lampu merah. |
| Method Gap | [x] Ya / [ ] Tidak | Belum ada integrasi variabel "bobot hambatan mikro" secara dinamis dalam algoritma rute terbuka (*open-source*) untuk konteks jalanan lokal. |
| Data Gap | [ ] Ya / [x] Tidak | Data perjalanan (*GPS logs*) sudah tersedia melimpah, namun pemanfaatannya untuk pemodelan hambatan mikro masih terbatas. |
| Context Gap | [x] Ya / [ ] Tidak | Model mutakhir (SOTA) sering diuji di tata kota teratur; hambatan unik Indonesia (titik balik padat dan persimpangan tak sebidang) belum terakomodasi secara eksplisit. |

**Gap utama yang dipilih:** Kombinasi Method dan Context Gap.
**Mengapa gap ini penting (bukan sekadar "belum ada yang meneliti")?**
> Karena ketidakakuratan prediksi waktu akibat kegagalan menangkap interupsi mikro berdampak langsung pada penurunan performa alokasi armada penjemputan dan kepuasan pelanggan ojek online. Model navigasi generalis yang ada saat ini tidak menyediakan parameter terbuka untuk memodelkan karakteristik jalanan lokal Indonesia yang sarat dengan titik hambatan mikro non-stokastik.

---

## Latihan 3 — Baseline Selection

Pilih 2 baseline dari literatur yang sudah dibaca.

| # | Baseline | Mengapa Relevan | Mengapa Representatif | Apakah SOTA? | Sumber |
|---|----------|----------------|----------------------|-------------|--------|
| 1 | XGBoost Regressor | Algoritma standar industri untuk pemodelan regresi data tabular perjalanan ojek online. | Mewakili arsitektur *Machine Learning* non-deep learning yang paling sering diimplementasikan pada data transportasi. | Ya (Tabular SOTA). | *Ahmad Fauzi (2024)* |
| 2 | Google Maps API (ETA Output) | Menjadi benchmark utama navigasi real-time yang digunakan mayoritas platform ojek online saat ini. | Menjadi standar emas navigasi yang dirasakan langsung oleh pengguna harian di lapangan. | Ya (Industry SOTA). | *Musridho et al. (2025)* |

**Apakah pemilihan baseline ini bisa dianggap straw man?** [ ] Ya / [x] Tidak
> Justifikasi: Perbandingan dilakukan langsung dengan algoritma *ensemble* tingkat tinggi yang sangat rigorus (*XGBoost*) serta pemimpin pasar navigasi global (*Google Maps*), bukan membandingkannya dengan metode statistik sederhana (seperti *Linear Regression* default) yang sengaja dilemahkan.

---

## Refleksi

> Apa perbedaan antara "belum ada yang meneliti ini" (klaim tanpa bukti) dengan research gap yang valid? Bagaimana cara membuktikan bahwa sebuah gap benar-benar ada?

**Jawaban:**
> Perbedaan mendasar terletak pada landasan pembuktian empirisnya. Klaim "belum ada yang meneliti" hanyalah tebakan subjektif tanpa riset pustaka yang matang. Sebaliknya, *research gap* yang valid dibangun di atas analisis kritis terhadap keterbatasan operasional (*boundary conditions*) yang secara eksplisit diakui dalam laporan-laporan ilmiah peneliti terdahulu.
> 
> Cara membuktikannya adalah dengan mendokumentasikan strategi pencarian sistematis secara transparan—meliputi pendefinisian batas pencarian (*Boolean query*), penentuan basis data (seperti *Google Scholar*), hingga pelacakan rujukan dua arah (*backward and forward snowballing*). Melalui *literature matrix* yang terstruktur, kita bisa memperlihatkan secara objektif bagian spesifik mana dari sistem atau konteks yang belum pernah diselesaikan oleh teknologi saat ini.
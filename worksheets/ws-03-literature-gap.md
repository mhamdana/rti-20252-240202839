# WS-03: Literature Mapping & Gap

> **Bab 3 — Literature Review, Research Gap & Baseline**

---

## Ringkasan Materi

### Literature Review = Positioning, Bukan Ringkasan

Literature review bukan merangkum paper satu per satu. Pendekatan yang benar adalah **concept-centric** — organisasi berdasarkan tema, metode, atau variabel. Tujuan: menemukan **pola, kontradiksi, dan gap**.

### Empat Jenis Research Gap

| Jenis Gap | Deskripsi | Contoh |
|-----------|----------|--------|
| **Performance Gap** | Performa belum memadai | Akurasi deteksi hanya 78% pada kasus tertentu |
| **Method Gap** | Pendekatan belum diterapkan | Belum ada yang pakai transformer untuk task ini |
| **Data Gap** | Dataset terbatas/tidak representatif | Semua studi pakai dataset sintetis |
| **Context Gap** | Belum diuji pada konteks berbeda | Belum ada evaluasi di negara berkembang |

Gap terkuat = kombinasi 2+ jenis.

### Systematic Search Strategy

1. **Database**: IEEE Xplore, ACM DL, Scopus, Google Scholar
2. **Boolean query** yang terdokumentasi eksplisit
3. **Snowballing**: backward (telusuri referensi) + forward (cari yang mengutip)
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

Gunakan topik riset dari WS-02. Cari minimal 5 paper relevan menggunakan Google Scholar atau database lain.

**Topik riset:** Optimasi Akurasi ETA Ojek Online melalui Integrasi Hambatan Mikro (Lampu Merah & Putar Balik) di Indonesia.
**Query pencarian:** ETA Prediction Indonesia, Machine Learning Transportasi Online, Traffic Delay Micro-obstacles.
**Database:** Google Scholar

| # | Study | Tahun | Method | Dataset | Result | Limitasi |
|---|-------|-------|--------|---------|--------|----------|
| 1 | *Ahmad Fauzi* | *2024* | *Random Forest & XGBoost* | *Data Gojek, Grab, Blue Bird* | *ML berkontribusi signifikan dalam memprediksi permintaan & rute* | *Belum mendalami variabel hambatan mikro spesifik seperti lampu merah.* |
| 2 | *Raja Joko Musridho* | *2025* | *Dijkstra vs Google Maps API* | *Rute nyata di Pekanbaru* | *Google Maps lebih adaptif terhadap lalu lintas dinamis dibanding Dijkstra* | *Mekanisme internal penentuan bobot Google Maps bersifat tertutup (black-box).* |
| 3 | *ByeoungDo Kim (PAtt)* | *2026* | *Pattern Attention Network* | *294 Juta rute (South Korea)* | *Korea) 

MAPE 8.78%, unggul dalam menangkap profil kecepatan historis* | *Fokus pada pola kecepatan makro, bukan hambatan statis di titik balik.* |
| 4 | *Sanjaya & Supangkat* | *2020* | *Predictive Analytics* | *Data keterlambatan PT. KAI* | *Berhasil memprediksi waktu keterlambatan berdasarkan penyebabnya* | *waktu keterlambatan berdasarkan penyebabnya 

Karakteristik jalur rel tunggal tidak sekompleks lalu lintas jalan raya.* |
| 5 | *Riskiyah et al.* | *2024* | *Extreme Learning Machine* | *Review kepuasan Gojek* | *Keterlambatan menjadi faktor utama ketidakpuasan pengguna* | *Fokus pada analisis sentimen, bukan optimasi rute waktu nyata.* |

**Pola yang terlihat — Metode dominan:** Penggunaan algoritma ensemble (XGBoost/RF) dan mekanisme Attention untuk memproses data sekuensial perjalanan.
**Limitasi yang berulang:** Kesulitan menangkap dinamika hambatan di titik mikro (lampu merah/U-turn) yang sering menyebabkan selisih waktu aktual jauh lebih lama dibanding prediksi aplikasi.

---

## Latihan 2 — Gap Identification

Berdasarkan tabel di Latihan 1, identifikasi gap.

| Jenis Gap | Ditemukan? | Gap Statement |
|-----------|-----------|---------------|
| Performance Gap | [v] Ya / [ ] Tidak | Akurasi prediksi sering meleset karena model cenderung melakukan perataan (smoothing) data, sehingga gagal mendeteksi lonjakan durasi di lampu merah. |
| Method Gap | [v] Ya / [ ] Tidak | Belum ada integrasi variabel "bobot hambatan mikro" secara dinamis dalam algoritma rute terbuka (open-source) untuk konteks jalanan lokal Indonesia. |
| Data Gap | [ ] Ya / [v] Tidak | Data perjalanan (GPS logs) sudah tersedia melimpah, namun pemanfaatannya untuk fitur hambatan mikro masih terbatas. |
| Context Gap | [v] Ya / [ ] Tidak | Model mutakhir (SOTA) sering diuji di tata kota teratur; hambatan unik Indonesia (titik balik padat) belum terakomodasi secara eksplisit dalam algoritma. |

**Gap utama yang dipilih:** Kombinasi Method dan Context Gap.
**Mengapa gap ini penting (bukan sekadar "belum ada yang meneliti")?**
> Karena ketidakakuratan prediksi waktu akibat hambatan mikro berdampak langsung pada kepuasan pelanggan dan efisiensi pengemudi , yang selama ini belum teratasi sepenuhnya oleh model navigasi generalis yang ada.

---

## Latihan 3 — Baseline Selection

Pilih 2 baseline dari literatur yang sudah dibaca.

| # | Baseline | Mengapa Relevan | Mengapa Representatif | Apakah SOTA? | Sumber |
|---|----------|----------------|----------------------|-------------|--------|
| 1 | XGBoost Regressor | Digunakan luas untuk prediksi durasi perjalanan ojek online. | Mewakili model ML tabular yang umum digunakan dalam riset transportasi lokal. | Ya (Machine Learning). | Ahmad Fauzi (2024) |
| 2 | Google Maps API | Benchmark navigasi real-time yang digunakan mayoritas platform ojek online. | Menjadi standar emas navigasi yang dirasakan langsung oleh pengguna. | Ya (Industry SOTA). | Musridho et al. (2025) |

**Apakah pemilihan baseline ini bisa dianggap straw man?** [ ] Ya / [v] Tidak
> Justifikasi: Perbandingan dilakukan dengan algoritma ML yang rigorus (XGBoost) dan pemimpin pasar (Google Maps), bukan dengan algoritma statis yang sengaja dibuat lemah.

---

## Refleksi

> Apa perbedaan antara "belum ada yang meneliti ini" (klaim tanpa bukti) dengan research gap yang valid? Bagaimana cara membuktikan bahwa sebuah gap benar-benar ada?

**Jawaban:**
> Perbedaan antara klaim "belum ada yang meneliti" dengan research gap yang valid terletak pada bukti pencarian. Klaim tanpa bukti hanyalah asumsi, sedangkan research gap valid didasarkan pada pemetaan literatur yang menunjukkan limitasi nyata dari peneliti terdahulu.
> Cara membuktikannya adalah melalui strategi pencarian sistematis—mendokumentasikan basis data, query, hingga teknik snowballing—untuk memastikan bahwa "kekosongan" tersebut memang belum dijawab oleh riset lain hingga saat ini.

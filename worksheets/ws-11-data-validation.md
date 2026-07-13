# WS-11: Data Validation & Integrity

> **Bab 11 — Validasi Data & Integritas**

---

## Ringkasan Materi

### Data Trust Model

```
Raw Data → Data Cleaning → Consistency Check → Validation Process → Trusted Data
```

Data mentah belum bisa dipercaya. Harus melewati pipeline validasi sebelum siap untuk analisis statistik.

### Empat Pilar Data Quality

| Pilar | Deskripsi | Contoh Pelanggaran |
|-------|----------|-------------------|
| **Accuracy** | Nilai dalam range masuk akal | Akurasi = 1.5 (di luar [0,1]) |
| **Consistency** | Format seragam di semua run | Run 1: CSV, Run 2: JSON |
| **Completeness** | Tidak ada data hilang dari plan | 97 dari 100 run tercatat |
| **Validity** | Data sesuai desain eksperimen | Parameter baseline tercampur treatment |

### Proses Validasi Progresif

1. **Format validation** — Tipe file, header, kolom
2. **Range validation** — Nilai dalam batas logis
3. **Consistency validation** — Format seragam antar-run
4. **Logic validation** — Data cocok dengan desain eksperimen

Jika gagal di langkah awal → tidak perlu lanjut.

### Anomaly Detection — 3 Jenis

| Jenis | Deskripsi | Deteksi |
|-------|----------|---------|
| **Statistical outlier** | Nilai di luar distribusi normal | IQR: < Q1-1.5×IQR atau > Q3+1.5×IQR |
| **Contextual anomaly** | Normal absolut, abnormal dalam konteks | Run 1-10: ~91%, Run 11-20: ~88% |
| **Pattern anomaly** | Pola sistematis (bukan random) | Performa menurun berurutan |

**Prinsip:** Detect → Investigate → Document → Decide — **JANGAN langsung hapus.**

### Engineering vs Research Validation

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan | Data sesuai spesifikasi bisnis | Data layak untuk analisis statistik |
| Missing data | Impute / set default | Investigasi penyebab → dokumentasi |
| Outlier | Bug → fix | Mungkin temuan → investigasi |
| Dokumentasi | Minimal (log error) | Komprehensif (anomali + keputusan) |

### Jebakan Kognitif

1. "Logging otomatis ≠ data benar" → bisa ada bug di logger
2. "Outlier = hapus" → bisa jadi temuan penting
3. "Dataset kecil tidak perlu validasi" → justru lebih rentan
4. "Mean normal = data benar" → [94, 95, 93, **44**, 94] → mean 84% terlihat wajar

---

## Template A.11 — Data Validation Checklist

```
DATA VALIDATION CHECKLIST

Completeness:
  [ ] Semua skenario tercakup
  [ ] Jumlah run sesuai rencana
  [ ] Tidak ada file output hilang
  Missing: ____ dari ____ data points

Format Consistency:
  [ ] Semua file format sama (CSV/JSON/...)
  [ ] Header konsisten
  [ ] Tipe data konsisten (numerik tetap numerik)

Range & Logic:
  [ ] Nilai dalam range masuk akal
  [ ] Tidak ada waktu negatif
  [ ] Metrik 0–100%, tidak di luar range
  Anomali ditemukan: ____________________

Cross-Validation:
  [ ] Run identik → hasil mendekati
  [ ] Trend konsisten dengan ekspektasi teori

Keputusan:
  [ ] Data siap analisis
  [ ] Perlu cleaning
  [ ] Perlu re-run (skenario: ____)
```

---

## Latihan 1 — Completeness Check

Verifikasi apakah semua data yang direncanakan sudah terkumpul.

| Skenario | Run Direncanakan | Run Tercatat | Missing | Alasan |
|----------|-----------------|-------------|---------|--------|
| *Google Chrome (Intervensi)* | *40* | *40* | *0* | *-* |
| *Mozilla Firefox (Baseline)* | *40* | *40* | *0* | *-* |

**Total expected:** 80 | **Total actual:** 80 | **Missing:** 0

**Keputusan untuk data missing:**
> Keseluruhan siklus perekaman berhasil diselesaikan oleh skrip otomatisasi tanpa ada iterasi yang terlewat. Data siap untuk dilanjutkan ke tahap pengecekan anomali (range validation).

---

## Latihan 2 — Anomaly Investigation

Periksa data Anda untuk anomali. Gunakan metode IQR atau z-score.

**Dataset sampel (Kapasitas RAM Terpakai Chrome Pasca 180s dalam MB):**

| Run | Kapasitas RAM (MB) |
|-----|-------------|
| 1 | 5745.04 |
| 2 | 5786.70 |
| 3 | 4764.92 |
| 4 | 5514.00 |
| 5 | 2100.50 |

**Deteksi outlier:**
- Q1 = 4764.92 | Q3 = 5745.04 | IQR = 980.12
- Batas bawah (Q1 - 1.5×IQR) = 3294.74
- Batas atas (Q3 + 1.5×IQR) = 7215.22
- Outlier terdeteksi: Run 5 (2100.50 MB)

**Investigasi (untuk setiap outlier):**

| Outlier | Nilai | Kemungkinan Penyebab | Keputusan |
|---------|-------|---------------------|-----------|
| *Run 5* | *2100.50* | *Windows 11 melakukan disk swapping ekstrem (memindah beban ke virtual memory di storage lokal) akibat manajemen termal yang mulai jenuh.* | *Tandai sebagai contextual anomaly, biarkan data tetap ada sebagai bukti fenomena swapping OS di laporan analisis.* |

---

## Latihan 3 — Validation Report

Buat laporan validasi ringkas untuk dataset eksperimen Anda.

**1. Completeness:** 100% data terkumpul (80 runs total).
**2. Format:** [x] Konsisten / [ ] Ada inkonsistensi: -
**3. Range check (anomali):** Ditemukan indikasi nilai memori anjlok tajam (outlier bawah) pada beberapa iterasi akibat intervensi *disk swapping*.
**4. Logic check:** [x] Parameter sesuai plan / [ ] Ada ketidaksesuaian: -

**Kesimpulan:** [x] Data siap analisis / [ ] Perlu tindakan: -

---

## Refleksi

> Apa perbedaan antara "data yang benar" dan "data yang dipercaya"? Mengapa proses validasi formal diperlukan meskipun data dikumpulkan secara otomatis?

**Jawaban:**
> "Data yang benar" adalah log angka mentah yang berhasil dicatat oleh Windows PerfMon tanpa *error* di program Python, berapapun nilainya. "Data yang dipercaya" adalah log data yang sudah dipastikan bebas dari gangguan latar belakang (seperti *update* OS), konsisten dengan desain eksperimen 40 URL, dan secara logika mencerminkan perilaku penghematan RAM, bukan sekadar manipulasi *virtual memory*.
> 
> Validasi formal mutlak diperlukan karena skrip pengeksekusi tidak memahami konteks. Mesin akan terus merekam nilai memori, meskipun saat jeda 180 detik tersebut sistem sedang mengeksekusi antrean beban latar belakang (*background noise*) lain yang tidak relevan dengan objek pengamatan arsitektur penjelajah web, sehingga validasi manual diperlukan untuk memisahkan hasil sesungguhnya dari anomali acak.
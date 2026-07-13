# WS-14: Analysis, Interpretation & Failure Analysis

> **Bab 14 — Analisis Data, Interpretasi & Failure Analysis**

---

## Ringkasan Materi

### Data → Knowledge Model

```
Data → Analysis → Interpretation → Explanation → Knowledge
```

Tiga level yang berbeda:
- **Analysis** — "Apa yang terjadi?" (deskriptif + inferensial)
- **Interpretation** — "Apa artinya?" (konteks RQ + literatur)
- **Failure Analysis** — "Mengapa tidak berhasil?" (boundary conditions)

### Beyond p-value

**Statistical significance ≠ practical significance.** Selalu laporkan:
1. p-value (signifikansi statistik)
2. Effect size (besarnya efek)
3. Confidence interval (rentang ketidakpastian)

| Effect Size (Cohen's d) | Interpretasi |
|-------------------------|-------------|
| < 0.2 | Small |
| 0.2 – 0.8 | Medium |
| > 0.8 | Large |

### Pemilihan Uji Statistik

| Kondisi | Uji yang Tepat |
|---------|---------------|
| 2 grup, normal, paired | Paired t-test |
| 2 grup, non-normal | Wilcoxon signed-rank |
| > 2 grup, normal | One-way ANOVA + post-hoc |
| > 2 grup, non-normal | Kruskal-Wallis + post-hoc |
| 2 variabel kontinu | Pearson (normal) / Spearman (rank) |

### Failure Analysis as Contribution

Hipotesis yang ditolak adalah **temuan yang berharga**:

| Dataset | New (F1) | Baseline (F1) | p-value | Cohen's d |
|---------|---------|--------------|---------|-----------|
| DS-1 (small, clean) | 94.2±1.1 | 89.3±1.5 | <0.001 | **3.7** |
| DS-4 (medium, noisy) | 78.3±3.2 | 82.1±2.8 | 0.008 | **-1.3** |
| DS-5 (large, noisy) | 71.6±4.1 | 80.5±3.0 | <0.001 | **-2.5** |

**Insight:** Metode baru unggul di data bersih tapi gagal di data noisy → asumsi Gaussian dilanggar → **boundary condition** ditemukan → hybrid approach direkomendasikan.

**Partial failure + deep analysis = kontribusi lebih kaya daripada full success tanpa analisis.**

### Limitation Types

| Jenis | Contoh |
|-------|--------|
| Internal validity | Confounders yang tidak dikontrol |
| External validity | Generalisasi ke domain lain |
| Construct validity | Metrik mengukur apa yang dimaksud? |
| Statistical limitation | Sample size, asumsi distribusi |

### Jebakan Kognitif

1. "Signifikan statistik = penting secara praktis" → cek effect size
2. "Hipotesis tidak didukung → cari sudut baru" → p-hacking
3. "Kegagalan tidak perlu dilaporkan detail" → missed insight
4. "Limitasi cukup disebutkan, tidak perlu dianalisis" → kedalaman hilang

---

## Template A.14 — Analysis & Interpretation Report

```
ANALYSIS & INTERPRETATION

1. Statistik Deskriptif:
   | Skenario | Mean | Std | Median | Min | Max | n |
   |----------|------|-----|--------|-----|-----|---|
   |          |      |     |        |     |     |   |

2. Uji Hipotesis:
   Uji yang digunakan  : ____________________
   Justifikasi          : ____________________
   Hasil: p = ____, effect size (d/r/η²) = ____
   CI 95%               : [____, ____]

3. Keputusan:
   [ ] H₀ ditolak → H₁ diterima
   [ ] H₀ tidak ditolak

4. Interpretasi:
   Hubungan ke RQ       : ____________________
   Practical significance: ____________________
   Perbandingan literatur: ____________________

5. Limitation:
   | Jenis | Ancaman | Dampak | Mitigasi |
   |-------|---------|--------|----------|
   |       |         |        |          |

6. Failure Analysis (jika H₀ tidak ditolak):
   Penyebab potensial  : ____________________
   Boundary condition   : ____________________
   Insight              : ____________________
```

---

## Latihan 1 — Pemilihan Uji Statistik

Tentukan uji statistik yang tepat untuk eksperimen Anda.

| Pertanyaan | Jawaban |
|-----------|---------|
| Berapa grup yang dibandingkan? | 2 grup (Google Chrome dan Mozilla Firefox) |
| Apakah data berpasangan (paired)? | Tidak (Independent), pengujian terpisah pada dua browser berbeda. |
| Apakah distribusi normal? (uji normalitas) | Ya, diasumsikan berdistribusi normal karena jumlah sampel besar (n=40 per grup) memenuhi Teorema Limit Pusat. |
| **Uji yang dipilih:** | **Independent Sample t-test** |
| **Justifikasi:** | Eksperimen membandingkan nilai rata-rata dari dua kelompok yang saling bebas (independen) menggunakan skala ukur rasio (Megabytes). |

**Effect size yang akan dilaporkan:** [x] Cohen's d / [ ] Eta-squared / [ ] Lainnya: ____

---

## Latihan 2 — Interpretasi Hasil

Gunakan data berikut (atau data riil Anda) untuk berlatih interpretasi.

**Data:**
| Model | RAM Pasca 180s (mean ± std) | n |
|-------|----------------------|---|
| Google Chrome (Intervensi) | 5214.3 ± 450.8 MB | 40 |
| Mozilla Firefox (Baseline) | 3045.6 ± 180.5 MB | 40 |

p < 0.001, Cohen's d = 6.2, CI 95% = [1978.5, 2358.9]

| Aspek | Interpretasi |
|-------|-------------|
| Signifikansi statistik | p < 0.001 → perbedaan konsumsi memori sangat signifikan pada tingkat α=0.001. |
| Effect size | d=6.2 → efek sangat besar (huge effect), arsitektur browser mendikte konsumsi memori secara masif. |
| Practical significance | Selisih 2.1 GB sangat esensial bagi stabilitas sistem operasi secara nyata pada laptop berspesifikasi pas-pasan. |
| Hubungan ke RQ | Firefox menahan kapasitas memori secara lebih efisien dibandingkan Chrome saat menangani 40 tab pasif, menolak hipotesis penelitian. |
| Perbandingan literatur | Sesuai dengan prinsip arsitektur mesin Gecko (Firefox) yang terpusat dibandingkan isolasi proses (sandboxing) Chromium (Chrome). |

---

## Latihan 3 — Failure Analysis

Latih kemampuan failure analysis: hipotesis TIDAK didukung. Apa yang bisa dipelajari?

**Skenario:** Hipotesis menyatakan fitur Memory Saver Chrome membebaskan RAM lebih banyak. Hasil eksperimen justru menunjukkan Firefox jauh lebih hemat memori hingga 2 GB. (H₁ ditolak).

| Pertanyaan | Jawaban |
|-----------|---------|
| Apakah ini "gagal"? | Bukan kegagalan riset. Hipotesis yang ditolak mengungkap bukti empiris objektif yang menyanggah asumsi atau klaim awal. |
| Kemungkinan penyebab? | Fitur Memory Saver tidak bisa sepenuhnya mengatasi overhead dari arsitektur sandboxing Chrome yang mengharuskan tiap tab memiliki proses memorinya sendiri. |
| Boundary condition? | Chrome mungkin berkinerja lebih efisien pada skenario multitasking ringan (di bawah 10 tab), namun gagal pada skala 40 tab. |
| Insight yang bisa diambil? | Terdapat trade-off yang nyata antara keamanan isolasi proses dan efisiensi memori. Pengguna dengan prioritas kelancaran sistem lebih disarankan menggunakan Firefox. |
| Apakah layak dilaporkan? Mengapa? | Sangat layak. Melaporkan temuan ini meluruskan disinformasi dan memberikan panduan optimasi yang valid tanpa unsur bias. |

**Limitation terkait:**
| Jenis | Ancaman | Dampak |
|-------|---------|--------|
| External Validity | URL pengujian statis/berita | Kesimpulan belum tentu berlaku jika membuka Web Apps berat (misal: Figma, Google Docs). |
| Construct Validity | Hanya mengukur Private Bytes memori | Tidak memperhitungkan metrik lonjakan CPU (processor spike) ketika tab dibangunkan kembali (wake up). |

---

## Refleksi

> Apakah "failure" dalam riset benar-benar gagal, atau justru kontribusi? Bagaimana failure analysis mengubah cara Anda melihat hasil negatif?

> Kegagalan hipotesis sama sekali bukan kegagalan penelitian, melainkan wujud nyata evaluasi ilmiah yang independen. Hasil temuan negatif mencegah peneliti lain melakukan asumsi yang salah dan membongkar batas operasional suatu arsitektur perangkat lunak.
> Failure analysis menyadarkan bahwa data yang tidak sesuai ekspektasi bukanlah sebuah aib yang harus dimanipulasi, melainkan ruang untuk menemukan pengetahuan baru terkait batas maksimal kapabilitas sebuah sistem komputasi (boundary condition).
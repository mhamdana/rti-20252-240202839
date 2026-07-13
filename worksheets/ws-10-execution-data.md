# WS-10: Experiment Execution & Data Collection

> **Bab 10 — Eksekusi Eksperimen & Pengumpulan Data**

---

## Ringkasan Materi

### Experiment Execution Pipeline

```
Design → Execution Plan → Controlled Execution → Data Collection → Data Logging → Dataset for Analysis
```

### Multiple Run = Non-Negotiable

Single run **tidak pernah cukup** untuk klaim ilmiah. Minimum 5-10 run per skenario dengan seed berbeda. Multiple run menghasilkan:
- Mean, std, confidence interval
- Distribusi hasil → uji statistik
- Variabilitas → error bar di grafik

### Execution Plan

Setiap eksperimen harus memiliki plan sebelum eksekusi:
- Daftar skenario
- Jumlah run per skenario
- Random seed per run (pre-determined!)
- Urutan eksekusi (randomisasi/counterbalancing)
- Pre-execution checklist

### Data Logging Komprehensif

Setiap run menghasilkan log terstruktur:
1. **Identitas** — Run ID, timestamp, skenario
2. **Konfigurasi** — Semua parameter, seed, code version
3. **Hasil** — Semua metrik, output detail
4. **Metadata** — Waktu eksekusi, resource usage, warning/error

Format: CSV/JSON/database — **bukan stdout yang di-copy-paste**.

### Engineering vs Research Execution

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Run | Sekali (deploy) | Multiple (min 5-10, seed berbeda) |
| Logging | Error log, access log | Semua parameter, metrik, metadata |
| Anomali | Bug → fix → redeploy | Investigasi → dokumentasi → analisis |
| Urutan | Tidak penting | Bisa bias — perlu randomisasi |

### Anomali = Dokumentasi, Bukan Hapus

Run gagal/anomali tidak boleh dihapus tanpa dokumentasi. Bisa jadi:
- **Bug** → fix & re-run (dokumentasikan!)
- **Batas kemampuan metode** → DNF = temuan
- **Data yang bias** jika hanya simpan run "berhasil"

### Jebakan Kognitif

1. "Satu angka cukup" → tanpa distribusi, tidak bisa diuji
2. "Seed tidak penting" → bahkan algoritma deterministik bisa dipengaruhi library stokastik
3. "Run gagal langsung hapus" → kehilangan temuan potensial
4. "Semua run harus hari ini" → thermal throttling, fatigue

---

## Template A.10 — Execution Plan & Data Log

```
EXECUTION PLAN

| Run # | Skenario | Seed | Parameter | Status | Waktu | Output File |
|-------|----------|------|-----------|--------|-------|-------------|
| 1     |          |      |           |        |       |             |
| 2     |          |      |           |        |       |             |
| 3     |          |      |           |        |       |             |
| ...   |          |      |           |        |       |             |

Jumlah runs per skenario : ____
Total runs               : ____

DATA LOG (per run):
  Run ID    : ____________________
  Timestamp : ____________________
  Skenario  : ____________________
  Input     : ____________________
  Output    : ____________________
  Anomali   : ____________________
  Catatan   : ____________________
```

---

## Latihan 1 — Execution Plan

Susun execution plan untuk eksperimen Anda. Tentukan skenario, jumlah run, dan seed sebelum eksekusi.

| Run # | Skenario | Seed | Parameter Kunci | Status |
|-------|----------|------|----------------|--------|
| *1* | *Google Chrome (Intervensi)* | *N/A* | *40 Tab Otomatis, Idle 180s* | *Selesai* |
| *2* | *Google Chrome (Intervensi)* | *N/A* | *40 Tab Otomatis, Idle 180s* | *Selesai* |
| 41 | Mozilla Firefox (Baseline) | N/A | 40 Tab Otomatis, Idle 180s | Selesai |
| 42 | Mozilla Firefox (Baseline) | N/A | 40 Tab Otomatis, Idle 180s | Selesai |
| ... | (Dan seterusnya hingga 80 run) | N/A | 40 Tab Otomatis, Idle 180s | Selesai |

**Total skenario:** 2 (Chrome vs Firefox)
**Run per skenario:** 40
**Total run keseluruhan:** 80

---

## Latihan 2 — Data Log Terstruktur

Desain format data log untuk eksperimen Anda. Tentukan field apa saja yang akan dicatat.

**Identitas:**
| Field | Contoh |
|-------|--------|
| Run ID | *CHR-001 / FFX-001* |
| Timestamp | *2026-07-13T10:30:00* |
| Skenario | *Kondisi Intervensi / Baseline* |

**Konfigurasi:**
| Field | Contoh |
|-------|--------|
| Seed | *N/A (Urutan statis)* |
| Code version | *Script Python Automation v1* |
| Lingkungan | *Windows 11, Clean Session* |

**Hasil:**
| Metrik | Tipe Data | Range Valid |
|--------|----------|-------------|
| *Total RAM Terpakai (Pasca 180s)* | *float* | *0.0 – 16000.0 (MB)* |
| Total RAM Awal (Peak) | float | 0.0 – 16000.0 (MB) |
| Total RAM Terbebas | float | > 0.0 (MB) |

**Format output:** [x] CSV / [ ] JSON / [ ] Database / [x] Lainnya: TXT Log

---

## Latihan 3 — Anomaly Protocol

Rencanakan bagaimana menangani anomali. Untuk setiap jenis, tentukan langkah yang diambil.

| Jenis Anomali | Contoh | Tindakan |
|---------------|--------|----------|
| Run gagal (crash) | *Contoh: Script terhenti / OOM saat load 40 tab* | *Contoh: Dokumentasikan titik crash, restart OS, dan ulangi eksekusi run tersebut* |
| Hasil ekstrem | Kapasitas RAM turun drastis secara tidak wajar (indikasi disk swapping). | Lakukan investigasi metrik Page File. Jika swapping aktif, tandai run sebagai outlier. |
| Waktu eksekusi anomali | Pemuatan awal 40 tab memakan waktu sangat lama (koneksi tidak stabil). | Hentikan skrip Python, periksa status internet, dan ulangi run saat bandwidth stabil. |
| Inkonsistensi dengan run lain | Terdapat lonjakan memori akibat background process saat fase idle. | Periksa Task Manager Windows. Diskualifikasi run yang terinterferensi update OS, lalu re-run. |

**Prinsip:** Detect → Investigate → Document → Decide

---

## Refleksi

> Pernahkah Anda melaporkan hasil riset/tugas dari single run? Apa risikonya? Bagaimana multiple run mengubah kepercayaan terhadap hasil?

**Pengalaman sebelumnya:**
> Dalam praktikum infrastruktur sistem sebelumnya, pengujian performa sering kali hanya dicatat satu kali (single run). Risikonya sangat tinggi karena angka yang terekam sangat rentan mengalami bias akibat fluktuasi noise dari proses latar belakang sistem operasi (Windows 11) maupun fluktuasi suhu perangkat keras.
**Yang akan dilakukan berbeda:**
> Melakukan perekaman menggunakan skrip otomatisasi Python dengan mengulang eksekusi sebanyak 40 repeated runs (dengan jeda 180 detik). Hal ini akan menghasilkan distribusi data rata-rata yang stabil dan kebal terhadap anomali acak, sehingga kesimpulan akhir komparasi RAM jauh lebih kredibel.
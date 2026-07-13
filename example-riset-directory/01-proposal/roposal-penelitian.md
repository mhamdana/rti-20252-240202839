# Proposal Penelitian: Komparasi Efisiensi Alokasi Memori RAM pada Browser Chromium dan Gecko

## 1. Latar Belakang
Pesatnya penggunaan aplikasi berbasis web telah menempatkan *web browser* sebagai komponen paling krusial dalam ekosistem sistem operasi. Namun, penggunaan memori (RAM) yang tinggi oleh *browser* modern sering kali menyebabkan penurunan performa sistem secara keseluruhan. Penelitian ini difokuskan pada perbandingan dua *engine* utama, Chromium (Blink) dan Gecko (Mozilla), dalam hal efisiensi alokasi memori saat menjalankan beban kerja (*workload*) simulasi yang identik.

## 2. Rumusan Masalah
* Bagaimana perbedaan profil penggunaan memori antara *engine* Chromium dan Gecko saat menjalankan beban kerja yang sama?
* *Engine* mana yang lebih efisien dalam mengelola memori pada skenario *multi-tab browsing*?
* Sejauh mana mekanisme *Tab Unloading* atau *Memory Saver* pada masing-masing *engine* memengaruhi *footprint* memori secara keseluruhan?

## 3. Tujuan Penelitian
* Melakukan pengukuran kuantitatif terhadap penggunaan memori (*Working Set* dan *Private Working Set*) pada Chromium dan Gecko.
* Membandingkan efisiensi kedua *engine* dalam mengelola beban memori secara *real-time*.
* Memberikan acuan empiris mengenai konsumsi memori bagi pengguna dan pengembang aplikasi web.

## 4. Urgensi Penelitian
Penggunaan memori yang berlebihan berdampak langsung pada performa perangkat, terutama pada perangkat dengan keterbatasan RAM. Riset ini memberikan data empiris yang krusial untuk memahami karakteristik manajemen memori *browser* modern di sistem operasi Windows.

## 5. Metodologi Penelitian (Ringkasan)
* **Instrumen:** Otomatisasi pengujian dengan Python (Playwright) dan monitoring metrik via *Windows Performance Monitor* (PerfMon).
* **Desain:** Eksperimen *repeated runs* (N=30) untuk mencapai signifikansi statistik.
* **Analisis:** Pembersihan *outlier* menggunakan metode statistik dan komparasi hasil antar-*engine* menggunakan uji hipotesis.

## 6. Roadmap
- **Tahap 1:** Desain Arsitektur & Skema Eksperimen (Selesai)
- **Tahap 2:** Implementasi Skrip Otomatisasi & Monitoring (Selesai)
- **Tahap 3:** Pengambilan Data (Dalam Proses/Sesuai Folder 04-data)
- **Tahap 4:** Analisis Statistik & Visualisasi Hasil (Rencana Lanjutan)
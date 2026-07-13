# Judul: Analisis Komparatif Efisiensi Alokasi Memori RAM pada Browser Chromium dan Gecko dalam Lingkungan Windows

## 1. PENDAHULUAN
[cite_start]Aplikasi *web browser* desktop modern menuntut sumber daya sistem yang besar[cite: 1]. [cite_start]Namun, penggunaan memori (RAM) yang tidak efisien sering memicu *disk swapping* dan *lag* pada perangkat berspesifikasi standar[cite: 2]. [cite_start]Penelitian ini bertujuan mengevaluasi efisiensi manajemen memori pada *engine* Chromium (Google Chrome) dan Gecko (Mozilla Firefox) saat menangani beban kerja 35 tab pasif[cite: 3].

## 2. TINJAUAN PUSTAKA
[cite_start]Penelitian sebelumnya menunjukkan bahwa arsitektur *multi-process* pada Chromium menawarkan isolasi memori yang lebih granular dibandingkan arsitektur Gecko[cite: 4]. [cite_start]Namun, efektivitas mekanisme fitur *Memory Saver* dan *Tab Unloading* masih memerlukan pembuktian empiris dalam kondisi beban kerja yang identik[cite: 5].

## 3. METODOLOGI

[cite_start]Penelitian ini menggunakan pendekatan kuantitatif dengan eksperimen *repeated runs* (N=3) untuk memastikan validitas data[cite: 6]. [cite_start]Pengambilan data dilakukan menggunakan *Windows Performance Monitor* (PerfMon) untuk mencatat penggunaan memori (MB) per proses, yang kemudian diolah untuk menghitung total kapasitas RAM yang terbebaskan dan durasi eksekusi pelepasan memori[cite: 7].

## 4. HASIL DAN ANALISIS
[cite_start]Hasil pengujian menunjukkan perbedaan profil manajemen memori sebagai berikut[cite: 8]:
* [cite_start]**Efisiensi Pelepasan Memori:** Data menunjukkan volume (MB) yang berhasil dibebaskan setelah 15 menit pasif pada kedua *engine*[cite: 8].
* [cite_start]**Kecepatan Respons:** Durasi waktu yang dibutuhkan masing-masing *engine* untuk memicu mekanisme pembekuan tab[cite: 8].
* [cite_start]**Analisis:** Chromium terbukti memberikan retensi memori yang lebih signifikan melalui isolasi proses, sementara Gecko mengandalkan *resource-sharing* yang lebih hemat secara *overhead* awal[cite: 4, 8].

## 5. KESIMPULAN
[cite_start]Penelitian menyimpulkan bahwa Chromium lebih efektif dalam membebaskan memori pada skenario 35 tab pasif berkat arsitektur *process-per-tab*-nya, sedangkan Gecko memberikan manajemen *overhead* yang lebih adaptif pada kondisi memori sangat terbatas[cite: 8]. [cite_start]Saran penelitian selanjutnya adalah menguji pengaruh ekstensi pihak ketiga terhadap pola pelepasan memori ini[cite: 9].

## 6. DAFTAR PUSTAKA
[Daftar referensi IEEE dari file daftar-pustaka.bib Anda]
# WS-01: Distorsi & Paradigma

> **Bab 1 — Research Mindset in IT**

---

## Ringkasan Materi

### Research Trust Model

Pengetahuan ilmiah tidak muncul langsung dari kenyataan. Ia melewati **6 tahap transformasi** yang masing-masing rawan distorsi:

```
Reality → Data → Processing → Analysis → Inference → Knowledge
```

Etika mencegah distorsi yang disengaja (fabrikasi, cherry-picking). Validitas mendeteksi distorsi yang tidak disengaja (confounding variable, sampling bias).

### Tiga Jenis Validitas

| Jenis | Pertanyaan | Contoh Ancaman |
|-------|-----------|----------------|
| **Internal Validity** | Apakah hubungan kausal benar ada? | Confounding variable |
| **External Validity** | Apakah bisa digeneralisasi? | Dataset terlalu homogen |
| **Construct Validity** | Apakah mengukur hal yang benar? | Metrik tidak sesuai klaim |

### Paradigma Riset

Mata kuliah ini menggunakan pendekatan **Positivist** (fenomena TI bisa diukur objektif melalui eksperimen terkontrol) diperkuat **Design Science Research** (DSR). Penting untuk membedakan keduanya:

| Paradigma | Cara Kerja | Contoh di TI |
|-----------|-----------|---------------|
| **Positivis** | Uji hipotesis dengan eksperimen terkontrol | Apakah CNN lebih akurat dari RF pada dataset X? |
| **Design Science Research** | Bangun artefak (sistem/model/framework) untuk menguji proposisi | Dapatkah arsitektur hybrid CNN+LSTM membuktikan peningkatan recall ≥5%? |
| **Interpretivis** | Pahami makna melalui konteks & kualitatif | Bagaimana peneliti manafsirkan anomali data sensor IoT? |

Dalam DSR, artefak **bukan tujuan akhir** — ia adalah instrumen untuk menghasilkan pengetahuan. Pertanyaan riset tetap harus difalsifikasi.

### Mode Berpikir Peneliti

**Curious** (mempertanyakan fenomena) → **Critical** (mengevaluasi klaim berdasarkan bukti) → **Systematic** (merancang investigasi terstruktur dan reproducible).

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan | Membuat sistem yang bekerja | Menghasilkan pengetahuan yang valid |
| Pertanyaan khas | "Bagaimana membuatnya jalan?" | "Apakah klaim ini benar?" |
| Ukuran sukses | Sistem berfungsi, client puas | Hipotesis terjawab, temuan tervalidasi |
| Kegagalan | Harus dihindari | Harus dilaporkan (negative result = kontribusi) |

### Istilah Penting

- **Research Mindset** — Pola pikir yang menuntut bukti dan mempertanyakan asumsi
- **Research Ethics** — Prinsip perilaku: kejujuran, objektivitas, keterbukaan, akuntabilitas
- **HARKing** — Hypothesizing After Results are Known — merumuskan hipotesis setelah melihat data
- **Falsifiability** — Hipotesis harus bisa dibuktikan salah

---

## Template A.1 — Research Mindset Self-Assessment

```
Nama Peneliti    : ____________________
Tanggal          : ____________________

1. Ketika membaca klaim "metode X 95% akurat":
   - Pertanyaan pertama saya: ____________________
   - Data yang dibutuhkan untuk verifikasi: ____________________

2. Posisi paradigma:
   - Pendekatan: [ ] Positivis  [ ] Interpretivis  [ ] Design Science  [ ] Mixed
   - Alasan: ____________________

3. Identifikasi distorsi:
   - Asumsi tersembunyi: ____________________
   - Sumber bias potensial: ____________________
   - Langkah mitigasi: ____________________

4. Komitmen etika:
   - Data yang tidak akan dimanipulasi: ____________________
   - Batasan yang diakui sejak awal: ____________________
```

---

## Latihan 1 — Identifikasi Distorsi

Pilih satu paper riset di bidang TI yang mengklaim "metode X meningkatkan performa." Telusuri setiap tahap Research Trust Model.

> **Panduan pencarian paper:** Gunakan [IEEE Xplore](https://ieeexplore.ieee.org), [ACM Digital Library](https://dl.acm.org), atau Google Scholar. Pilih paper **tahun 2020 ke atas**, di topik yang Anda minati: deteksi anomali, klasifikasi citra, NLP, keamanan siber, IoT, dsb.
>
> **Contoh domain TI:** "Deteksi anomali lalu-lintas jaringan menggunakan CNN — akurasi meningkat 94% vs baseline SVM 87%." Distorsi potensial: apakah dataset normal/anomali seimbang? Apakah hanya diuji pada satu vendor traffic?

**Paper yang dipilih:**
<<<<<<< HEAD
> **Judul:** Evaluation of Rust and WebAssembly when building a Progressive Web Application: An analysis of performance and memory usage.
> **Penulis (Tahun):** Natan Teferi Asegehegn (2022).
=======
> Judul: _______________________________________________
> Penulis (Tahun): ______________________________________
> Sumber/Link DOI: _____________________________________
>>>>>>> upstream/main

| Tahap | Apa yang Dilakukan | Potensi Distorsi |
|-------|-------------------|-----------------|
| **Reality → Data** | Mengumpulkan metrik performa (*Lighthouse auditing*) dan jejak memori (*JSHeapUsedSize*) dari PWA berbasis Yew (Rust/Wasm) dan ReactJS. | **Sampling Bias:** Pengujian performa hanya menggunakan skenario satu komponen kecil dari *Internet Booking Engine* (IBE), sehingga belum tentu mencerminkan variasi beban kerja dari aplikasi web kompleks berskala penuh. |
| **Data → Processing** | Menjalankan pengujian dalam lingkungan tertutup dengan menutup aplikasi latar belakang serta menggunakan sesi penjelajah baru (*fresh browser sessions*). | **Environment Distortion:** Kondisi lingkungan pengujian yang sangat terisolasi ini dapat mendistorsi realitas penggunaan dunia nyata, di mana perangkat pengguna biasanya menjalankan banyak aplikasi latar belakang secara simultan. |
| **Processing → Analysis** | Menjalankan audit Lighthouse sebanyak 5 kali dan mengambil nilai median, serta mengukur memori berdasarkan variasi jumlah *DOM nodes* (300 hingga 1500). | **Measurement Bias:** Alat Puppeteer (`page.metrics()`) pada awalnya tidak mampu menangkap isolasi konsumsi memori linier dari *instance* WebAssembly secara akurat, sehingga membutuhkan *heap snapshot* tambahan untuk meminimalkan bias. |
| **Analysis → Inference** | Membandingkan skor Lighthouse antara versi ReactJS dan Yew pada platform desktop komputer serta platform *mobile* (emulasi Moto G4). | **Assumptive Bias:** Mengasumsikan penurunan skor *Largest Contentful Paint* (LCP) pada Yew murni karena kelemahan *framework*, padahal penurunan drastis tersebut diperparah oleh adanya layer latensi tambahan dari *JavaScript Web API calls* untuk *fetch data*. |
| **Inference → Knowledge** | Menyimpulkan bahwa PWA berbasis Rust/Wasm menghasilkan performa setara ReactJS pada desktop, namun berkinerja lebih buruk pada platform *mobile*. | **Overgeneralization:** Kesimpulan mengenai performa buruk di *mobile* dan efisiensi memori Rust ditarik dari arsitektur *framework* Yew, sehingga belum tentu berlaku sama jika menggunakan *framework* Wasm lain seperti Seed atau Blazor. |

**Distorsi paling besar di tahap:** Processing → Analysis.

**Dua distorsi spesifik yang teridentifikasi:**
1. **Wasm Memory Reporting Limitation:** Ketidakmampuan metrik dasar Puppeteer dalam melacak alokasi memori linier terisolasi milik *Wasm instance* berpotensi memicu pelaporan data *runtime memory* yang tidak valid sebelum dievaluasi ulang via *heap snapshot*.
2. **Web API Interleaving Latency:** Proses interaksi bi-direksional antara Wasm dan JavaScript glue code untuk memicu *network request* serta memanipulasi DOM menciptakan bias latensi tambahan pada pengukuran metrik LFP.

---

## Latihan 2 — Analisis Kasus Etika

Skenario: Seorang peneliti menemukan bahwa jika 3 data point outlier (misalnya, nilai pengujian Lighthouse yang melonjak tinggi akibat interferensi proses internal OS) dihapus, hasil eksperimennya menjadi signifikan. Dengan outlier, hasilnya tidak signifikan.

| Perspektif | Analisis |
|------------|---------|
| **Kejujuran ilmiah** | Peneliti wajib melaporkan ke-5 hasil pengujian Lighthouse secara utuh termasuk data anomali tersebut. Menyembunyikan data *outlier* hanya agar aplikasi Rust/Wasm terlihat selalu unggul dan stabil merupakan bentuk manipulasi informasi. |
| **Transparansi** | Peneliti harus memaparkan secara terbuka fluktuasi nilai skor audit pada platform emulasi *mobile*. Pembaca perlu mengetahui apakah variansi skor terjadi karena efisiensi kode atau ketidakstabilan *environment* pengujian komputasi. |
| **Peer review** | Penelaah ahli (*reviewer*) memerlukan visibilitas terhadap seluruh rentang data (nilai minimum, maksimum, dan standar deviasi) untuk memverifikasi ketangguhan klaim performa komparatif kedua PWA tersebut. |

**Keputusan akhir dan justifikasi:**
> **Keputusan:** Peneliti harus mempertahankan seluruh data point (termasuk 3 data *outlier*) dan menggunakan pendekatan statistik agregasi seperti median atau rata-rata untuk mereduksi variansi data secara jujur.
> **Justifikasi:** Merujuk pada asas kejujuran ilmiah, melaporkan hasil yang tidak signifikan atau kegagalan optimasi (*negative result*) tetap bernilai sebagai kontribusi pengetahuan. Melaporkan penyebaran data secara transparan membantu mengidentifikasi batasan riil dari eksekusi WebAssembly pada perangkat dengan keterbatasan *resource* memori dan daya.

---

## Latihan 3 — Posisi Paradigma

**Topik riset:** Evaluation of Rust and WebAssembly when building a Progressive Web Application: An analysis of performance and memory usage.

> **Skala 1–5:** 1 = tidak sesuai sama sekali dengan topik ini, 5 = sangat sesuai dan dominan digunakan pada riset bertopik serupa.

| Kriteria | Positivis | Interpretivis | Design Science |
|----------|-----------|---------------|----------------|
<<<<<<< HEAD
| **Ksesuaian dengan topik (1–5)** | **5** | **1** | **5** |
| **Jenis data yang dikumpulkan** | Data kuantitatif terukur seperti skor metrik Lighthouse (FCP, LCP, TTI) dan ukuran *bundle* (MB). | Pemahaman kualitatif mengenai opini atau kenyamanan subjektif pengembang saat menulis kode Rust. | Artefak fungsional berupa dua versi prototype PWA (*Internet Booking Engine*) sebagai instrumen uji. |
| **Limitasi paradigma** | Angka performa murni tidak bisa mengurai kompleksitas biaya *development cost* pengumpulan keahlian bahasa Rust. | Tidak bisa memberikan pembuktian empiris berbasis angka yang valid mengenai efisiensi memori *runtime*. | Terlalu fokus pada evaluasi teknis performa artefak sehingga mengabaikan aspek interaksi manusia jangka panjang. |
=======
| Kesesuaian dengan topik (1–5) | *Contoh: 4 — topik kuantitatif, cocok uji hipotesis* | *Contoh: 2 — topik tidak studi makna/konteks* | *Contoh: 5 — membangun artefak untuk uji klaim* |
| Jenis data yang dikumpulkan | *Metrik numerik, log eksperimen* | *Wawancara, observasi kualitatif* | *Hasil uji artefak, komparasi kinerja* |
| Limitasi paradigma | | | |
>>>>>>> upstream/main

**Paradigma yang dipilih:** Design Science di bawah asumsi filosofis Positivism.
**Alasan:** Riset ini berfokus pada penciptaan dan evaluasi sebuah artefak teknologi (prototype PWA IBE) untuk memecahkan masalah kompleksitas multi-platform dalam rekayasa perangkat lunak. Evaluasi kualitas dan efisiensi artefak tersebut kemudian diuji secara objektif menggunakan eksperimen kuantitatif di laboratorium terkontrol untuk menghasilkan pengetahuan empiris yang bebas dari bias pengamat.

---

## Refleksi

> Sebelum membaca materi ini, apakah pernah mempertanyakan klaim "95% akurat"? Setelah memahami rantai distorsi, pertanyaan apa yang sekarang akan diajukan saat membaca paper?

**Jawaban:**
> Sebelum menelaah materi ini, saya cenderung menerima begitu saja klaim paper yang menyatakan WebAssembly pasti lebih cepat daripada JavaScript hanya karena landasan teorinya adalah bahasa terkompilasi. 
> 
> Setelah memahami rantai transformasi dalam *Research Trust Model*, saya menyadari bahwa efisiensi tinggi dari sebuah teknologi sangat terikat pada variansi lingkungan eksekusinya. Kini, pertanyaan kritis yang akan saya ajukan saat membaca paper adalah:
> *"Bagaimana karakteristik lingkungan pengujian diisolasi dari gangguan eksternal, dan apakah data log performa diperoleh dari skenario running berulang (repeated runs) pada clean session yang adil bagi baseline maupun metode intervensi?"*

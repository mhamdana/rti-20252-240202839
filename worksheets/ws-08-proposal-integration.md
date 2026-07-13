# WS-08: Proposal Integration (UTS)

> **Bab 8 — Proposal & Checkpoint**

---

## Ringkasan Materi

### Proposal = Satu Argumen Utuh

Proposal riset bukan kumpulan bab yang independen. Ia adalah **satu argumen** yang mengalir dari masalah ke rencana solusi. Jika satu koneksi putus, seluruh proposal kehilangan koherensi.

### Integration Map — 6 Koneksi Kritis

```
Problem (Bab 2) → Gap (Bab 3) → RQ & H (Bab 4) → Metrik (Bab 5) → Sistem (Bab 6) → Eksperimen (Bab 7)
```

| Koneksi | Pertanyaan Verifikasi |
|---------|----------------------|
| Problem → Gap | Apakah gap muncul dari analisis literatur terhadap masalah? |
| Gap → RQ | Apakah RQ langsung menjawab gap yang teridentifikasi? |
| RQ → Metrik | Apakah setiap variabel di RQ punya metrik terdefinisi? |
| Metrik → Sistem | Apakah setiap metrik bisa diukur oleh komponen sistem? |
| Sistem → Eksperimen | Apakah desain eksperimen menggunakan sistem sebagai instrumen? |

### Koherensi Vertikal + Horizontal

- **Vertikal** — Alur logis atas-ke-bawah (problem → experiment). Setiap section menjawab pertanyaan yang diangkat section sebelumnya dan memunculkan pertanyaan baru.
- **Horizontal** — Konsistensi terminologi (nama variabel di RQ = di hipotesis = di metrik = di desain)

**Operasionalisasi Red Thread** (benang merah):
```
Bab 2 (Problem) → | memperkenalkan masalah X + evidensi |
                          ↓ menimbulkan pertanyaan: "apa akar gap-nya?"
Bab 3 (Gap)     → | menjawab pertanyaan tadi + membuka "lalu apa yang perlu diteliti?" |
                          ↓
Bab 4 (RQ/H)    → | menjawab gap dengan pertanyaan spesifik + prediksi terukur |
                          ↓
Bab 5-7 (Method)→ | menjawab RQ melalui desain eksperimen yang tepat |
```
Jika ada lompatan (section B tidak menjawab pertanyaan section A), red thread putus.

### Jebakan Kognitif

| Jebakan | Deskripsi |
|---------|----------|
| "Selling" Introduction | Menulis promosi, bukan menyajikan data dan gap |
| Copy-paste Methodology | Menyalin deskripsi tekstbook tanpa menyesuaikan ke RQ |
| Optimistic Timeline | Meremehkan waktu implementasi; selalu tambah buffer 30-50% |
| No Possibility of Failure | Mengimplikasikan hasil pasti sukses — proposal jujur mengakui H₀ mungkin tidak ditolak |

### Struktur Proposal

1. **Pendahuluan** — Latar belakang + problem statement (Bab 1-2)
2. **Tinjauan Pustaka** — Literature review + gap + baseline (Bab 3)
3. **RQ / Kontribusi / Hipotesis** — (Bab 4)
4. **Metodologi** — Metrik + sistem + desain eksperimen (Bab 5-7)
5. **Timeline & Output**

### Istilah Penting

- **Integration Map** — Diagram 6 koneksi kritis antar komponen proposal
- **Vertical Coherence** — Alur logis atas-ke-bawah
- **Horizontal Coherence** — Konsistensi terminologi di semua bagian
- **Checkpoint** — Titik self-assessment sebelum transisi dari desain ke eksekusi

---

## Template A.8 — Integration Checklist

```
PROPOSAL INTEGRATION CHECKLIST

Koneksi Vertikal (Flow Atas-Bawah):
  [ ] Problem → Gap: masalah terdokumentasi di literatur
  [ ] Gap → RQ: pertanyaan menjawab gap spesifik
  [ ] RQ → Hypothesis: hipotesis memprediksi jawaban
  [ ] Hypothesis → Metric: metrik mengukur variabel dalam hipotesis
  [ ] Metric → System: komponen sistem menghasilkan/mengukur metrik
  [ ] System → Experiment: desain eksperimen menggunakan sistem

Koneksi Horizontal (Konsistensi):
  [ ] Istilah sama di semua bagian
  [ ] Variabel di RQ = variabel di hipotesis = metrik di desain
  [ ] Scope tidak berubah dari masalah ke eksperimen

Cognitive Trap Checklist:
  [ ] Tidak ada paragraf "promosi" di pendahuluan (hanya data & gap)
  [ ] Metodologi disesuaikan ke RQ, bukan copy-paste textbook
  [ ] Timeline sudah ditambah buffer 30-50% dari estimasi awal
  [ ] Proposal mengakui kemungkinan H0 tidak ditolak (honest uncertainty)
  [ ] Tidak ada klaim "pasti berhasil" atau "meningkatkan signifikan"

Rubrik Self-Assessment:
| Kriteria     | 1 (Lemah)                                        | 2 (Cukup)                                     | 3 (Baik)                                           | Skor |
|------------- |--------------------------------------------------|-----------------------------------------------|----------------------------------------------------|------|
| Koherensi    | >2 koneksi vertikal terputus                     | 1-2 koneksi lemah, argumen masih bisa diikuti | Semua 6 koneksi terhubung, red thread jelas        |      |
| Specificity  | Variabel/metrik masih abstrak, tidak ada angka   | Sebagian metrik terdefinisi numerik           | Semua metrik + threshold + unit pengukuran jelas   |      |
| Feasibility  | Timeline >6 bulan tanpa memperhitungkan sumber   | Timeline 3-6 bulan dengan asumsi tertentu     | Timeline 1-3 bulan realistis dengan rencana detail |      |
| Rigor        | Baseline tidak jelas atau straw man              | 1-2 baseline dengan justifikasi partial       | 2+ baseline SOTA + justifikasi pemilihan lengkap   |      |
```

---

## Latihan 1 — Kompilasi Proposal Mini

Kumpulkan hasil dari WS-02 sampai WS-07 menjadi satu ringkasan proposal.

| Komponen | Sumber | Isi (1-2 kalimat) |
|----------|--------|-------------------|
| Problem Statement | WS-02 | Penggunaan aplikasi *web browser* dalam skenario *multi-tab* memicu konsumsi kapasitas RAM berlebih yang mengakibatkan penurunan performa sistem (lag/hang) bagi pengguna perangkat berspesifikasi standar . |
| Gap | WS-03 | Terdapat kesenjangan data evaluatif empiris mengenai perbedaan efektivitas reduksi memori nyata antara fitur *Memory Saver* Google Chrome dan *Tab Unloading* Mozilla Firefox saat berada dalam kondisi beban kerja yang identik . |
| RQ | WS-04 | Apakah fitur *Memory Saver* pada Google Chrome menghasilkan retensi kapasitas memori RAM yang lebih besar dibandingkan fitur *Tab Unloading* pada Mozilla Firefox saat menangani 35 tab pasif ? |
| Hipotesis | WS-04 | Google Chrome dengan fitur *Memory Saver* diduga mampu membebaskan kapasitas RAM lebih besar dibandingkan Mozilla Firefox pada pengujian 35 tab pasif . |
| Variabel & Metrik | WS-05 | Variabel bebas (IV) adalah jenis arsitektur manajemen memori browser , variabel terikat (DV) adalah efisiensi resource , yang diukur dengan metrik kapasitas RAM terbebas (MB) dan kecepatan eksekusi (detik) . |
| Sistem | WS-06 | Sistem instrumentasi menggunakan Windows Performance Monitor (PerfMon) terintegrasi untuk merekam log RAM sistem secara netral , didukung oleh Browser Internal Task Manager untuk memetakan alokasi memori pada level sub-proses internal . |
| Desain Eksperimen | WS-07 | Eksperimen dirancang sebagai *comparison study* dengan skenario *3x repeated run* berupa pembukaan 35 tab identik kaya media . Pengujian membandingkan kondisi *Baseline* (Firefox Gecko) dan *Intervensi* (Chrome Chromium) setelah dibiarkan pasif selama 15 menit pada *clean session* . |

---

## Latihan 2 — Integration Checklist

Verifikasi 6 koneksi kritis. Isi dengan merujuk tabel di Latihan 1.

| Koneksi | Status | Bukti |
|---------|--------|-------|
| Problem → Gap | ✅ | Gap secara spesifik diturunkan dari masalah lonjakan utilisasi RAM akibat beban kerja *multi-tab*, di mana belum ada pengujian evaluatif terkontrol yang membandingkan reduksi memori secara empiris antara *Memory Saver* Chrome dan *Tab Unloading* Firefox. |
| Gap → RQ | ✅ | RQ secara presisi menjawab gap dengan menanyakan apakah *Memory Saver* pada Chrome menghasilkan retensi memori lebih besar dibandingkan *Tab Unloading* pada Firefox saat menangani 35 tab pasif. |
| RQ → Hypothesis | ✅ | Hipotesis secara langsung memprediksi jawaban empiris untuk RQ, yaitu Chrome diduga mampu membebaskan kapasitas RAM lebih besar pada pengujian 35 tab pasif. |
| Hypothesis → Metric | ✅ | Klaim membebaskan kapasitas RAM pada hipotesis diukur secara mutlak menggunakan metrik volume memori RAM terbebas (Megabytes) dan kecepatan eksekusi (detik). |
| Metric → System | ✅ | Pengambilan data metrik volume memori dan durasi eksekusi direkam oleh instrumen *Windows Performance Monitor* (PerfMon) dan *profiler* bawaan aplikasi secara objektif. |
| System → Experiment | ✅ | Instrumen sistem *PerfMon* diaplikasikan langsung ke dalam skenario eksperimen *3x repeated run* dengan membuka 35 tab web di lingkungan *clean session* pada OS Windows 11 desktop. |

**Koneksi mana yang paling lemah?** Koneksi Metric → System.

**Bagaimana cara memperkuatnya?** Memastikan bahwa pengambilan metrik dari *Windows Performance Monitor* (di tingkat kernel OS) tersinkronisasi presisi dengan *Browser Internal Task Manager* agar tidak ada *delay* pencatatan yang memicu bias saat membandingkan alokasi memori antara arsitektur mesin *Chromium* dan *Gecko*.

**Konsistensi horizontal — apakah istilah dan scope konsisten?** [x] Ya / [ ] Tidak
> Terminologi utama seperti "35 tab pasif", "Memory Saver", "Tab Unloading", serta penggunaan metrik terukur "Megabytes" dan "detik" dipertahankan secara ajek dari perumusan masalah, hipotesis, hingga skenario desain eksperimen.

---

## Latihan 3 — Rubrik Self-Assessment

| Kriteria | Skor (1-3) | Justifikasi |
|----------|-----------|-------------|
| Koherensi | 3 | Semua 6 koneksi terhubung kuat; alur logis sangat jelas mulai dari fenomena perangkat lambat (lag) akibat konsumsi RAM hingga pengujian komparatif fitur pembekuan tab. |
| Specificity | 3 | Variabel sudah sangat operasional dengan metrik pengukur kuantitatif yang terdefinisi secara mutlak, yaitu kapasitas RAM terbebas dalam Megabytes (MB) dan durasi pelepasan memori dalam hitungan detik. |
| Feasibility | 3 | Desain eksperimen menggunakan instrumen bawaan sistem operasi (Windows PerfMon) yang realistis dan sangat layak untuk dieksekusi sesuai dengan timeline jadwal 8 fase kegiatan mingguan. |
| Rigor | 3 | Pemilihan Mozilla Firefox (Gecko) dengan Tab Unloading sebagai kondisi Baseline sangat setara dan representatif untuk menguji efisiensi intervensi Google Chrome (Chromium) pada lingkungan repeated runs dan clean session yang identik. |

**Skor total:** 12 / 12

**Apakah proposal siap untuk fase eksekusi?** [x] Ya / [ ] Belum
> Proposal sudah matang dan siap dieksekusi. Desain eksperimen (comparison study) beserta variabel terukurnya sudah didefinisikan dengan setup sistem operasional yang spesifik dan objektif (Windows 11, PerfMon), sehingga rancangan ini dapat langsung diimplementasikan ke tahap pengambilan data log.

---

## Refleksi

> Dari seluruh proses WS-01 sampai WS-08, bagian mana yang paling mudah dan paling sulit? Mengapa? Apa yang akan dilakukan berbeda jika mengulang dari awal?

**Bagian termudah:** Menentukan variabel dan metrik kuantitatif (WS-05). Hal ini karena metrik performa komputasi untuk efisiensi memori sangat absolut dan mudah didefinisikan secara operasional, yaitu menggunakan selisih kapasitas RAM terbebas (dalam hitungan Megabytes) dan durasi pelepasan (dalam detik).

**Bagian tersulit:** Merancang mitigasi ancaman validitas (Threat Analysis) pada desain eksperimen (WS-07). Mengisolasi lingkungan pengujian dari *background noise* atau sub-proses latar belakang acak yang secara natural dieksekusi oleh kernel OS Windows 11 sangat menantang dan rentan memicu bias pada hasil pencatatan.

**Yang akan dilakukan berbeda:**
> Saya akan mengunci spesifikasi *environment* dan parameter *clean session* (WS-09) secara mendetail sejak perumusan masalah, alih-alih di tahap metodologi akhir. Dengan memetakan batasan perangkat keras dan sistem operasi sejak awal, proses penyusunan batasan validitas eksperimen dan pencarian referensi pustaka (*baseline* SOTA) akan menjadi jauh lebih tajam dan meminimalisasi revisi ulang pada alur arsitektur pengujian.
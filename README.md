# Pertemuan 10 - String Python

## Identitas

- **Nama:** Masya Bantani
- **NIM:** 2225250113
- **Kelas:** 3E
- **Mata Kuliah:** Algoritma dan Pemrograman

## Tujuan

Mempelajari pengolahan string dalam Python, meliputi operasi dasar string, indeks dan slicing, method string, pembersihan teks, pemisahan dan penggabungan kata, pencarian kata, serta penggunaan fungsi untuk melakukan normalisasi data mahasiswa agar lebih rapi dan konsisten.

## Struktur Folder

```text
pertemuan-10-string-2225250119/
├── README.md
├── .gitignore
├── latihan/
│   ├── 01_dasar_string.py
│   ├── 02_indeks_slicing.py
│   ├── 03_method_string.py
│   ├── 04_bersihkan_teks.py
│   ├── 05_split_join.py
│   └── 06_pencarian_kata.py
└── tugas/
    └── normalisasi_data_mahasiswa.py
```

## Materi yang Dipelajari

1. Membuat dan menampilkan string menggunakan variabel.
2. Menghitung jumlah karakter menggunakan fungsi `len()`.
3. Mengubah huruf menjadi kapital dan huruf kecil menggunakan `upper()` dan `lower()`.
4. Mengakses karakter string menggunakan indeks dan mengambil bagian teks menggunakan slicing.
5. Membersihkan spasi menggunakan `strip()` serta mengubah format huruf menggunakan `title()` dan `capitalize()`.
6. Membersihkan teks dari spasi yang tidak diperlukan.
7. Memisahkan kalimat menjadi daftar kata menggunakan `split()` dan menggabungkan kata menggunakan `join()`.
8. Mencari kata dalam teks menggunakan operator `in` serta method `count()` dan `find()`.
9. Membuat fungsi untuk normalisasi nama, membuat inisial, dan menormalisasi kode kelas.
10. Menjalankan program melalui terminal VS Code serta mengelola tugas menggunakan Git dan GitHub.

## Deskripsi Latihan

| No. | Nama File | Keterangan |
|---|---|---|
| 1 | `01_dasar_string.py` | Menampilkan teks, menghitung jumlah karakter, serta mengubah huruf menjadi kapital dan huruf kecil. |
| 2 | `02_indeks_slicing.py` | Mengakses karakter pertama dan terakhir, mengambil sebagian teks, serta membalik urutan string. |
| 3 | `03_method_string.py` | Menggunakan method string untuk membersihkan dan mengubah format teks. |
| 4 | `04_bersihkan_teks.py` | Membersihkan spasi yang tidak diperlukan dan merapikan teks. |
| 5 | `05_split_join.py` | Memisahkan kalimat menjadi daftar kata dan menggabungkannya menggunakan tanda hubung. |
| 6 | `06_pencarian_kata.py` | Memeriksa keberadaan kata, menghitung jumlah kemunculan, dan mencari posisi pertama kata dalam teks. |
| 7 | `normalisasi_data_mahasiswa.py` | Menormalisasi nama mahasiswa, membuat inisial, dan mengubah kode kelas menjadi huruf kapital. |

## Cara Menjalankan Program

Pastikan Python sudah terpasang di komputer dan terminal VS Code berada di folder utama proyek.

### 1. Menjalankan File Latihan

Jalankan setiap program menggunakan perintah berikut:

```bash
python latihan/01_dasar_string.py
python latihan/02_indeks_slicing.py
python latihan/03_method_string.py
python latihan/04_bersihkan_teks.py
python latihan/05_split_join.py
python latihan/06_pencarian_kata.py
```

### 2. Menjalankan Program Tugas

Jalankan perintah berikut pada terminal VS Code:

```bash
python tugas/normalisasi_data_mahasiswa.py
```

Program akan meminta pengguna memasukkan nama dan kode kelas, kemudian menampilkan nama yang telah dinormalisasi, inisial nama, dan kode kelas dalam huruf kapital.

## Hasil Pengujian Latihan

| No. | Program | Hasil Pengujian |
|---|---|---|
| 1 | Dasar string | Teks = `Algoritma`, panjang karakter = `9`, huruf kapital = `ALGORITMA`, huruf kecil = `algoritma`. |
| 2 | Indeks dan slicing | Karakter pertama = `P`, karakter terakhir = `n`, hasil slicing = `Pemr` dan `ograman`, string terbalik = `namargormeP`. |
| 3 | Method string | Hasil `strip()` = `Kevin lius Bong`, format judul = `Kevin Lius Bong`, huruf kapital = `KEVIN LIUS BONG`. |
| 4 | Membersihkan teks | Hasil = `Belajar python untuk pendidikan`. |
| 5 | Split dan join | Daftar kata = `['data', 'teks', 'perlu', 'dibersihkan']`, hasil join = `data-teks-perlu-dibersihkan`. |
| 6 | Pencarian kata | Kata ditemukan = `True`, jumlah kemunculan = `2`, posisi pertama = `0`. |

## Hasil Pengujian Tugas

Program `normalisasi_data_mahasiswa.py` diuji menggunakan beberapa variasi nama dan kode kelas.

| No. | Input Nama | Input Kode Kelas | Nama Normalisasi | Inisial | Kode Normalisasi |
|---|---|---|---|---|---|
| 1 | `aan hendrayana` | `pmat a 2026` | Aan Hendrayana | AH | PMAT A 2026 |
| 2 | `fATHIYYAH mUTHMAINNAH` | `kelas b` | Fathiyyah Muthmainnah | FM | KELAS B |
| 3 | `BUDI` | `pmtk 01` | Budi | B | PMTK 01 |
| 4 | `siti nur aisyah` | `kelas c` | Siti Nur Aisyah | SNA | KELAS C |

Berdasarkan hasil pengujian, program berhasil menormalisasi nama dengan menghapus spasi di awal dan akhir serta mengubah huruf awal setiap kata menjadi kapital. Program juga berhasil membuat inisial berdasarkan huruf pertama setiap kata dan mengubah kode kelas menjadi huruf kapital. Hasil tersebut menunjukkan bahwa fungsi yang dibuat dapat mengolah variasi input sesuai dengan tujuan program.

## Kuis Formatif

Kuis formatif membahas materi string Python, meliputi operasi dasar string, indeks dan slicing, penggunaan method string, pembersihan teks, pemisahan dan penggabungan kata, pencarian kata, serta pembuatan fungsi untuk normalisasi nama dan kode kelas.

## Refleksi

Melalui pertemuan ini, saya mempelajari cara mengolah teks menggunakan string dalam Python. Saya memahami penggunaan indeks dan slicing untuk mengambil karakter atau bagian teks, serta penggunaan berbagai method seperti `strip()`, `upper()`, `lower()`, dan `title()` untuk membersihkan serta mengubah format teks.

Selain itu, saya mempelajari cara memisahkan dan menggabungkan kata menggunakan `split()` dan `join()`, serta mencari kata menggunakan `in`, `count()`, dan `find()`. Pada tugas normalisasi data mahasiswa, saya belajar membuat fungsi untuk merapikan nama, menghasilkan inisial, dan menyeragamkan kode kelas.

Program latihan dan tugas diuji melalui terminal VS Code untuk memeriksa kesesuaian keluarannya. Materi ini membantu saya meningkatkan pemahaman tentang pengolahan teks serta penggunaan fungsi dalam Python.

# 📦 Simple Warehouse System (S-Data Project)

![Status](https://img.shields.io/badge/Status-Academic%20Project-green?style=for-the-badge)
![Team](https://img.shields.io/badge/Team-5%20Members-blue?style=for-the-badge)

> **"Simulasi Logistik Gudang Sederhana"**
> Penerapan 5 Struktur Data Fundamental untuk manajemen gudang yang efisien.

## 📖 Tentang Project Ini
Project ini adalah simulasi sistem manajemen gudang untuk memenuhi tugas Struktur Data. Kami membagi alur kerja gudang menjadi 5 modul terpisah, di mana setiap modul menggunakan struktur data yang paling sesuai dengan karakteristik masalahnya (Array, Linked List, Stack, Queue, dan Tree).

---

## 🏗️ Pembagian Tugas & Logika (Modules)

Berikut adalah penjelasan teknis bagaimana setiap struktur data bekerja dalam ekosistem gudang kami:

### 1. 🗄️ Manajemen Rak Gudang (Storage)
* **Penanggung Jawab:** Banu
* **Menggunakan:** **Array**
* **Fungsi:** Menyimpan data fisik barang di rak.
* **Alasan:** Jumlah rak gudang bersifat tetap (misal: 100 slot). Menggunakan Array memungkinkan akses langsung (*Direct Access*) ke nomor rak tertentu tanpa perlu mencari satu per satu.

### 2. 📝 Log Riwayat Restock (History)
* **Penanggung Jawab:** Bintang
* **Menggunakan:** **Linked List**
* **Fungsi:** Mencatat riwayat setiap barang yang masuk dari supplier.
* **Alasan:** Data riwayat bersifat dinamis (tidak terbatas). Linked List memungkinkan penambahan catatan baru (`insert tail`) secara terus-menerus tanpa membebani memori di awal seperti Array.

### 3. 🛒 Antrian Pesanan (Order Processing)
* **Penanggung Jawab:** Raja
* **Menggunakan:** **Queue (Antrian)**
* **Fungsi:** Menampung daftar pesanan pelanggan yang masuk.
* **Alasan:** Menggunakan prinsip **FIFO (First In, First Out)** untuk keadilan. Pesanan yang masuk pertama kali ke sistem akan diproses dan disiapkan lebih dulu.

### 4. 🚚 Loading Barang ke Truk (Shipping)
* **Penanggung Jawab:** Michdan
* **Menggunakan:** **Stack (Tumpukan)**
* **Fungsi:** Simulasi menumpuk barang ke troli/palet sebelum dimasukkan ke dalam truk.
* **Alasan:** Menggunakan prinsip **LIFO (Last In, First Out)** untuk mengatur posisi muatan.
    * Barang pesanan pertama ditumpuk paling bawah di troli, agar saat dibongkar masuk ke truk, ia berada di posisi **paling dekat pintu**.
    * Ini memastikan barang yang pertama dipesan tetap bisa diturunkan pertama kali di tujuan.

### 5. 🔍 Katalog & Pencarian (Indexing)
* **Penanggung Jawab:** Albani
* **Menggunakan:** **Tree (Pohon Data)**
* **Fungsi:** Peta indeks untuk mencari lokasi barang berdasarkan ID.
* **Alasan:** Pencarian menggunakan struktur Tree jauh lebih cepat dibanding mencari linear. Tree membantu admin menemukan di rak nomor berapa sebuah barang disimpan hanya dengan input ID Barang.

---

## 👥 Tim Pengembang

| Nama | Role / Struktur Data | Fokus Pengerjaan |
| :--- | :--- | :--- |
| **Banu** | `Array` | Fisik Rak Gudang |
| **Bintang** | `Linked List` | Pencatatan Log Masuk |
| **Raja** | `Queue` | Administrasi Pesanan |
| **Michdan** | `Stack` | Logika Muat Barang (Loading) |
| **Albani** | `Tree` | Mesin Pencari Lokasi |

---

## 💻 Cara Menjalankan
1. Clone repository ini.
2. Buka terminal dan jalankan file `main.py` (atau `main.cpp`).
3. Ikuti instruksi menu di layar untuk melakukan simulasi (Tambah Barang, Pesan Barang, Kirim Barang, Cari Barang).

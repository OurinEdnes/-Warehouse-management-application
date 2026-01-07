# 📦 Simple Warehouse System (S-Data Project)

![Status](https://img.shields.io/badge/Status-Beginner%20Friendly-green?style=for-the-badge)
![Team](https://img.shields.io/badge/Team-5%20Members-blue?style=for-the-badge)

> **"Aplikasi Gudang Sederhana"**
> Simulasi cara kerja gudang menggunakan 5 Struktur Data dasar.

## 📖 Tentang Project Ini
Ini adalah tugas kelompok kami untuk membuat simulasi gudang. Kami mencoba menerapkan 5 metode penyimpanan data yang berbeda untuk 5 fungsi yang berbeda di dalam gudang. Tujuannya agar kami paham kapan harus pakai Array, Stack, Queue, dll.

---

## 🏗️ Pembagian Tugas & Logika (Modules)

Berikut adalah bagaimana kami membagi peran struktur data dalam gudang ini:

### 1. 🗄️ Daftar Stok Barang (Inventory)
* **Penanggung Jawab:** Banu
* **Menggunakan:** **Array**
* **Penjelasan:** * Ini adalah **Daftar Utama** barang yang ada di gudang.
    * Kita pakai Array karena jumlah rak di gudang sudah pasti (misal: Rak 1 sampai Rak 100).
    * Jadi kalau mau cek isi Rak nomor 10, kita bisa langsung akses datanya dengan mudah.

### 2. 📝 Riwayat Barang Masuk (Restock History)
* **Penanggung Jawab:** Bintang
* **Menggunakan:** **Linked List**
* **Penjelasan:** * Setiap kali ada supplier mengirim barang baru ke gudang, datanya dicatat di sini.
    * Kita pakai Linked List karena kita tidak tahu berapa banyak barang yang akan masuk hari ini.
    * Datanya saling bersambung seperti rantai. Data baru tinggal disambung di bagian belakang.

### 3. 📦 Tumpukan Packing (Ready to Ship)
* **Penanggung Jawab:** Michdan
* **Menggunakan:** **Stack (Tumpukan)**
* **Penjelasan:** * Ini adalah area tempat barang yang sudah siap dikirim ditumpuk.
    * Prinsipnya **LIFO (Last In, First Out)**.
    * Bayangkan tumpukan kardus: Kardus yang **terakhir ditaruh** di posisi paling atas, adalah yang **pertama kali diambil** oleh kurir pengiriman.

### 4. 🛒 Antrian Pesanan Pembeli (Orders)
* **Penanggung Jawab:** Raja
* **Menggunakan:** **Queue (Antrian)**
* **Penjelasan:** * Daftar pesanan dari customer yang harus segera diproses.
    * Prinsipnya **FIFO (First In, First Out)**.
    * Pesanan yang **masuk duluan**, harus dilayani dan **dikerjakan duluan**. Adil kan?

### 5. 🔍 Pencarian ID Barang (Search)
* **Penanggung Jawab:** Albani
* **Menggunakan:** **Tree (Pohon Data)**
* **Penjelasan:** * Fitur untuk mencari apakah sebuah barang ada di gudang atau tidak berdasarkan ID Barang.
    * Dengan metode Tree, kita bisa mencari barang lebih cepat dengan memilah ID (kiri lebih kecil, kanan lebih besar), jadi tidak perlu mengecek rak satu per satu dari awal.

---

## 👥 Anggota Kelompok

| Nama | Bagian |
| :--- | :--- |
| **Banu** | `Array` (List Rak Gudang) |
| **Bintang** | `Linked List` (Catatan Barang Masuk) |
| **Michdan** | `Stack` (Tumpukan Packing) |
| **Raja** | `Queue` (Antrian Pesanan) |
| **Albani** | `Tree` (Pencarian Barang) |

---

## 💻 Cara Menjalankan
1. Clone repo ini.
2. Jalankan file `main.py` (atau `main.cpp`).
3. Ikuti menu yang muncul di layar untuk simulasi gudang.

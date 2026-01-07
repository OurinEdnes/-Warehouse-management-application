# 📦 Warehouse Management System (WMS) Structure

![Project Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge&logo=git)
![Language](https://img.shields.io/badge/Language-Python%20%7C%20C%2B%2B-blue?style=for-the-badge&logo=python)
![Course](https://img.shields.io/badge/Course-Data%20Structure%20%26%20Algorithm-orange?style=for-the-badge)

> **"Efficiency is the soul of a Warehouse."**
> A comprehensive simulation of warehouse logistics implemented using 5 fundamental Data Structures.

## 📖 Table of Contents
* [About the Project](#-about-the-project)
* [System Architecture](#-system-architecture-modules)
* [Technical Implementation](#-technical-implementation)
* [Team Contributors](#-team-contributors)
* [Installation & Usage](#-installation--usage)

---

## 🧐 About The Project

**Warehouse Management System (WMS)** ini adalah proyek tugas akhir untuk mata kuliah Struktur Data. Aplikasi ini dirancang untuk mensimulasikan ekosistem gudang modern, di mana pengelolaan barang, pencatatan transaksi, dan pemrosesan pesanan terjadi secara real-time.

Tantangan utama dalam proyek ini adalah **mengintegrasikan 5 struktur data berbeda** (Array, Linked List, Stack, Queue, dan Tree) agar dapat bekerja secara harmonis untuk menyelesaikan masalah logistik yang spesifik. Kami membuktikan bahwa pemilihan struktur data yang tepat dapat meningkatkan efisiensi operasional secara signifikan.

---

## 🏗️ System Architecture (Modules)

Aplikasi ini dibagi menjadi 5 modul utama berdasarkan fungsionalitas dan struktur data yang digunakan:

### 1. 🗄️ Inventory Storage (The Rack)
* **Responsible:** Banu
* **Data Structure:** **Array**
* **Logic:**
    * Digunakan untuk merepresentasikan fisik rak gudang.
    * Setiap indeks array mewakili nomor slot rak yang unik.
    * **Keunggulan:** Akses data (pengambilan/penyimpanan) memiliki kompleksitas waktu **$O(1)$** (Constant Time) karena lokasi slot sudah terindeks secara pasti.

### 2. 📜 Transaction History (The Logger)
* **Responsible:** Bintang
* **Data Structure:** **Linked List**
* **Logic:**
    * Mencatat setiap aktivitas (Barang Masuk/Keluar) sebagai sebuah *node*.
    * Node baru akan selalu ditambahkan di akhir rantai (Tail).
    * **Keunggulan:** **Dynamic Size**. Tidak seperti Array, Linked List tidak memiliki batasan memori statis, sehingga log transaksi bisa bertambah terus menerus tanpa perlu *resize* manual.

### 3. 📦 Operations Bay (The Pallet)
* **Responsible:** Michdan
* **Data Structure:** **Stack (LIFO - Last In First Out)**
* **Logic:**
    * Mensimulasikan tumpukan barang di atas palet atau di area loading.
    * Barang yang terakhir diletakkan di tumpukan (Top) harus diambil/diproses terlebih dahulu.
    * **Keunggulan:** Menangani logika pembatalan aksi (*Undo*) atau pengambilan barang tumpukan secara natural.

### 4. 🚚 Order Processing (The Gate)
* **Responsible:** Raja
* **Data Structure:** **Queue (FIFO - First In First Out)**
* **Logic:**
    * Mengatur antrian pesanan pelanggan atau truk yang masuk ke area gudang.
    * Pesanan yang datang lebih awal (Head) akan diproses lebih dulu daripada yang datang belakangan (Tail).
    * **Keunggulan:** Menjamin prinsip keadilan (*Fairness*) dalam pemrosesan data.

### 5. 🔍 Smart Indexing (The Catalog)
* **Responsible:** Albani
* **Data Structure:** **Binary Search Tree (BST) / AVL Tree**
* **Logic:**
    * Mengindeks seluruh item di gudang berdasarkan ID Barang.
    * Memungkinkan fitur pencarian (*Searching*) yang sangat cepat.
    * **Keunggulan:** Kompleksitas pencarian rata-rata **$O(\log n)$**. Jauh lebih cepat dibandingkan mencari satu per satu (Linear Search) pada data yang besar.

---

## 👥 Team Contributors

Project ini dikembangkan oleh **Kelompok [Nama Kelompok Kalian]**:

| Name | Role | Focus Area |
| :--- | :--- | :--- |
| **Banu** | Core Engineer | `Array` Implementation |
| **Bintang** | Backend Log | `Linked List` Implementation |
| **Michdan** | Operations | `Stack` Logic |
| **Raja** | Flow Manager | `Queue` System |
| **Albani** | Algorithm Lead | `Tree` / `BST` Search |

---

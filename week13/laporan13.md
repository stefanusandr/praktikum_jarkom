# MODUL 13 - DNS (Domain Name System)
---

## Tujuan Praktikum

1. Memahami cara kerja Domain Name System (DNS).
2. Mengamati proses resolusi nama domain menjadi alamat IP.
3. Menganalisis paket DNS menggunakan Wireshark.
4. Memahami fungsi DNS Query dan DNS Response.

---

## Dasar Teori

Domain Name System (DNS) merupakan layanan yang digunakan untuk menerjemahkan nama domain menjadi alamat IP. DNS memudahkan pengguna mengakses layanan internet tanpa harus menghafal alamat IP.

Ketika pengguna mengakses suatu website, komputer akan mengirimkan DNS Query ke DNS Server. DNS Server kemudian mengirimkan DNS Response yang berisi alamat IP tujuan.

---

## Alat dan Bahan

* Wireshark
* Browser Web
* Sistem Operasi Windows
* Koneksi Internet

---

## Langkah Percobaan

1. Menjalankan aplikasi Wireshark.
2. Memulai proses capture paket.
3. Membuka browser dan mengakses beberapa website.
4. Memfilter paket menggunakan kata kunci:

```text
dns
```

5. Mengamati DNS Query dan DNS Response yang terbentuk.
6. Mencatat informasi alamat IP hasil resolusi domain.

---

## Hasil Percobaan

### DNS Query

Client mengirimkan permintaan resolusi nama domain ke DNS Server.

### DNS Response

DNS Server mengirimkan alamat IP yang sesuai dengan domain yang diminta.

Contoh:

| Domain     | IP Address      |
| ---------- | --------------- |
| google.com | xxx.xxx.xxx.xxx |
| github.com | xxx.xxx.xxx.xxx |

---

## Analisis

DNS berfungsi sebagai penerjemah antara nama domain dan alamat IP. Pada hasil capture Wireshark terlihat bahwa sebelum browser terhubung ke web server, sistem terlebih dahulu melakukan query DNS untuk memperoleh alamat IP tujuan.

Proses ini mempercepat dan mempermudah penggunaan layanan internet karena pengguna cukup mengingat nama domain.

---

## Kesimpulan

1. DNS digunakan untuk menerjemahkan nama domain menjadi alamat IP.
2. DNS bekerja menggunakan mekanisme Query dan Response.
3. Wireshark dapat digunakan untuk menganalisis paket DNS.
4. Sebelum mengakses website, client terlebih dahulu melakukan proses resolusi DNS.

---

## Dokumentasi

![DNS Query](images/dns-query.png)

![DNS Response](images/dns-response.png)

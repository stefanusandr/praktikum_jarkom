# MODUL 14 - HTTP dan Web Traffic Analysis


---

## Tujuan Praktikum

1. Memahami cara kerja protokol HTTP.
2. Mengamati komunikasi client dan web server.
3. Menganalisis HTTP Request dan HTTP Response menggunakan Wireshark.
4. Memahami metode HTTP yang digunakan dalam komunikasi web.

---

## Dasar Teori

Hypertext Transfer Protocol (HTTP) merupakan protokol yang digunakan untuk pertukaran data antara client dan web server.

HTTP bekerja dengan mekanisme request dan response. Browser bertindak sebagai client yang mengirimkan request, sedangkan web server memberikan response berupa halaman web atau data lainnya.

---

## Alat dan Bahan

* Wireshark
* Browser Web
* Sistem Operasi Windows
* Koneksi Internet

---

## Langkah Percobaan

1. Menjalankan Wireshark.
2. Memulai proses capture paket.
3. Membuka browser.
4. Mengakses beberapa website menggunakan HTTP.
5. Memfilter paket menggunakan:

```text
http
```

6. Mengamati paket HTTP Request dan HTTP Response.
7. Mencatat informasi yang diperoleh.

---

## Hasil Percobaan

### HTTP Request

Client mengirimkan request ke server menggunakan metode:

```http
GET
```

### HTTP Response

Server mengirimkan response:

```http
HTTP/1.1 200 OK
```

beserta data halaman web yang diminta.

---

## Analisis

Pada hasil capture terlihat browser mengirimkan HTTP Request ke server. Setelah request diterima, server mengirimkan HTTP Response yang berisi status code dan data halaman.

Status code 200 menunjukkan bahwa permintaan berhasil diproses. Proses ini merupakan dasar komunikasi antara browser dan web server.

---

## Kesimpulan

1. HTTP menggunakan mekanisme Request dan Response.
2. Browser berperan sebagai client sedangkan website berperan sebagai server.
3. Status code digunakan untuk menunjukkan hasil pemrosesan request.
4. Wireshark dapat digunakan untuk menganalisis lalu lintas HTTP secara detail.

---

## Dokumentasi

![HTTP Request](images/http-request.png)

![HTTP Response](images/http-response.png)

![Wireshark HTTP](images/http-wireshark.png)

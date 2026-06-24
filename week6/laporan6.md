# LAPORAN PRAKTIKUM JARINGAN KOMPUTER
# MODUL 6: TRANSMISSION CONTROL PROTOCOL (TCP)

## 1. Tujuan Praktikum

Mahasiswa dapat menginvestigasi cara kerja protokol TCP menggunakan perangkat lunak Wireshark.

### Dokumentasi

![Tujuan Praktikum](images/tcp-wireshark-overview.png)

---

## 2. Landasan Teori

TCP (Transmission Control Protocol) adalah protokol lapisan transport yang bersifat connection-oriented dan menyediakan layanan transfer data yang andal (reliable), berurutan, serta dilengkapi mekanisme flow control dan congestion control.

### Three-Way Handshake TCP

![Three Way Handshake](images/tcp-handshake.png)

---

## 3. Hasil dan Analisis Pertanyaan Modul

### A. Tampilan Awal Captured Trace

#### 1. Alamat IP dan Port Klien

Jawaban:

- IP Client : `192.168.1.102`
- Source Port : `1161`

#### Bukti Wireshark

![HTTP POST](images/tcp-post.png)

---

#### 2. Alamat IP dan Port Server

Jawaban:

- IP Server : `128.119.245.12`
- Destination Port : `80`

---

### B. Dasar TCP

#### 1. Sequence Number Segmen SYN

Jawaban:

- Relative Sequence Number = 0
- Flag SYN = 1
- Flag ACK = 0

#### Bukti

![TCP SYN](images/tcp-sequence.png)

---

#### 2. Sequence Number Segmen SYNACK

Jawaban:

- Sequence Number = 0
- Acknowledgement Number = 1
- SYN = 1
- ACK = 1

---

#### 3. Sequence Number HTTP POST

Jawaban:

Sequence Number segmen HTTP POST pertama adalah 1.

---

#### 4. Panjang Enam Segmen Pertama

Jawaban:

Sebagian besar segmen memiliki ukuran mendekati MSS (Maximum Segment Size) yaitu sekitar 1460 byte.

---

#### 5. Receiver Window

Jawaban:

Nilai Window Size tidak pernah mencapai 0 sehingga tidak terjadi hambatan pengiriman akibat kekurangan buffer.

---

#### 6. Retransmission

Jawaban:

Tidak ditemukan retransmission selama proses transfer.

---

#### 7. Throughput

Rumus:

```text
Throughput = Total Data / Total Waktu Transfer
```

Perhitungan:

```text
Throughput = 152138 / 5.3
           = 28705 byte/s
           ≈ 28.7 KB/s
```

---

### C. Congestion Control TCP

#### Analisis Time-Sequence Graph (Stevens)

![Time Sequence Graph](images/tcp-time-sequence-graph.png)

##### Slow Start

- Dimulai pada awal transmisi.
- Terjadi hingga sekitar detik ke-1.

##### Congestion Avoidance

- Dimulai setelah slow start.
- Grafik meningkat secara linier hingga akhir transfer.

---

## 4. Kesimpulan

Berdasarkan hasil analisis menggunakan Wireshark dapat disimpulkan bahwa:

1. TCP menggunakan mekanisme Three-Way Handshake sebelum melakukan transfer data.
2. Sequence Number dan Acknowledgement Number menjamin keandalan komunikasi.
3. Tidak ditemukan retransmission pada trace yang diamati.
4. Receiver Window selalu mencukupi sehingga tidak menghambat transfer.
5. Grafik Time-Sequence menunjukkan transisi dari fase Slow Start menuju Congestion Avoidance.
6. Throughput rata-rata koneksi sebesar ±28,7 KB/s.

---

## Dokumentasi Praktikum

### Gambar 1. Tampilan Awal Capture Wireshark

![Capture Awal](images/tcp-wireshark-overview.png)

### Gambar 2. Three-Way Handshake

![Handshake](images/tcp-handshake.png)

### Gambar 3. HTTP POST Segment

![HTTP POST](images/tcp-post.png)

### Gambar 4. Analisis Sequence Number

![Sequence Number](images/tcp-sequence.png)

### Gambar 5. Time Sequence Graph (Stevens)

![Time Sequence Graph](images/tcp-time-sequence-graph.png)


HASIL SS:
![mod6.1](../assets/image/mod6.1.jpeg.png)
![mod6.2](../assets/image/mod6.2.jpeg.png)
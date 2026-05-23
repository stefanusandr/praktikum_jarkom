import socket

# 1. Inisialisasi Socket TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Bind socket ke IP lokal (localhost) dan Port 5000
# (Jika nanti ingin dicoba antar laptop teman, ganti '127.0.0.1' dengan IP Wi-Fi mu)
server.bind(('127.0.0.1', 5000))
server.listen(1)
print("=== SERVER UNICAST (SINGLE THREAD) READY ===")
print("Menunggu koneksi dari client...\n")

while True:
    # 3. Menerima koneksi dari Client
    conn, addr = server.accept()
    print(f"[TERHUBUNG] Koneksi diterima dari {addr}")
    
    try:
        # 4. Membaca HEADER/LABEL terlebih dahulu (dibatasi 1024 bytes)
        header = conn.recv(1024).decode('utf-8')
        
        # Memisahkan string berdasarkan karakter '|'
        # Format header: JENIS|NAMA_FILE|UKURAN
        jenis, nama_file, ukuran = header.split('|')
        ukuran = int(ukuran)
        
        print(f"[INFO] Menerima data jenis: {jenis}, Ukuran: {ukuran} bytes")
        
        # 5. EKSEKUSI BERDASARKAN JENIS DATA
        if jenis == "TEKS":
            # Jika teks, langsung terima sisa datanya sesuai ukuran dan decode ke string
            data_teks = conn.recv(ukuran).decode('utf-8')
            print(f"[PESAN TERIMA] Isi Teks:\n{data_teks}\n")
            
        elif jenis == "FILE":
            # Jika file, kita buat file baru di folder server dengan awalan 'terima_'
            nama_file_baru = f"terima_{nama_file}"
            
            print(f"[MENGUNDUH] Sedang mengunduh file {nama_file}...")
            with open(nama_file_baru, "wb") as f:
                terbaca = 0
                # Lakukan perulangan (buffering) sampai seluruh ukuran file terpenuhi
                while terbaca < ukuran:
                    chunk = conn.recv(4096) # Baca per 4KB
                    if not chunk:
                        break
                    f.write(chunk)
                    terbaca += len(chunk)
                    
            print(f"[SUKSES] File berhasil disimpan dengan nama: {nama_file_baru}\n")
            
    except Exception as e:
        print(f"[ERROR] Terjadi kesalahan: {e}")
        
    finally:
        # 6. Tutup koneksi dengan client saat ini agar server bisa menerima client berikutnya
        conn.close()
        print("[TERPUTUS] Koneksi dengan client ditutup. Menunggu koneksi baru...\n")
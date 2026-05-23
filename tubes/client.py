import socket
import os

def kirim_data():
    # 1. Inisialisasi Socket TCP dan hubungkan ke Server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect(('127.0.0.1', 5000))
    except Exception as e:
        print(f"Gagal terhubung ke server: {e}")
        return

    print("\n=== MENU PENGIRIMAN UNICAST ===")
    print("1. Kirim Teks (1-5 Kata / Kalimat / Paragraf)")
    print("2. Kirim File (TXT, DOCX, PDF, JPG, PNG, MP3, MP4)")
    pilihan = input("Pilih menu (1/2): ")

    if pilihan == "1":
        # === PROSES KIRIM TEKS ===
        pesan = input("\nMasukkan teks yang ingin dikirim:\n")
        ukuran_pesan = len(pesan.encode('utf-8'))
        
        # Buat label header: TEKS|nama_file_kosong|ukuran
        header = f"TEKS|none|{ukuran_pesan}"
        
        # Kirim header dulu, baru kirim teksnya
        client.send(header.encode('utf-8'))
        # Beri jeda sangat singkat/pastikan data terpisah (opsional, aman di TCP)
        client.send(pesan.encode('utf-8'))
        print("[SUKSES] Teks berhasil dikirim!")

    elif pilihan == "2":
        # === PROSES KIRIM FILE ===
        path_file = input("\nMasukkan nama file beserta ekstensinya (contoh: foto.jpg, lagu.mp3, video.mp4):\n")
        
        # Cek apakah file benar-benar ada di folder
        if not os.path.exists(path_file):
            print("[ERROR] File tidak ditemukan! Pastikan file berada di folder yang sama.")
            client.close()
            return
            
        nama_file = os.path.basename(path_file)
        ukuran_file = os.path.getsize(path_file)
        
        # Buat label header: FILE|nama_file|ukuran
        header = f"FILE|{nama_file}|{ukuran_file}"
        
        # Kirim header terlebih dahulu
        client.send(header.encode('utf-8'))
        
        # Buka file dalam mode 'rb' (Read Binary) lalu kirim seluruh isinya
        print(f"Sedang mengirim {nama_file} ({ukuran_file} bytes)...")
        with open(path_file, "rb") as f:
            client.sendall(f.read())
        print("[SUKSES] File berhasil dikirim!")
        
    else:
        print("Pilihan tidak valid.")

    client.close()

if __name__ == "__main__":
    while True:
        kirim_data()
        tanya = input("\nIngin mengirim data lagi? (y/n): ")
        if tanya.lower() != 'y':
            break
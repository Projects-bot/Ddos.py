# UJICOBA WEBSITE SERANGAN (Script DDoS Simulasi)

> **DISCLAIMER:** Script ini hanya untuk *pengujian pribadi* terhadap server milik sendiri. Jangan digunakan untuk menyerang sistem yang bukan milikmu tanpa izin, karena itu **melanggar hukum**.

---

## Fitur
- Simulasi serangan DDoS HTTP GET untuk pengujian
- Multi-threading
- Logging ke file `log_ddos.txt`
- Menu CLI interaktif
- Bisa dihentikan sewaktu-waktu
- Banner berwarna + ASCII art tengkorak

---

## Cara Install dan Jalankan di Termux

### 1. **Update Termux dan install Python**
```bash
pkg update && pkg upgrade
pkg install python git

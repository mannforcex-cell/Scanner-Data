# 🛡️ Mann Force X — Virus Scanner

Tool ringan untuk Termux yang mengimbas fail dalam telefon Android anda menggunakan enjin **VirusTotal** (70+ antivirus sekaligus). Kira hash fail dan semak dengan pangkalan data malware — tanpa muat naik fail, jadi privasi anda terjaga.

## ✨ Ciri-ciri

- Banner & antara muka berwarna
- Pilihan jenis fail: APK, dokumen, gambar, arkib, atau semua sekaligus
- Animasi loading (spinner)
- Progress counter semasa imbasan
- Output berwarna: 🔴 bahaya / 🟢 selamat
- Ringkasan akhir jumlah fail berbahaya

## 📦 Pemasangan

\`\`\`bash
# 1. Kemas kini Termux & pasang Python
pkg update && pkg upgrade -y
pkg install python git -y

# 2. Pasang library yang diperlukan
pip install requests

# 3. Bagi Termux akses storan telefon
termux-setup-storage

# 4. Clone repo ini
git clone https://github.com/mannforcex-cell/Scanner-Data.git
cd Scanner-Data
\`\`\`

## 🔑 Cara Dapatkan API Key VirusTotal (Percuma)

1. Pergi ke [virustotal.com](https://www.virustotal.com) dan klik **Sign up**
2. Daftar akaun percuma (guna email)
3. Sahkan email anda
4. Log masuk, klik ikon profil di penjuru atas kanan
5. Pilih **API key** dari menu
6. Salin kunci yang dipaparkan
7. Buka fail script, cari baris ini dan tampal kunci anda:

\`\`\`python
API_KEY = "MASUKKAN_API_KEY_VIRUSTOTAL_ANDA"
\`\`\`

> ⚠️ **Nota:** Akaun percuma terhad kepada 4 permintaan seminit. Script ini sudah ada jeda 15 saat antara fail untuk mematuhi had ini. Jangan kongsi API key anda secara terbuka.

## ▶️ Cara Guna

\`\`\`bash
python mannforcex.py
\`\`\`

Kemudian:
1. Masukkan laluan folder (cth: \`/sdcard/Download\`)
2. Pilih jenis fail untuk diimbas
3. Tunggu hasil imbasan

## 📋 Keperluan

- Termux (dari F-Droid — versi Play Store sudah lapuk)
- Python 3.x
- Sambungan internet
- API key VirusTotal (percuma)

## ⚖️ Penafian

Tool ini untuk **kegunaan peribadi** mengimbas fail anda sendiri. Hasil bergantung pada pangkalan data VirusTotal — fail baharu yang belum direkod mungkin dipaparkan sebagai "tiada rekod". Ini bukan ganti untuk antivirus komersial yang lengkap.

## 📄 Lesen

MIT License — bebas guna dan ubah suai.

## 🔗 Tool Berkaitan (Untuk Pembelajaran Keselamatan Siber)

Repo-repo sah yang bagus untuk belajar tentang keselamatan & analisis fail:

- **[ClamAV](https://github.com/Cisco-Talos/clamav)** — Enjin antivirus open-source rasmi
- **[YARA](https://github.com/VirusTotal/yara)** — Tool corak untuk kenal pasti & klasifikasi malware (dari pasukan VirusTotal sendiri)
- **[VirusTotal API Docs](https://github.com/VirusTotal/vt-py)** — Library Python rasmi VirusTotal
- **[OWASP Cheat Sheet](https://github.com/OWASP/CheatSheetSeries)** — Panduan amalan keselamatan terbaik
- **[Hashdeep](https://github.com/jessek/hashdeep)** — Tool pengiraan & pengesahan hash fail

> 📚 Tool-tool ini untuk tujuan pembelajaran dan pertahanan (defensive security) sahaja.

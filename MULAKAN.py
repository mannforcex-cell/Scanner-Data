import os
import hashlib
import requests
import time
import sys

# ===== KONFIGURASI =====
API_KEY = "MASUKKAN_API_KEY_VIRUSTOTAL_ANDA"

# Warna terminal
class C:
    R = "\033[91m"; G = "\033[92m"; Y = "\033[93m"
    B = "\033[94m"; CY = "\033[96m"; W = "\033[97m"
    BOLD = "\033[1m"; END = "\033[0m"

def banner():
    print(C.CY + C.BOLD + r"""
   __  ___                 ____                   _  __
  /  |/  /__ ____  ___    / __/__  ___________   | |/_/
 / /|_/ / _ `/ _ \/ _ \  / _// _ \/ __/ __/ -_) _>  <  
/_/  /_/\_,_/_//_/_//_/ /_/  \___/_/  \__/\__/ /_/|_|  
""" + C.END)
    print(C.Y + "        [ Mann Force X — Virus Scanner ]" + C.END)
    print(C.W + "        Powered by VirusTotal Engine\n" + C.END)

def loading(msg, secs=2):
    frames = ["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏"]
    end = time.time() + secs
    i = 0
    while time.time() < end:
        sys.stdout.write(f"\r{C.G}{frames[i % len(frames)]} {msg}{C.END}")
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    sys.stdout.write(f"\r{C.G}✓ {msg} — selesai{C.END}\n")

# ===== FUNGSI SCAN =====
EXTENSIONS = {
    "1": ("APK / Aplikasi", [".apk", ".xapk"]),
    "2": ("Dokumen", [".pdf", ".doc", ".docx", ".xls", ".xlsx"]),
    "3": ("Gambar", [".jpg", ".jpeg", ".png", ".gif"]),
    "4": ("Arkib", [".zip", ".rar", ".7z"]),
    "5": ("Semua fail", None),
}

def get_file_hash(filepath):
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        for block in iter(lambda: f.read(4096), b""):
            sha256.update(block)
    return sha256.hexdigest()

def check_virustotal(file_hash):
    url = f"https://www.virustotal.com/api/v3/files/{file_hash}"
    headers = {"x-apikey": API_KEY}
    try:
        r = requests.get(url, headers=headers, timeout=30)
        if r.status_code == 200:
            stats = r.json()["data"]["attributes"]["last_analysis_stats"]
            return stats["malicious"], stats["suspicious"]
    except requests.RequestException:
        pass
    return None, None

def collect_files(folder, exts):
    found = []
    for root, dirs, files in os.walk(folder):
        for name in files:
            if exts is None or os.path.splitext(name)[1].lower() in exts:
                found.append(os.path.join(root, name))
    return found

def scan(folder, exts):
    loading("Mengumpul senarai fail", 2)
    files = collect_files(folder, exts)
    total = len(files)
    if total == 0:
        print(C.Y + "\nTiada fail yang sepadan dijumpai." + C.END)
        return

    print(C.W + f"\nJumlah fail untuk discan: {total}\n" + C.END)
    bahaya = 0

    for idx, path in enumerate(files, 1):
        name = os.path.basename(path)
        sys.stdout.write(f"\r{C.B}[{idx}/{total}] Memproses: {name[:30]}...{C.END}")
        sys.stdout.flush()
        try:
            h = get_file_hash(path)
            mal, sus = check_virustotal(h)
            print()  # baris baru
            if mal is None:
                print(f"  {C.Y}[?] {name} — tiada rekod / fail baharu{C.END}")
            elif mal > 0:
                print(f"  {C.R}{C.BOLD}[!] BAHAYA: {name} — {mal} enjin tanda malicious{C.END}")
                bahaya += 1
            else:
                print(f"  {C.G}[OK] {name} — selamat{C.END}")
            time.sleep(15)  # had API percuma: 4 permintaan/minit
        except Exception as e:
            print(f"\n  {C.R}[X] Ralat baca {name}: {e}{C.END}")

    print(C.CY + "\n" + "="*45 + C.END)
    print(C.BOLD + f" Imbasan selesai — {bahaya} fail berbahaya dikesan" + C.END)
    print(C.CY + "="*45 + C.END)

def main():
    os.system("clear")
    banner()
    folder = input(C.W + "Masukkan laluan folder [/sdcard/Download]: " + C.END).strip()
    if not folder:
        folder = "/sdcard/Download"
    if not os.path.isdir(folder):
        print(C.R + "Folder tidak wujud." + C.END)
        return

    print(C.W + "\nPilih jenis fail untuk discan:" + C.END)
    for k, (label, _) in EXTENSIONS.items():
        print(f"  {C.G}[{k}]{C.END} {label}")
    choice = input(C.W + "\nPilihan anda: " + C.END).strip()

    if choice not in EXTENSIONS:
        print(C.R + "Pilihan tidak sah." + C.END)
        return

    label, exts = EXTENSIONS[choice]
    print(C.Y + f"\nMod: {label}" + C.END)
    loading("Memulakan enjin imbasan", 2)
    scan(folder, exts)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(C.R + "\n\nImbasan dibatalkan oleh pengguna." + C.END)

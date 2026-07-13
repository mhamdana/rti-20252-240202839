import time
import os
import psutil
import pandas as pd
from playwright.sync_api import sync_playwright

# 1. DAFTAR 40 URL WEB SESUAI KASUS KAMU
URLS = [
    "https://www.youtube.com", "https://www.facebook.com", "https://www.instagram.com",
    "https://www.tiktok.com", "https://x.com", "https://www.reddit.com",
    "https://www.pinterest.com", "https://www.linkedin.com", "https://www.mixcloud.com",
    "https://www.snapchat.com", "https://www.twitch.tv", "https://www.quora.com",
    "https://id.wikipedia.org", "https://github.com", "https://www.tumblr.com",
    "https://medium.com", "https://www.threads.net", "https://substack.com",
    "https://www.bilibili.tv", "https://www.messenger.com", "https://mastodon.social",
    "https://bsky.app", "https://kick.com", "https://www.pixiv.net",
    "https://www.dailymotion.com", "https://soundcloud.com", "https://bandcamp.com",
    "https://www.wattpad.com", "https://www.behance.net", "https://dribbble.com",
    "https://www.artstation.com", "https://www.deviantart.com", "https://www.flickr.com",
    "https://www.producthunt.com", "https://www.goodreads.com", "https://myanimelist.net",
    "https://letterboxd.com", "https://itch.io", "https://imgur.com", "https://steamcommunity.com"
]

TOTAL_REPEATS = 5     # Jumlah pengulangan tes
WAIT_TIME = 180          # Jeda tunggu halaman stabil (3 menit / 180 detik)
COOLDOWN_TIME = 60       # Jeda kosongkan RAM sebelum tes berikutnya (1 menit)

def hitung_ram_proses(nama_proses):
    """Menghitung total RAM (dalam MB) dari seluruh proses browser yang aktif"""
    total_rss = 0
    for proc in psutil.process_iter(['name', 'memory_info']):
        try:
            # Mengecek nama proses (chrome atau firefox)
            if nama_proses in proc.info['name'].lower():
                total_rss += proc.info['memory_info'].rss
        except (psutil.NoSuchProcess, psutil.AccessDenied, proc.ZombieProcess):
            continue
    return round(total_rss / (1024 * 1024), 2) # Mengubah bytes ke MB

def jalankan_eksperimen(tipe_browser, nama_proses, file_output):
    hasil_data = []
    
    print(f"#=== MEMULAI PENGUJIAN INTERNAL {tipe_browser.upper()} ===#")
    
    with sync_playwright() as p:
        # Pilih mesin browser bawaan playwright
        browser_type = getattr(p, tipe_browser)
        
        for loop in range(1, TOTAL_REPEATS + 1):
            print(f"\n[Run {loop}/{TOTAL_REPEATS}] Membuka browser...")
            
            # Membuka dengan opsi bebas dari cache lama (Clean State)
            if tipe_browser == "chromium":
                browser = browser_type.launch(headless=False, channel="chrome")
            else:
                browser = browser_type.launch(headless=False)
                
            context = browser.new_context()
            page = context.new_page()
            
            print(f"[Run {loop}] Membuka 5 tab secara bertahap...")
            # Buka URL pertama di tab pertama
            try:
                page.goto(URLS[0], timeout=60000)
            except Exception:
                pass
                
            # Buka 39 URL sisanya di tab baru
            for url in URLS[1:]:
                try:
                    new_tab = context.new_page()
                    new_tab.goto(url, timeout=60000)
                except Exception:
                    continue 
            
            print(f"[Run {loop}] Semua tab selesai diperintahkan. Menunggu {WAIT_TIME} detik agar status web stabil...")
            time.sleep(WAIT_TIME)
            
            # Mengambil data RAM dari OS
            ram_terpakai = hitung_ram_proses(nama_proses)
            print(f"--> [HASIL Run {loop}] Total RAM {tipe_browser.upper()}: {ram_terpakai} MB")
            
            hasil_data.append({
                "Pengujian Ke": loop,
                "Total RAM (MB)": ram_terpakai
            })
            
            # Tutup total browser untuk membersihkan memori
            print(f"[Run {loop}] Menutup browser dan membersihkan memori...")
            browser.close()
            
            # Jeda istirahat sistem operasi sebelum pengulangan berikutnya
            if loop < TOTAL_REPEATS:
                print(f"Menunggu jeda pendinginan OS selama {COOLDOWN_TIME} detik...")
                time.sleep(COOLDOWN_TIME)
                
    # Simpan hasil akhir satu browser ke file Excel
    df = pd.DataFrame(hasil_data)
    df.to_excel(file_output, index=False)
    print(f"\n[SELESAI] Data sukses disimpan ke {file_output}")

# --- EKSEKUSI ---
if __name__ == "__main__":
    # KELOMPOK 1: UJI CHROME
    jalankan_eksperimen(tipe_browser="firefox", nama_proses="firefox", file_output="Hasil_RAM_Firefox_5x.xlsx")
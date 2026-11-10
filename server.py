import socket
import http.server
import socketserver
import os
import sys

PORT = 8080

def get_lan_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

ip = get_lan_ip()
url = f"http://{ip}:{PORT}"

print("=" * 65)
print("       ỨNG DỤNG HỌC TIẾNG INDONESIA — BIPA COURSE")
print("=" * 65)
print(f"\n[+] May chu da khoi dong thanh cong!")
print(f"[+] Tren may tinh: http://localhost:{PORT}")
print(f"\n[+] HUONG DAN CHAY TREN DIEN THOAI (Android / iPhone):")
print(f"    1. Ket noi dien thoai chung Wi-Fi voi may tinh nay.")
print(f"    2. Mo trinh duyet tren dien thoai (Chrome / Safari / Coc Coc).")
print(f"    3. Nhap dia chi sau:")
print(f"\n       👉  {url}  👈\n")
print(f"[+] MEO CAI DAT THANH APP:")
print(f"    - Android (Chrome): Bam 3 cham -> 'Cai dat ung dung' (Add to Home screen).")
print(f"    - iPhone (Safari): Bam Chia se (hinh vuong mui ten) -> 'Them vao MH chinh'.")
print(f"    -> Se co icon BIPA rieng ngoai man hinh, chay toan man hinh nhu App that!\n")
print("=" * 65)
print("Nhan Ctrl + C de dung may chu khi hoc xong.")
print("=" * 65)

os.chdir(os.path.dirname(os.path.abspath(__file__)))
Handler = http.server.SimpleHTTPRequestHandler

# Allow address reuse
socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nDa dung may chu.")

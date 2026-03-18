import requests
import random
import string
import time

GREEN = "\033[92m"
RESET = "\033[0m"

def generate_username(length=4):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def check_availability(username):
    url = f"https://www.tiktok.com/@{username}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    try:
        response = requests.get(url, headers=headers, timeout=3)
        return response.status_code == 404
    except:
        return False

def save(username):
    with open("available.txt", "a") as f:
        f.write(f"@{username}\n")

def main():
    print("🚀 RIMI TURBO – Super Fast Username Sniper")
    found = 0

    try:
        while True:
            user = generate_username(length=4)  # تقدر تحط 3 لو تبي أسرع وأكثر متوفر
            if check_availability(user):
                print(f"{GREEN}[✓] Available: @{user} ✔{RESET}")
                save(user)
                found += 1
            time.sleep(0.2)  # تيربو 😂
    except KeyboardInterrupt:
        print(f"\n🛑 انتهى الفحص. تم إيجاد {found} يوزر.")
        print("📁 Saved in: available.txt")
        exit()

main()

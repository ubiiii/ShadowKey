import re
import getpass
from colorama import Fore, Style, init

# ✅ Initialize colorama
init(autoreset=True)

def check_password_strength(password):
    length = len(password) >= 8
    upper = re.search(r'[A-Z]', password) is not None
    lower = re.search(r'[a-z]', password) is not None
    digit = re.search(r'\d', password) is not None
    symbol = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    score = sum([length, upper, lower, digit, symbol])

    if score == 5:
        return "Very Strong", Fore.GREEN
    elif score == 4:
        return "Strong", Fore.GREEN
    elif score == 3:
        return "Moderate", Fore.YELLOW
    elif score == 2:
        return "Weak", Fore.RED
    else:
        return "Very Weak", Fore.RED

# --- Main Execution ---
print("🔐 Welcome to ShadowKey - Password Strength Checker\n")
password = getpass.getpass("Enter your password (input hidden): ")

strength, color = check_password_strength(password)
print(f"\n🧠 Password Strength: {color}{strength}{Style.RESET_ALL}")

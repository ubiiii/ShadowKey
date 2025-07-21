from flask import Flask, render_template, request, jsonify
import re
import math
import random
import string

app = Flask(__name__)  # 🔧 Create the Flask app


@app.route('/generate-password', methods=['POST'])
def generate_password():

    data = request.json
    length = int(data.get('length', 12))
    use_upper = data.get('uppercase', True)
    use_lower = data.get('lowercase', True)
    use_digits = data.get('numbers', True)
    use_symbols = data.get('symbols', True)

    selected_sets = []
    guaranteed_chars = []

    if use_upper:
        selected_sets.append(string.ascii_uppercase)
        guaranteed_chars.append(random.choice(string.ascii_uppercase))
    if use_lower:
        selected_sets.append(string.ascii_lowercase)
        guaranteed_chars.append(random.choice(string.ascii_lowercase))
    if use_digits:
        selected_sets.append(string.digits)
        guaranteed_chars.append(random.choice(string.digits))
    if use_symbols:
        selected_sets.append(string.punctuation)
        guaranteed_chars.append(random.choice(string.punctuation))

    if not selected_sets:
        return jsonify({'error': 'No character sets selected!'}), 400

    # Fill the rest of the password length with random characters from all selected sets
    all_chars = ''.join(selected_sets)
    remaining_length = length - len(guaranteed_chars)
    if remaining_length < 0:
        return jsonify({'error': 'Length too short for selected options!'}), 400

    password_chars = guaranteed_chars + [random.choice(all_chars) for _ in range(remaining_length)]
    random.shuffle(password_chars)

    return jsonify({'password': ''.join(password_chars)})


def estimate_crack_time(password):
    charset = 0
    if re.search(r'[a-z]', password): charset += 26
    if re.search(r'[A-Z]', password): charset += 26
    if re.search(r'\d', password): charset += 10
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password): charset += 32  # Approx number of common symbols

    guesses_per_sec = 1_000_000_000  # 1 billion guesses/second (fast GPU)
    total_combinations = charset ** len(password)

    # Avoid math overflow for super long passwords
    try:
        seconds = total_combinations / guesses_per_sec
    except OverflowError:
        return "∞ (Too long to crack)"
    
    return format_time(seconds)

def format_time(seconds):
    units = [("year", 60*60*24*365), ("day", 60*60*24), ("hour", 60*60), ("minute", 60), ("second", 1)]
    result = []
    for name, count in units:
        value = int(seconds // count)
        if value:
            seconds -= value * count
            result.append(f"{value} {name}{'s' if value > 1 else ''}")
    return ', '.join(result) if result else "less than 1 second"

# 🔍 Password checker logic
def analyze_password(password):
    rules = {
        "Length ≥ 8": len(password) >= 8,
        "Uppercase letter": re.search(r'[A-Z]', password) is not None,
        "Lowercase letter": re.search(r'[a-z]', password) is not None,
        "Digit": re.search(r'\d', password) is not None,
        "Special character": re.search(r'[!@#$%^&*(),.?\":{}|<>]', password) is not None
    }

    score = sum(rules.values())

    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return rules, strength

# 🌐 Route: Home Page
@app.route('/')
def index():
    return render_template('index.html')  # Will create this next

# 🔐 Route: Password Check API
@app.route('/check-password', methods=['POST'])
def check_password():
    data = request.json
    password = data.get('password', '')
    rules, strength = analyze_password(password)
    crack_time = estimate_crack_time(password)  # Add this line

    return jsonify({
        'strength': strength,
        'rules': rules,
        'crack_time': crack_time  # And include it here
    })

# 🚀 Run the app
if __name__ == '__main__':
    app.run(debug=True)

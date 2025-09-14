import streamlit as st
import re
import math
import random
import string

st.set_page_config(
    page_title="🔐 ShadowKey",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for hacker theme
st.markdown("""
<style>
    .main {
        background-color: #0d1117;
        color: #c9d1d9;
    }
    .stApp {
        background-color: #0d1117;
    }
    .stTextInput > div > div > input {
        background-color: #21262d;
        color: #c9d1d9;
        border: 1px solid #30363d;
    }
    .stTextInput > div > div > input:focus {
        border-color: #58a6ff;
        box-shadow: 0 0 0 2px rgba(88, 166, 255, 0.3);
    }
    .stButton > button {
        background-color: #238636;
        color: white;
        border: none;
        border-radius: 6px;
        font-weight: 500;
    }
    .stButton > button:hover {
        background-color: #2ea043;
    }
    .stSelectbox > div > div > select {
        background-color: #21262d;
        color: #c9d1d9;
        border: 1px solid #30363d;
    }
    .stSlider > div > div > div > div {
        background-color: #58a6ff;
    }
    .stCheckbox > div > div > div > label {
        color: #c9d1d9;
    }
    .stMarkdown {
        color: #c9d1d9;
    }
    .strength-strong { color: #3fb950; }
    .strength-moderate { color: #d29922; }
    .strength-weak { color: #f85149; }
    .password-display {
        font-family: 'Courier New', monospace;
        background-color: #21262d;
        padding: 10px;
        border-radius: 6px;
        border: 1px solid #30363d;
        word-break: break-all;
        user-select: all;
    }
</style>
""", unsafe_allow_html=True)

def estimate_crack_time(password):
    charset = 0
    if re.search(r'[a-z]', password): charset += 26
    if re.search(r'[A-Z]', password): charset += 26
    if re.search(r'\d', password): charset += 10
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password): charset += 32

    guesses_per_sec = 1_000_000_000  # 1 billion guesses/second
    total_combinations = charset ** len(password)

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

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
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
        return "Error: No character sets selected!"

    all_chars = ''.join(selected_sets)
    remaining_length = length - len(guaranteed_chars)
    if remaining_length < 0:
        return "Error: Length too short for selected options!"

    password_chars = guaranteed_chars + [random.choice(all_chars) for _ in range(remaining_length)]
    random.shuffle(password_chars)

    return ''.join(password_chars)

# Main app
st.title("🔐 ShadowKey")
st.markdown("**Password Security Toolkit** - Check strength, estimate crack time, and generate secure passwords")

# Create two columns
col1, col2 = st.columns([1, 1])

with col1:
    st.header("🔍 Password Strength Checker")
    
    password = st.text_input(
        "Enter your password to analyze:",
        type="password",
        placeholder="••••••••",
        help="Your password will not be stored or transmitted anywhere"
    )
    
    if st.button("Check Strength", type="primary"):
        if password:
            rules, strength = analyze_password(password)
            crack_time = estimate_crack_time(password)
            
            # Display strength with color
            if strength in ["Very Strong", "Strong"]:
                st.markdown(f"**Strength:** <span class='strength-strong'>{strength}</span>", unsafe_allow_html=True)
            elif strength == "Moderate":
                st.markdown(f"**Strength:** <span class='strength-moderate'>{strength}</span>", unsafe_allow_html=True)
            else:
                st.markdown(f"**Strength:** <span class='strength-weak'>{strength}</span>", unsafe_allow_html=True)
            
            # Display rules checklist
            st.markdown("**Security Checklist:**")
            for rule, passed in rules.items():
                if passed:
                    st.markdown(f"✅ {rule}")
                else:
                    st.markdown(f"❌ {rule}")
            
            # Display crack time
            st.markdown(f"**Estimated Crack Time:** {crack_time}")
        else:
            st.warning("Please enter a password to check")

with col2:
    st.header("🔧 Password Generator")
    
    # Password length slider
    length = st.slider("Password Length", min_value=4, max_value=64, value=12, step=1)
    
    # Character set options
    st.markdown("**Character Sets:**")
    use_upper = st.checkbox("Include Uppercase (A-Z)", value=True)
    use_lower = st.checkbox("Include Lowercase (a-z)", value=True)
    use_digits = st.checkbox("Include Numbers (0-9)", value=True)
    use_symbols = st.checkbox("Include Symbols (!@#$...)", value=True)
    
    # Ensure at least one character set is selected
    if not any([use_upper, use_lower, use_digits, use_symbols]):
        st.error("Please select at least one character set!")
        use_lower = True  # Default fallback
    
    if st.button("Generate Password", type="secondary"):
        generated_password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
        
        if not generated_password.startswith("Error"):
            st.markdown("**Generated Password:**")
            st.markdown(f'<div class="password-display">{generated_password}</div>', unsafe_allow_html=True)
            
            # Copy button functionality
            if st.button("📋 Copy to Clipboard"):
                st.code(generated_password)
                st.success("Password copied! (Click on the code above to select all)")
        else:
            st.error(generated_password)

# Sidebar with additional info
with st.sidebar:
    st.header("ℹ️ About ShadowKey")
    st.markdown("""
    **ShadowKey** is a password security toolkit that helps you:
    
    - ✅ Check password strength
    - ⏱️ Estimate crack time
    - 🔧 Generate secure passwords
    - 🛡️ Improve security practices
    
    **Security Note:** All analysis is done locally in your browser. No passwords are stored or transmitted.
    """)
    
    st.header("🔒 Security Tips")
    st.markdown("""
    - Use at least 12 characters
    - Include mixed case, numbers, and symbols
    - Avoid common words and patterns
    - Use unique passwords for each account
    - Consider using a password manager
    """)
    
    st.header("📊 Strength Levels")
    st.markdown("""
    - **Very Strong:** 5/5 criteria met
    - **Strong:** 4/5 criteria met  
    - **Moderate:** 3/5 criteria met
    - **Weak:** 2/5 criteria met
    - **Very Weak:** 1/5 criteria met
    """)

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666; font-size: 0.9em;'>
        <p>🔐 <strong>ShadowKey</strong> - Password Security Toolkit</p>
        <p>Made with ❤️ for security-conscious users</p>
    </div>
    """, 
    unsafe_allow_html=True
)

import re

def check_password_strength(password):
    length_error = len(password) < 8
    lowercase_error = re.search(r"[a-z]", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    score = 5 - sum([length_error, lowercase_error, uppercase_error, digit_error, special_char_error])

    if score <= 2:
        strength = "Weak"
    elif 3 <= score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    print(f"Password Strength: {strength}")

    # Detailed feedback (optional)
    if length_error:
        print("- Password should be at least 8 characters long.")
    if lowercase_error:
        print("- Include at least one lowercase letter.")
    if uppercase_error:
        print("- Include at least one uppercase letter.")
    if digit_error:
        print("- Include at least one number.")
    if special_char_error:
        print("- Include at least one special character (!@#$%^&* etc).")

# Example usage
password = input("Enter your password: ")
check_password_strength(password)

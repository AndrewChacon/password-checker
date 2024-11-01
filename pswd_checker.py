import re

def password_strength(password):
    score = 0
    strength = ''

    # check length of password
    if len(password) >= 12: score += 2
    elif len(password) >= 8: score += 1

    # check for uppercase letters
    if re.search(r'[A-Z]', password): score += 1

    # check for lowercase letters
    if re.search(r'[a-z]', password): score += 1

    # check for special characters
    if re.search(r'[@$!%*?&#]', password): score += 1

    # check at least one digit (0-9)
    if re.search(r'\d', password): score += 1
    
    # check password against common words or patterns
    common_patterns = ['password', '1234', 'qwerty', 'abcd']
    if any(pattern in password for pattern in common_patterns):
        socre -= 1

    if score >= 5: strength = "Strong"
    elif score >= 3: strength = "Moderate"
    else: strength = "Weak"

    print("Password Score:", score)
    print("Password Strength:", strength)

password_strength("YourPassWord123!")


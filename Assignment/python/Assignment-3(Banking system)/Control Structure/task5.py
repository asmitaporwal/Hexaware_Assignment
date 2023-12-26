def validate_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    
    has_upper = any(char.isupper() for char in password)
    if not has_upper:
        return False, "Password must contain at least one uppercase letter."
    
    has_digit = any(char.isdigit() for char in password)
    if not has_digit:
        return False, "Password must contain at least one digit."
    
    return True, "Password is valid!"


user_password = input("Create your password: ")
is_valid, message = validate_password(user_password)
print(message)
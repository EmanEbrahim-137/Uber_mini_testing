import hashlib

# Helper Functions

def hash_password(password: str) -> str:
    if not password:
        raise ValueError("Password cannot be empty")

    return hashlib.sha256(password.encode()).hexdigest()


def verify_password(password: str, hashed_password: str) -> bool:
    return hash_password(password) == hashed_password

# User Functions

def register_user(email: str, password: str, users_db: dict) -> dict:
    if not email or not password:
        raise ValueError("Email and password are required")

    if email in users_db:
        raise ValueError("User already exists")

    users_db[email] = {
        "email": email,
        "password": hash_password(password)
    }
    return users_db[email]


def login_user(email: str, password: str, users_db: dict) -> bool:
    if email not in users_db:
        return False

    return verify_password(password, users_db[email]["password"])

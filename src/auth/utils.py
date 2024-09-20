from passlib.context import CryptContext

passwd_context = CryptContext(schemes=["bcrypt"])


ACCESS_TOKEN_EXPIRY = 3600


def generate_passwd_hash(password: str) -> str:
    hash = passwd_context.hash(password)

    return hash
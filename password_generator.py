"""
Password Generator
Run: python password_generator.py
"""
import random, string

def generate(length=12, use_upper=True, use_digits=True, use_symbols=True):
    chars = list(string.ascii_lowercase)
    if use_upper: chars += list(string.ascii_uppercase)
    if use_digits: chars += list(string.digits)
    if use_symbols: chars += list("!@#$%^&*()-_=+[]{};:,.?/")
    if length < 4: raise ValueError("Use length >= 4")
    return "".join(random.choice(chars) for _ in range(length))

if __name__ == "__main__":
    print("Generated:", generate())

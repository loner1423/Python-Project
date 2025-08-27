"""
Simple CLI Calculator
Run: python calculator_cli.py
"""
def calc(expr):
    try:
        return eval(expr, {"__builtins__": {}}, {})
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    print("Enter expressions (e.g., 2+3*4). Type 'quit' to exit.")
    while True:
        s = input(">>> ").strip()
        if s.lower() == "quit": break
        print(calc(s))

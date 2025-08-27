"""
Currency Converter (API)
Requires: pip install requests
Usage: python currency_converter.py FROM TO AMOUNT
"""
import sys, requests
def convert(f,t,a):
    r=requests.get(f"https://api.exchangerate.host/convert?from={f}&to={t}&amount={a}")
    return r.json()["result"]
if __name__=="__main__":
    if len(sys.argv)<4: print("Usage: python currency_converter.py USD INR 100"); sys.exit(1)
    print(convert(sys.argv[1],sys.argv[2],float(sys.argv[3])))

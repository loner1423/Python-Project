"""
Alarm Clock (plays a beep in console)
Run: python alarm_clock.py HH:MM (24-hour)
"""
import sys, time, datetime, os

def beep():
    try:
        # Windows
        import winsound
        winsound.Beep(1000, 800)
    except Exception:
        # Cross-platform fallback
        print("\a", end="")

def main():
    if len(sys.argv) < 2:
        print("Usage: python alarm_clock.py HH:MM")
        sys.exit(1)
    target_str = sys.argv[1]
    today = datetime.date.today()
    hour, minute = map(int, target_str.split(":"))
    target = datetime.datetime(today.year, today.month, today.day, hour, minute)
    print(f"Alarm set for {target.strftime('%H:%M')}")
    while datetime.datetime.now() < target:
        time.sleep(1)
    for _ in range(5):
        beep(); time.sleep(0.5)
    print("Alarm!")

if __name__ == "__main__":
    main()

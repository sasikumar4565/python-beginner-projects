import time

print("===== COUNTDOWN TIMER =====")

seconds = 10

while seconds > 0:
    minutes = seconds // 60
    remaining_seconds = seconds % 60

    print(f"Time remaining: {minutes:02d}:{remaining_seconds:02d}")

    time.sleep(1)
    seconds -= 1

print("Time's up!")

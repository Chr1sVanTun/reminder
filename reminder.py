import time
import ctypes

MB_SETFOREGROUND = 0x00010000
MBeep = 0x00000000

amount = input("How many sets you want to perform? ")
minutes = float(input("How many minutes you want to rest between the sets? "))
print(f"Do your first Set, you will be remembered for the next {amount} sets")

for x in range(0, int(amount)):
    local_time = float(minutes * 60)
    time.sleep(local_time)
    MessageBeep = ctypes.windll.user32.MessageBeep(MBeep)
    MessageBox = ctypes.windll.user32.MessageBoxW
    MessageBox(None, 'Do 21 Air Squats, followed by 12 Push-Ups!!', 'Time for Training!', MB_SETFOREGROUND, 0)

import psutil
import time

print("gracias por jugar ;)")
time.sleep(2)

PROCNAME = "py.exe"

for proc in psutil.process_iter():
    if proc.name() == PROCNAME:
        proc.kill()

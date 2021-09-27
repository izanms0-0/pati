import psutil
print("gracias por jugar ;)")

PROCNAME = "py.exe"

for proc in psutil.process_iter():
    if proc.name() == PROCNAME:
        proc.kill()

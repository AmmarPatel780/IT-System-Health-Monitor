
import platform
import shutil
import os

print("=== IT System Health Checker ===")

print("Operating System:", platform.system())
print("OS Version:", platform.release())
print("Processor:", platform.processor())

total, used, free = shutil.disk_usage(
    os.path.expanduser("~")
)

print("Disk Total:", round(total / (1024**3), 2), "GB")
print("Disk Used:", round(used / (1024**3), 2), "GB")
print("Disk Free:", round(free / (1024**3), 2), "GB")

print("System check completed!")

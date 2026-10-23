
import platform
import psutil

print("=== IT SYSTEM HEALTH MONITOR ===")

print("\nSYSTEM INFORMATION")
print("Operating System:", platform.system(), platform.release())
print("Processor:", platform.processor())

print("\nCPU MONITORING")
cpu = psutil.cpu_percent(interval=1)
print(f"CPU Usage: {cpu}%")

print("\nMEMORY MONITORING")
ram = psutil.virtual_memory()
print(f"RAM Usage: {ram.percent}%")
print(f"Available RAM: {ram.available / (1024**3):.2f} GB")

print("\nDISK MONITORING")
disk = psutil.disk_usage("C:\\")
print(f"Disk Usage: {disk.percent}%")
print(f"Free Disk: {disk.free / (1024**3):.2f} GB")

print("\nSYSTEM HEALTH STATUS")
if cpu > 90 or ram.percent > 90 or disk.percent > 90:
    print("WARNING: High resource usage detected!")
else:
    print("System resources are within normal thresholds.")

print("\nMonitoring completed successfully!")

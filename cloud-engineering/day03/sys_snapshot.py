import subprocess, json, datetime

# Capture uptime and load
uptime = subprocess.check_output(["uptime"], text=True).strip()
load_avg = uptime.split("load average:")[-1].strip()

# Capture memory (in MB)
mem = subprocess.check_output(["free", "-m"], text=True).strip().split('\n')[1]
mem_stats = mem.split()
# mem_stats: [0:"Mem:", 1:"total", 2:"used", 3:"free", 4:"shared", 5:"buff/cache", 6:"available"]

# Build JSON
data = {
    "timestamp": datetime.datetime.now().isoformat(),
    "load_avg": load_avg,
    "mem_total_mb": int(mem_stats[1]),
    "mem_used_mb": int(mem_stats[2]),
    "mem_available_mb": int(mem_stats[6])
}

# Write to file
with open("system_snapshot.json", "w") as f:
    json.dump(data, f, indent=2)

print("✅ Snapshot written to system_snapshot.json")
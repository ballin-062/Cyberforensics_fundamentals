import subprocess
import os

# === Configure These ===
VOL_PATH = "C:\\PATH\\TO\\volatility3\\vol.py"    # Full path to your volatility3 vol.py
MEMORY_IMAGE = "C:\\Path\\To\\your_image.mem"     # Full path to your Windows memory dump
OUTPUT_DIR = "C:\\Path\\To\\analysis_output"      # Where you want logs saved

# === Volatility3 Plugins to Run ===
# IF target is LINUX, swap the 'windows.*' for 'linux.*' and see what happens....
commands = {
    "system_info": ["windows.info"],
    "hostname": ["windows.envars"],
    #"ip_addresses": ["windows.netscan"], DOESNT EXIST IN VOL3, USE VOL2.6
    "user_accounts": ["windows.getsids"],
    "command_history": ["windows.cmdscan"],
    "suspicious_processes": ["windows.malfind"],
    "process_tree": ["windows.psscan"],
    "process_list": ["windows.pslist"],
}

def run_volatility(plugin_name, plugin_args):
    log_file = os.path.join(OUTPUT_DIR, f"{plugin_name}.txt")
    command = ["python", VOL_PATH, "-f", MEMORY_IMAGE] + plugin_args
    try:
        with open(log_file, "w") as f:
            subprocess.run(command, stdout=f, stderr=subprocess.STDOUT, check=True)
        print(f"[+] {plugin_name} completed — output saved to {log_file}")
    except subprocess.CalledProcessError as e:
        print(f"[!] Error running {plugin_name}: {e}")

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    for plugin_name, plugin_args in commands.items():
        print(f"[*] Running {plugin_name}...")
        run_volatility(plugin_name, plugin_args)

if __name__ == "__main__":
    main()

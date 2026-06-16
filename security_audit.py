import os
import subprocess
import datetime

def run_windows_audit():
    print("==================================================")
    print("    🛡️  WINDOWS SYSTEM SECURITY AUDIT TOOL  🛡️   ")
    print("==================================================")
    print(f"Executed on: {datetime.datetime.now()}")
    print("--------------------------------------------------")

    print("\n[1] Checking Windows Firewall Status...")
    try:
        netsh_output = subprocess.check_output("netsh advfirewall show allprofiles state", shell=True).decode('utf-8', errors='ignore')
        if "ON" in netsh_output:
            print("[✔] SAFE: Windows Firewall is ENABLED on active profiles.")
        else:
            print("[❌ ALERT] VULNERABLE: Firewall might be DISABLED!")
    except Exception as e:
        print(f"[⚠️] Could not check Firewall status: {e}")

 
    print("\n[2] Scanning Active Listening Ports (ESTABLISHED/LISTENING)...")
    try:
        connections = subprocess.check_output("netstat -an | findstr LISTENING", shell=True).decode('utf-8', errors='ignore')
        print(connections[:500] + "\n... (Truncated for readability)")
    except Exception:
        print("[⚠️] No active listening ports captured or command failed.")

  
    print("\n[3] Checking Current User Context...")
    try:
        user = subprocess.check_output("whoami", shell=True).decode('utf-8').strip()
        print(f"[👤] Current User: {user}")
    except Exception:
        pass

    print("\n==================================================")
    print("          🛡️  END OF SECURITY AUDIT  🛡️          ")
    print("==================================================")

if __name__ == "__main__":
    run_windows_audit()
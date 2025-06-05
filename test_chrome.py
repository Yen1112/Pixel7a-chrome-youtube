import subprocess
import time

def adb(cmd):
    subprocess.run(["adb"] + cmd, check=True)

for i in range(100):
    print(f"[Chrome] Iteration {i+1}/100")
    adb(["shell", "am", "start", "-n", "com.android.chrome/com.google.android.apps.chrome.Main"])
    time.sleep(4)

    adb(["shell", "input", "tap", "540", "150"])
    time.sleep(1)

    adb(["shell", "input", "text", "Pixel%207a"])
    adb(["shell", "input", "keyevent", "66"])
    time.sleep(5)

    adb(["shell", "input", "keyevent", "3"])  # Return to home
    time.sleep(2)

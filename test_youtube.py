import subprocess
import time

def adb(cmd):
    subprocess.run(["adb"] + cmd, check=True)

for i in range(100):
    print(f"[YouTube] Iteration {i+1}/100")
    adb(["shell", "am", "start", "-n", "com.google.android.youtube/com.google.android.apps.youtube.app.WatchWhileActivity"])
    time.sleep(5)

    adb(["shell", "input", "tap", "540", "550"])  # First video area
    time.sleep(10)

    adb(["shell", "input", "keyevent", "3"])  # Return to home
    time.sleep(2)

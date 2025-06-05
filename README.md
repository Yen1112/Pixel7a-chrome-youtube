# Pixel 7a Chrome & YouTube Test Scripts (Repeat 100 Times)

These scripts automate Chrome and YouTube interactions and now repeat their actions 100 times for stress/reliability testing.

---

## Scripts Included

### ✅ `test_chrome.py`
- Launches Chrome
- Taps the address bar
- Searches for "cnn"
- Waits 5 seconds and returns to home
- Repeats the above 100 times

### ✅ `test_youtube.py`
- Launches YouTube
- Waits for home feed to load
- Taps on the first video
- Plays 10 seconds then returns home
- Repeats the above 100 times

---

## ⚙️ Requirements

- Pixel 7a
- USB debugging enabled
- Python 3.x + ADB installed

---

## 🚀 Run the scripts

```bash
python test_chrome.py
python test_youtube.py
```

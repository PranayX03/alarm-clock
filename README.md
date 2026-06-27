# ⏰ Alarm Clock

A Python alarm clock with a **Tkinter GUI**, live clock display, snooze functionality, and cross-platform sound support.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-blue?style=flat-square)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Mac%20%7C%20Linux-lightgrey?style=flat-square)

---

## ✨ Features

- 🖥️ Clean dark-themed GUI built with Tkinter
- 🕐 Live clock — shows current time updating every second
- ⏰ Set alarm using hour / minute / second dropdowns
- 💤 Snooze button — adds 5 minutes automatically
- ⛔ Stop button to cancel the alarm
- 🔊 Plays MP3 sound using `playsound` (works on Windows, Mac, Linux)
- 🧵 Uses threading — UI stays responsive while alarm runs in background

---

## 🛠️ Tech Used

- **Python 3.x**
- `tkinter` — built-in Python GUI library (no install needed)
- `pygame` — cross-platform audio playback
- `datetime` — to get and compare time
- `threading` — to run alarm loop without freezing the UI

---

## 📁 Project Structure

```
alarm-clock/
│
├── alarm_clock.py      # Main application
├── alarm_sound.mp3     # Sound file (add your own)
├── requirements.txt    # Dependencies
└── README.md
```

---

## ⚙️ Setup & Run

**1. Clone the repo**
```bash
git clone https://github.com/PranayX03/alarm-clock.git
cd alarm-clock
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Add a sound file**

Download any free `.mp3` from [freesound.org](https://freesound.org), rename it to `alarm_sound.mp3`, and place it in the project folder.

**4. Run**
```bash
python alarm_clock.py
```

---

## 🖼️ How to Use

1. Run the script — a window opens
2. Select your alarm time using the Hour / Minute / Second dropdowns
3. Click **Set Alarm** — the live clock starts ticking
4. When the alarm triggers, you'll hear the sound
5. Click **Snooze** to delay by 5 minutes, or **Stop** to cancel

---

## 📚 What I Learned

- Building GUI applications with Tkinter
- Using `threading` to prevent UI freezing
- Working with Python's `datetime` and `timedelta`
- Cross-platform audio playback with `pygame`
- Structuring a Python project with clean separation of logic and UI

---

## 🔮 Future Ideas

- [ ] Multiple alarms support
- [ ] Recurring daily alarm
- [ ] Custom snooze duration
- [ ] System tray minimization

---

*Part of my Python mini-projects series — [PranayX03](https://github.com/PranayX03)*

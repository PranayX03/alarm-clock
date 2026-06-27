from tkinter import *
from tkinter import messagebox
import datetime
import time
from threading import Thread
import pygame

# ── Main Window ────────────────────────────────────────────────
root = Tk()
root.title("Alarm Clock")
root.geometry("420x320")
root.resizable(False, False)
root.configure(bg="#1e1e2e")

# ── State variables ─────────────────────────────────────────────
alarm_running = False   # True while the alarm loop is active
alarm_ringing = False   # True when the alarm is currently going off

# ── Helper: pad numbers to 2 digits ─────────────────────────────
def two_digits(n):
    return [str(i).zfill(2) for i in range(n)]

# ── Alarm Logic ─────────────────────────────────────────────────
def start_alarm_thread():
    """Called when Set Alarm button is clicked."""
    global alarm_running
    if alarm_running:
        messagebox.showwarning("Already Running", "An alarm is already set!")
        return
    alarm_running = True
    status_label.config(text="⏳ Alarm is set...", fg="#a6e3a1")
    t = Thread(target=alarm_loop, daemon=True)
    t.start()

def alarm_loop():
    """Runs in background thread. Checks time every second."""
    global alarm_running, alarm_ringing
    target = f"{hour.get()}:{minute.get()}:{second.get()}"

    while alarm_running:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        # Update live clock on UI safely
        root.after(0, update_clock, now)

        if now == target:
            alarm_ringing = True
            root.after(0, on_alarm_trigger)   # update UI from main thread
            try:
                pygame.mixer.init()
                pygame.mixer.music.load("alarm_sound.mp3")
                pygame.mixer.music.play()  # plays the sound
            except Exception:
                root.after(0, lambda: status_label.config(
                    text="⚠️ Sound file not found!", fg="#f38ba8"))
            break

        time.sleep(1)

def on_alarm_trigger():
    """Updates the UI when alarm fires."""
    status_label.config(text="⏰ Wake up! Alarm is ringing!", fg="#f38ba8")
    snooze_btn.config(state=NORMAL)
    stop_btn.config(state=NORMAL)
    set_btn.config(state=DISABLED)

def snooze():
    """Adds 5 minutes to current time and restarts the alarm loop."""
    global alarm_running, alarm_ringing
    alarm_ringing = False
    alarm_running = False  # stop current loop

    # Calculate snooze time = now + 5 minutes
    snooze_time = datetime.datetime.now() + datetime.timedelta(minutes=5)
    h = snooze_time.strftime("%H")
    m = snooze_time.strftime("%M")
    s = snooze_time.strftime("%S")

    # Update the dropdowns to show snooze time
    hour.set(h)
    minute.set(m)
    second.set(s)

    status_label.config(text=f"💤 Snoozed until {h}:{m}:{s}", fg="#fab387")
    snooze_btn.config(state=DISABLED)
    stop_btn.config(state=DISABLED)
    set_btn.config(state=NORMAL)

    # Restart alarm with new time
    alarm_running = True
    t = Thread(target=alarm_loop, daemon=True)
    t.start()

def stop_alarm():
    """Stops the alarm completely."""
    global alarm_running, alarm_ringing
    alarm_running = False
    alarm_ringing = False
    status_label.config(text="✅ Alarm stopped.", fg="#a6e3a1")
    snooze_btn.config(state=DISABLED)
    stop_btn.config(state=DISABLED)
    set_btn.config(state=NORMAL)

def update_clock(now):
    """Updates the live clock label."""
    live_clock.config(text=f"🕐 {now}")

# ── UI Layout ───────────────────────────────────────────────────

# Title
Label(root, text="⏰ Alarm Clock",
      font=("Helvetica", 22, "bold"),
      bg="#1e1e2e", fg="#cba6f7").pack(pady=(18, 4))

# Live clock display
live_clock = Label(root, text="🕐 --:--:--",
                   font=("Courier", 14),
                   bg="#1e1e2e", fg="#89dceb")
live_clock.pack()

# "Set Time" label
Label(root, text="Set Alarm Time",
      font=("Helvetica", 12),
      bg="#1e1e2e", fg="#cdd6f4").pack(pady=(14, 4))

# Dropdowns frame
frame = Frame(root, bg="#1e1e2e")
frame.pack()

dropdown_style = {
    "font": ("Helvetica", 13),
    "bg": "#313244",
    "fg": "#cdd6f4",
    "activebackground": "#45475a",
    "relief": FLAT,
    "width": 4
}

hour = StringVar(root)
hour.set("00")
OptionMenu(frame, hour, *two_digits(24)).config(**dropdown_style).pack if False else None
hrs = OptionMenu(frame, hour, *two_digits(24))
hrs.config(**dropdown_style)
hrs.pack(side=LEFT, padx=6)

Label(frame, text=":", font=("Helvetica", 16, "bold"),
      bg="#1e1e2e", fg="#cdd6f4").pack(side=LEFT)

minute = StringVar(root)
minute.set("00")
mins = OptionMenu(frame, minute, *two_digits(60))
mins.config(**dropdown_style)
mins.pack(side=LEFT, padx=6)

Label(frame, text=":", font=("Helvetica", 16, "bold"),
      bg="#1e1e2e", fg="#cdd6f4").pack(side=LEFT)

second = StringVar(root)
second.set("00")
secs = OptionMenu(frame, second, *two_digits(60))
secs.config(**dropdown_style)
secs.pack(side=LEFT, padx=6)

# Buttons frame
btn_frame = Frame(root, bg="#1e1e2e")
btn_frame.pack(pady=16)

set_btn = Button(btn_frame, text="Set Alarm",
                 font=("Helvetica", 12, "bold"),
                 bg="#cba6f7", fg="#1e1e2e",
                 activebackground="#b4befe",
                 relief=FLAT, padx=14, pady=6,
                 command=start_alarm_thread)
set_btn.pack(side=LEFT, padx=8)

snooze_btn = Button(btn_frame, text="💤 Snooze 5 min",
                    font=("Helvetica", 12, "bold"),
                    bg="#fab387", fg="#1e1e2e",
                    activebackground="#f9e2af",
                    relief=FLAT, padx=14, pady=6,
                    state=DISABLED,
                    command=snooze)
snooze_btn.pack(side=LEFT, padx=8)

stop_btn = Button(btn_frame, text="⛔ Stop",
                  font=("Helvetica", 12, "bold"),
                  bg="#f38ba8", fg="#1e1e2e",
                  activebackground="#eba0ac",
                  relief=FLAT, padx=14, pady=6,
                  state=DISABLED,
                  command=stop_alarm)
stop_btn.pack(side=LEFT, padx=8)

# Status label
status_label = Label(root, text="Set a time and click Set Alarm",
                     font=("Helvetica", 11),
                     bg="#1e1e2e", fg="#6c7086")
status_label.pack(pady=6)

# ── Start ────────────────────────────────────────────────────────
root.mainloop()
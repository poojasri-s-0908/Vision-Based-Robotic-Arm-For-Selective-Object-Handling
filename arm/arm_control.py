import serial
import time
import tkinter as tk
import threading

# 🔧 CHANGE PORT IF NEEDED
ser = serial.Serial('COM12', 115200, timeout=1)
time.sleep(2)

# ---------- READ FROM ESP ----------
def read_serial():
    while True:
        try:
            if ser.in_waiting:
                data = ser.readline().decode(errors='ignore').strip()
                if data:
                    print("ESP:", data)
        except:
            pass

threading.Thread(target=read_serial, daemon=True).start()

# ---------- SEND COMMAND ----------
def send(cmd):
    try:
        ser.write((cmd + "\n").encode())
        time.sleep(0.1)
        print("Sent:", cmd)
    except:
        print("Error sending")

# ---------- GUI ----------
root = tk.Tk()
root.title("ROBOT ARM CONTROL")
root.geometry("300x300")

tk.Label(root, text="ARM CONTROL", font=("Arial", 16)).pack(pady=10)

tk.Button(root, text="HOME", width=20, height=2,
          command=lambda: send("HOME")).pack(pady=5)

tk.Button(root, text="GROUND", width=20, height=2,
          command=lambda: send("GROUND")).pack(pady=5)

tk.Label(root, text="GRIPPER", font=("Arial", 14)).pack(pady=10)

tk.Button(root, text="OPEN / CLOSE", width=20, height=2,
          command=lambda: send("GRIPPER")).pack(pady=5)

root.mainloop()

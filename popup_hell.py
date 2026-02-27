import tkinter as tk
import random
import threading
import time

MESSAGES = [
    ("⚠️ CẢNH BÁO NGHIÊM TRỌNG", "Máy tính của bạn có 47 VIRUS!\nHãy gọi ngay: 1800-SCAM-NOW", "#ff0000"),
    ("🔴 HỆ THỐNG BỊ XÂM NHẬP", "Hacker đang truy cập file của bạn!\nĐừng tắt máy!!!", "#cc0000"),
    ("💀 LỖI NGHIÊM TRỌNG", "KERNEL_PANIC_0x000000FF\nHệ thống sẽ tự hủy sau 10 giây", "#8b0000"),
    ("🛑 CẦN CẬP NHẬT NGAY", "Windows của bạn đã hết hạn!\nMua license: $299.99", "#ff4400"),
    ("😱 DỮ LIỆU BỊ MÃ HÓA", "Toàn bộ file đã bị khóa!\n(jk không có gì xảy ra hết đâu 😂)", "#ff0066"),
    ("🔥 CPU NHIỆT ĐỘ CAO", "CPU đang ở 247°C !!!\nMáy sắp nổ rồi bạn ơi!", "#ff6600"),
    ("👁️ ĐANG BỊ THEO DÕI", "NSA đang xem màn hình của bạn\nLúc này. Ngay bây giờ. 👀", "#6600cc"),
    ("💸 TÀI KHOẢN BỊ HACK", "Ai đó vừa chuyển $99,999\nra khỏi tài khoản của bạn!", "#ff0000"),
    ("🤖 AI ĐANG KIỂM SOÁT", "ChatGPT vừa chiếm quyền\nkiểm soát máy tính của bạn 🤖", "#0066ff"),
    ("📱 ĐIỆN THOẠI BỊ CLONE", "Có người đang đọc\ntin nhắn Zalo của bạn!", "#cc6600"),
    ("☢️ PHÓNG XẠ PHÁT HIỆN", "Màn hình của bạn đang phát\ntia UV cực mạnh. Nhắm mắt lại!", "#00cc00"),
    ("🎰 CHÚC MỪNG BẠN TRÚNG", "Bạn là người dùng thứ 1.000.000!\nPhần thưởng: 1 cái popup nữa 🎉", "#ff00ff"),
]

POSITIONS = []
active_windows = []
running = True

def random_pos(w, h):
    sw = root_hidden.winfo_screenwidth()
    sh = root_hidden.winfo_screenheight()
    x = random.randint(0, max(0, sw - w))
    y = random.randint(0, max(0, sh - h))
    return x, y

def make_popup():
    if not running:
        return

    title, msg, color = random.choice(MESSAGES)

    win = tk.Toplevel(root_hidden)
    win.title(title)
    win.configure(bg="#1a1a1a")
    win.attributes("-topmost", True)
    win.resizable(False, False)

    w, h = 340, 180
    x, y = random_pos(w, h)
    win.geometry(f"{w}x{h}+{x}+{y}")

    # Fake title bar màu
    bar = tk.Frame(win, bg=color, height=32)
    bar.pack(fill="x")
    bar.pack_propagate(False)
    tk.Label(bar, text=f"  {title}", font=("Segoe UI", 9, "bold"),
             fg="white", bg=color).pack(side="left", padx=6, pady=6)

    # Nút X giả — khi bấm mở thêm popup mới 😈
    def fake_close():
        # Mở 2 cái mới thay vì đóng
        win.destroy()
        root_hidden.after(100, make_popup)
        root_hidden.after(200, make_popup)

    tk.Label(bar, text=" × ", font=("Segoe UI", 11, "bold"),
             fg="white", bg=color, cursor="hand2").pack(side="right", padx=4)
    bar.bind("<Button-1>", lambda e: fake_close())

    # Nội dung
    tk.Label(win, text=msg, font=("Segoe UI", 11),
             fg="white", bg="#1a1a1a", justify="center",
             wraplength=300).pack(expand=True, pady=(10, 5))

    # Nút OK giả — cũng mở thêm popup
    btn_frame = tk.Frame(win, bg="#1a1a1a")
    btn_frame.pack(pady=(0, 12))

    def fake_ok():
        win.destroy()
        root_hidden.after(50, make_popup)
        root_hidden.after(150, make_popup)
        root_hidden.after(300, make_popup)

    tk.Button(btn_frame, text="  OK  ", font=("Segoe UI", 9, "bold"),
              bg=color, fg="white", relief="flat", cursor="hand2",
              command=fake_ok).pack(side="left", padx=6)
    tk.Button(btn_frame, text="  Hủy  ", font=("Segoe UI", 9, "bold"),
              bg="#333", fg="white", relief="flat", cursor="hand2",
              command=fake_ok).pack(side="left", padx=6)
    tk.Button(btn_frame, text="  Bỏ qua  ", font=("Segoe UI", 9, "bold"),
              bg="#333", fg="white", relief="flat", cursor="hand2",
              command=fake_ok).pack(side="left", padx=6)

    active_windows.append(win)

def spawn_loop():
    """Tự động thêm popup mới sau mỗi vài giây"""
    while running:
        time.sleep(random.uniform(1.5, 3.5))
        if running:
            root_hidden.after(0, make_popup)

def stop_all(event=None):
    global running
    running = False
    root_hidden.destroy()

# Root ẩn
root_hidden = tk.Tk()
root_hidden.withdraw()  # ẩn cửa sổ chính
root_hidden.bind("<Control-q>", stop_all)
root_hidden.bind("<Control-w>", stop_all)

# Hướng dẫn thoát
guide = tk.Toplevel(root_hidden)
guide.title("Hướng dẫn")
guide.configure(bg="#222")
guide.attributes("-topmost", True)
guide.resizable(False, False)
guide.geometry("300x100+20+20")
tk.Label(guide, text="Nhấn  Ctrl+Q  để thoát 😂",
         font=("Segoe UI", 12, "bold"), fg="#00ff88", bg="#222").pack(expand=True)

# Spawn vài cái đầu tiên
for i in range(3):
    root_hidden.after(i * 300, make_popup)

# Vòng lặp tự spawn
threading.Thread(target=spawn_loop, daemon=True).start()

root_hidden.mainloop()

import tkinter as tk
from tkinter import ttk

# ===== Functions =====
def button_click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# ===== Window Setup =====
root = tk.Tk()
root.title("Professional Calculator")

# Window in center
width, height = 320, 470
sw, sh = root.winfo_screenwidth(), root.winfo_screenheight()
x, y = (sw - width) // 2, (sh - height) // 2
root.geometry(f"{width}x{height}+{x}+{y}")

root.config(bg="#1E1E1E")

# ===== Style Setup =====
style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Rounded.TButton",
    font=("Arial", 16, "bold"),
    padding=10,
    relief="flat",
    background="#333333",
    foreground="white",
    borderwidth=0,
)
style.map(
    "Rounded.TButton",
    background=[("active", "#555555")]
)

# ===== Frame =====
main_frame = tk.Frame(root, bg="#1E1E1E")
main_frame.pack(expand=True)

# ===== Entry =====
entry = tk.Entry(
    main_frame,
    width=16,
    font=('Arial', 26, 'bold'),
    borderwidth=0,
    relief='flat',
    justify='right',
    bg="#2D2D2D",
    fg="white",
)
entry.grid(row=0, column=0, columnspan=4, pady=25, padx=10, ipady=15)

# ===== Helper to Create Buttons =====
def make_btn(text, r, c, cmd=None, bg="#333333", colspan=1):
    b = ttk.Button(main_frame, text=text, style="Rounded.TButton", command=cmd)
    b.grid(row=r, column=c, columnspan=colspan, padx=5, pady=5, sticky="nsew")

# ===== Buttons =====
make_btn("AC", 1, 0, cmd=clear, bg="#FF6666")
make_btn("<--", 1, 1, cmd=backspace, bg="#FFB347")
make_btn("%", 1, 2, cmd=lambda: button_click("%"), bg="#FFB347")
make_btn("/", 1, 3, cmd=lambda: button_click("/"), bg="#FFB347")

make_btn("7", 2, 0, cmd=lambda: button_click("7"))
make_btn("8", 2, 1, cmd=lambda: button_click("8"))
make_btn("9", 2, 2, cmd=lambda: button_click("9"))
make_btn("*", 2, 3, cmd=lambda: button_click("*"), bg="#FFB347")

make_btn("4", 3, 0, cmd=lambda: button_click("4"))
make_btn("5", 3, 1, cmd=lambda: button_click("5"))
make_btn("6", 3, 2, cmd=lambda: button_click("6"))
make_btn("-", 3, 3, cmd=lambda: button_click("-"), bg="#FFB347")

make_btn("1", 4, 0, cmd=lambda: button_click("1"))
make_btn("2", 4, 1, cmd=lambda: button_click("2"))
make_btn("3", 4, 2, cmd=lambda: button_click("3"))
make_btn("+", 4, 3, cmd=lambda: button_click("+"), bg="#FFB347")

# “0” button spans two columns (0 and 1)
make_btn("0", 5, 0, colspan=2, cmd=lambda: button_click("0"))
make_btn(".", 5, 2, cmd=lambda: button_click("."))
make_btn("=", 5, 3, cmd=calculate, bg="#00CC99")

# ===== Final Layout Fix =====
for i in range(6):
    main_frame.rowconfigure(i, weight=0)
for i in range(4):
    main_frame.columnconfigure(i, weight=0)

root.mainloop()

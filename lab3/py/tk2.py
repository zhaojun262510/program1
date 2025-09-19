import tkinter as tk

def greet():
    user_name = entry.get()
    label.config(text=f"Hello, {user_name}!")

root = tk.Tk()
root.title("欢迎界面")
root.geometry("300x150")

label = tk.Label(root, text="请输入你的名字:", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="确认", command=greet)
button.pack(pady=5)

root.mainloop()

import tkinter as tk

height = 600
width = 800

root = tk.Tk()
# Keep application between root and main loop

canvas = tk.Canvas(root, height=height, width=width)
canvas.pack()

frame = tk.Frame(root, bg='white')
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.5)

button = tk.Button(frame, text="First Button", fg='red', bg='white')
button.place(relx=0.85, rely=0.20, relwidth=0.25, relheight=0.25)

label = tk.Label(frame, text="This is a test label", bg="blue")
label.place(relx=0.3, rely=0, relwidth=0.45, relheight=0.25)

entry = tk.Entry(frame, bg='gray')
entry.grid(row=0, column=2)

root.mainloop()
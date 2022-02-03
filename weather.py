import tkinter as tk

height = 600
width = 800

root = tk.Tk()
# Keep application between root and main loop

canvas = tk.Canvas(root, height=height, width=width)
canvas.pack()

frame = tk.Frame(root, bg='white')
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

button = tk.Button(frame, text="First Button")
button.pack()

label = tk.Label(frame, text="This is a test label", bg="gray")
label.pack()

entry = tk.Entry(frame, bg='gray')
entry.pack()

root.mainloop()
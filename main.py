from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = "0"


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel(timer)
    marks = " "
    label1.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    label2.config(text=marks)
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start():
    global reps
    reps += 1
    work_hrs = WORK_MIN * 60
    break_min = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps % 2 != 0:
        label1.config(text="WORK", fg=GREEN)
        count_down(work_hrs)

    elif reps % 8 == 0:
        label1.config(text="LONG BREAK", fg=RED)
        count_down(long_break)

    else:
        label1.config(text="SHORT BREAK", fg=PINK)
        count_down(break_min)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    mini = count // 60
    sec = count % 60
    if mini < 10:
        mini = f"0{mini}"
    if sec < 10:
        sec = f"0{sec}"
    canvas.itemconfig(timer_text, text=f"{mini}:{sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start()
        marks = " "
        work_sessions = reps // 2
        for _ in range(work_sessions):
            marks += "✔"
        label2.config(text=marks)

        # ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)

label1 = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
label1.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(row=1, column=1)

button1 = Button(text="start", highlightthickness=0, command=start)
button1.grid(row=2, column=0)

button2 = Button(text="Reset", highlightthickness=0, command=reset)
button2.grid(row=2, column=2)

label2 = Label(font=(FONT_NAME, 15, "bold"), fg=GREEN, bg=YELLOW)
label2.grid(row=3, column=1)

window.mainloop()

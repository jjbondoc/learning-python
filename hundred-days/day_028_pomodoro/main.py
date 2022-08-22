from cProfile import label
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.2
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 0.3
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer) # pause the timer
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    label_timer.config(text="Timer")
    label_checks.config(text="")
    

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        label_timer.config(text="Break", fg=RED)
        count_down(math.floor(long_break_sec))
        
    
    elif reps % 2 == 1:
        label_timer.config(text="Work", fg=GREEN)
        count_down(math.floor(work_sec))
        
    else:
        label_timer.config(text="Break", fg=PINK)
        count_down(math.floor(short_break_sec))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    mins = math.floor(count / 60)
    secs = "{:0>2d}".format(count % 60)
    canvas.itemconfig(timer_text, text=f"{mins}:{secs}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            checks = label_checks['text']
            label_checks.config(text=checks + "✔")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

#label: timer
label_timer = Label(text="Timer", font=(FONT_NAME, 48, 'normal'), bg=YELLOW, fg=GREEN)
label_timer.grid(column=1, row=0)

#label: check mark
label_checks = Label(bg=YELLOW, fg=GREEN, font=('Arial', 18, 'normal'))
label_checks.grid(column=1, row=3)

#button: start
button_start = Button(text="Start", command=start_timer, highlightthickness=0)
button_start.grid(column=0, row=2)

#button: end
button_end = Button(text="Reset", command=reset_timer, highlightthickness=0)
button_end.grid(column=2, row=2)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_png = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_png)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 24, 'bold'))
canvas.grid(column=1, row=1)

window.mainloop()
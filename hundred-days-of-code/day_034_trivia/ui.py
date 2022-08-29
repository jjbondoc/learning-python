from cgitb import text
from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ('Arial', 14, 'italic')

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain) -> None: #* quiz_brain is declared as the class QuizBrain
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        #score
        self.score_label = Label(text="Score: 0", font=('Arial', 12, 'normal'), bg=THEME_COLOR, fg='white')
        self.score_label.grid(column=1, row=0)
        #photos
        true_img = PhotoImage(file="./images/true.png")
        false_img = PhotoImage(file="./images/false.png")
        #canvas
        self.canvas = Canvas(width=300, height=250, background='white', highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Question", font=FONT)
        self.canvas.grid(column=0, columnspan=2, row=1, pady=50)
        #buttons
        self.true_b = Button(image=true_img, highlightthickness=0, relief='flat', borderwidth=0, command=self.answer_true)
        self.true_b.grid(column=0, row=2)
        self.false_b = Button(image=false_img, highlightthickness=0, relief='flat', borderwidth=0, command=self.answer_false)
        self.false_b.grid(column=1, row=2)
        
        self.get_next_question()

        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas.config(background='white')
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_b.config(state="disabled")
            self.false_b.config(state="disabled")
    
    def answer_false(self):
        self.give_feedback(self.quiz.check_answer("false"))
    
    def answer_true(self):
        self.give_feedback(self.quiz.check_answer("true"))
    
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(background='green')
        else:
            self.canvas.config(background='red')
        self.window.after(1000, func=self.get_next_question)
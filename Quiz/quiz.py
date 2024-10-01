from tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.answer_vars = []
        self.answer_corrects = ["Answer 1", "Answer 1", "Answer 2", "Answer 1", "Answer 3", "Answer 4"]
        
        # Tạo canvas và scrollbar
        self.canvas = Canvas(self)
        self.scrollbar = Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Đặt vị trí cho canvas và scrollbar
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.scrollbar.grid(row=0, column=1, sticky="ns")

        self.create_widgets()

    def create_widgets(self):
        self.create_question("Question 1: Có bao nhiêu quốc gia trên thế giới?", "195 quốc gia.", "189 quốc gia", "193 quốc gia.", "178 quốc gia", 0)
        self.create_question("Question 2: Quốc gia nào đồng dân nhất?", "Trung quốc", "Nga", "Mỹ", "Ấn Độ", 6)
        self.create_question("Question 3: Quốc gia nào nhỏ nhất thế giới?", "Việt Nam", "Vatican", "Italya", "Brazil", 11)
        self.create_question("Question 4: Quốc gia nào có dân số ít nhất thế giới?", "Vatican", "Korean", "Japan", "Nepal", 16)
        self.create_question("Question 5: Quốc gia nào có bài quốc ca hào hùng nhất?", "Portugal", "UK", "Việt Nam", "Turkey", 21)
        self.create_question("Question 6: Quốc gia nào có nhiều dân tộc nhất?", "Triều Tiên", "Nga", "Mỹ", "Kazakhstan", 26)
        
        Button(self.scrollable_frame, text="Submit", command=self.submit_answers).grid(row=32, column=0, pady=10)

    def create_question(self, question, answer1, answer2, answer3, answer4, row):
        answer1_var = IntVar()
        answer2_var = IntVar()
        answer3_var = IntVar()
        answer4_var = IntVar()
        
        Label(self.scrollable_frame, text=question).grid(row=row, column=0, sticky='w', padx=5, pady=5)
        Checkbutton(self.scrollable_frame, text="Answer 1: " + answer1, variable=answer1_var).grid(row=row + 1, column=0, sticky='w', padx=5)
        Checkbutton(self.scrollable_frame, text="Answer 2: " + answer2, variable=answer2_var).grid(row=row + 2, column=0, sticky='w', padx=5)
        Checkbutton(self.scrollable_frame, text="Answer 3: " + answer3, variable=answer3_var).grid(row=row + 3, column=0, sticky='w', padx=5)
        Checkbutton(self.scrollable_frame, text="Answer 4: " + answer4, variable=answer4_var).grid(row=row + 4, column=0, sticky='w', padx=5)
        Label(self.scrollable_frame, text="--------------------------------------------------------------").grid(row=row + 5, column=0, sticky='w', padx=5)

        self.answer_vars.append((answer1_var, answer2_var, answer3_var, answer4_var))
    def open_popup(self, score):
        popup = Toplevel(self)
        popup.title("Popup Window")
        popup.geometry("200x100")

        label = Label(popup, text="Điểm: " + score)
        label.pack(pady=10)

        close_button = Button(popup, text="Close", command=popup.destroy)
        close_button.pack(pady=5)

    def submit_answers(self):
        selected_answers = []
        score = 0
        for index, answer_group in enumerate(self.answer_vars):
            for var in answer_group:
                if var.get():  # Nếu checkbox được chọn
                    selected_answers.append("Answer {}".format(answer_group.index(var) + 1))
            # Kiểm tra đáp án đúng cho câu hỏi này
            if selected_answers and selected_answers[-1] == self.answer_corrects[index]:
                score += 1
            selected_answers.clear()  # Reset cho câu hỏi tiếp theo

        self.open_popup(str(score))
# Khởi tạo 1 frame
root = Tk()
# khởi tạo 1 app với frame đã được tạo ở trên
app = Application(master=root)
# Set title cho frame đó
app.master.title("Quiz Application")
# set kích thước cho frame
app.master.minsize(400, 300)
# chạy vòng lặp tạo ra frame hình đó
app.mainloop()
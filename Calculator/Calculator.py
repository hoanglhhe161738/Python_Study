from tkinter import *
from tkinter import ttk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        
        # Entry box để hiển thị kết quả
        self.result_var = StringVar()
        self.entry = ttk.Entry(root, textvariable=self.result_var, font=("Arial", 24), justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, sticky='nsew')
        
        # Các nút số và phép tính
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        
        # Tạo các nút
        row_val = 1
        col_val = 0
        for button in buttons:
            ttk.Button(root, text=button, command=lambda b=button: self.on_button_click(b)).grid(row=row_val, column=col_val, sticky='nsew', ipadx=10, ipady=10)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Tạo các dòng để có thể thay đổi kích thước
        for i in range(5):
            root.grid_rowconfigure(i, weight=1)
            root.grid_columnconfigure(i, weight=1)

    def on_button_click(self, button):
        if button == '=':
            try:
                # Tính toán biểu thức và hiển thị kết quả
                result = str(eval(self.result_var.get()))
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        else:
            # Thêm nút bấm vào entry
            current_text = self.result_var.get()
            self.result_var.set(current_text + button)

if __name__ == "__main__":
    root = Tk()
    calculator = Calculator(root)
    root.mainloop()
from future.moves.tkinter import *


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title('Calculator')
        self.root.iconbitmap('calculator.ico')
        # Color code
        dark_grey = '#141414'
        med_grey = '#212121'
        cus_red = '#c41212'
        self.display = Text(root, bg=dark_grey, font=('Helvetica', 32), height=1, state='disabled',
                            fg='white', bd=0, pady=50, padx=5, selectbackground=dark_grey,
                            inactiveselectbackground=dark_grey)

        for x in range(1, 5):
            self.root.columnconfigure(x, weight=1)
            self.root.rowconfigure(x, weight=1)

        self.display.grid(row=0, column=0, columnspan=5, sticky=W + E + N + S)
        self.display.configure(state='normal')
        self.equation = ''
        self.root.geometry('500x600+850+50')
        b1 = self.createButton(7)
        b2 = self.createButton(8)
        b3 = self.createButton(9)
        b4 = self.createButton(u"\u00F7", bg=med_grey)  # division (÷) button code
        b5 = self.createButton(4)
        b6 = self.createButton(5)
        b7 = self.createButton(6)
        b8 = self.createButton(u"\u00D7", bg=med_grey)  # multiplication (x) button code
        b9 = self.createButton(1)
        b10 = self.createButton(2)
        b11 = self.createButton(3)
        b12 = self.createButton('-', bg=med_grey)
        b13 = self.createButton(None)  # Blank button
        b14 = self.createButton(0)
        b15 = self.createButton(None)  # Blank button
        b16 = self.createButton('+', bg=med_grey)
        b17 = self.createButton('DEL', None, bg=med_grey)
        b18 = self.createButton('CE', None, bg=med_grey)
        b19 = self.createButton('=', None, bg=cus_red)
        b13.config(state='disabled')
        b15.config(state='disabled')
        buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19]

        count = 0
        for row in range(1, 5):
            for col in range(4):
                buttons[count].grid(row=row, column=col, sticky=W + E + N + S)
                count += 1

        buttons[16].grid(row=1, column=4, rowspan=1, sticky=W + E + N + S)
        buttons[17].grid(row=2, column=4, rowspan=2, sticky=W + E + N + S)
        buttons[18].grid(row=4, column=4, rowspan=1, sticky=W + E + N + S)

    def createButton(self, val, write=True, width=5, bg='black'):
        return Button(self.root, text=val, command=lambda: self.click(val, write), width=width, bg=bg, bd=0, fg='white',
                      font=('Helvetica', 24))

    def click(self, text, write):
        if write == None:
            if text == '=' and self.equation:
                self.equation = re.sub(u'\u00F7', '/', self.equation)
                self.equation = re.sub(u'\u00D7', '*', self.equation)
                print(self.equation)
                answer = str(eval(self.equation))
                self.clear_screen()
                self.insert_screen(answer, newline=True)
            elif text == "CE":
                self.clear_screen()
            elif text == 'DEL':
                self.del_screen()
        else:
            # add text to screen
            self.insert_screen(text)

    def clear_screen(self):
        self.equation = ''
        self.display.configure(state='normal')
        self.display.delete(1.0, END)
        self.display.configure(state='disabled')

    def del_screen(self):
        self.equation = self.equation[:-1]
        self.display.configure(state='normal')
        text = self.display.get("1.0", END)[:-2]
        self.display.tag_config('val', justify=RIGHT)
        self.display.delete(1.0, END)
        self.display.insert(END, text, 'val')
        self.display.configure(state='disabled')

    def insert_screen(self, value, newline=False):
        self.display.configure(state='normal')
        self.display.tag_config('val', justify=RIGHT)
        self.display.insert(END, str(value), 'val')
        self.equation += str(value)
        self.display.configure(state='disabled')


root = Tk()
calc = Calculator(root)
root.mainloop()

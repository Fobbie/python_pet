from tkinter import *
import random as rdm


class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.startUI()

    def startUI(self):
        btn = Button(root, text="Rock", font=("Salina", 15),
                     command=lambda x=1: self.btn_click(x), bg='#a72f99', fg='white')
        btn2 = Button(root, text="Scissors", font=("Salina", 15),
                      command=lambda x=2: self.btn_click(x), bg='#a72f99', fg='white')
        btn3 = Button(root, text="Paper", font=("Salina", 15),
                      command=lambda x=3: self.btn_click(x), bg='#a72f99', fg='white')

        btn.place(x=10, y=100, width=120, height=50)
        btn2.place(x=155, y=100, width=120, height=50)
        btn3.place(x=300, y=100, width=120, height=50)

        self.lbl = Label(root, text="Start!", bg="#13121f", font=("Salina", 21, "bold"), fg='white')
        self.lbl.place(x=150, y=25)

        self.win = self.drow = self.lose = 0

        self.lbl2 = Label(root, justify="left", font=("Salina", 13),
                         text=f"Wins: {self.win}\nLose:"
                              f" {self.lose}\nDraw: {self.drow}",
                         bg="#13121f", fg='white')
        self.lbl2.place(x=5, y=5)

    def btn_click(self, choise):
        comp_choise = rdm.randint(1, 3)

        if choise == comp_choise:
            self.drow += 1
            self.lbl.configure(text="Draw")
        elif (choise == 1 and comp_choise == 2 
            or choise == 2 and comp_choise == 3 
            or choise == 3 and comp_choise == 1):
            self.win += 1
            self.lbl.configure(text="Win")
        else:
            self.lose += 1
            self.lbl.configure(text="Lose")

        self.lbl2.configure(text=f"Wins: {self.win}\nDraw:"
                              f" {self.lose}\nLose: {self.drow}")

        del comp_choise


if __name__ == '__main__':
    root = Tk()
    root.geometry("430x160+200+200")
    root.title("Rock, paper, scissors")
    root.resizable(False, False)
    root["bg"] = "#13121f"
    app = Main(root)
    app.pack()
    root.mainloop()

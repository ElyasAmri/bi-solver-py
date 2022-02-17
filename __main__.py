from tkinter import *
from tkinter.ttk import *


class App(Tk):
    def __init__(self, width=1260, height=720, gx=20, gy=20):
        super().__init__()
        self.title('Data Sampler')
        self.geometry(f"{width}x{height}+{int((self.winfo_screenwidth() - width) / 2)}"
                      f"+{int((self.winfo_screenheight() - height) / 2)}")
        self.fr = Frame(self)
        self.width = width
        self.height = height
        self.gx = gx
        self.gy = gy

        self.action()
        buttons = Frame(self)
        buttons.pack(anchor=S, expand=1)
        buttons.grid_columnconfigure(4)
        buttons.grid_rowconfigure(2)
        act = Button(buttons, text='Action')
        act.grid(row=1, columnspan=4)
        act.configure(command=self.action)

        def change(sv, ref):
            try:
                if ref == 1:
                    self.gx = int(sv.get())
                else:
                    self.gy = int(sv.get())
            except Exception:
                return

        gx_l = StringVar()
        gx_l.set('30')
        gx_l.trace("w", lambda name, index, mode, sv=gx_l: change(gx_l, 1))
        gy_l = StringVar()
        gy_l.set('30')
        gx_l.trace("w", lambda name, index, mode, sv=gy_l: change(gy_l, 2))

        Label(buttons, text='width').grid(column=0, row=0)
        Entry(buttons, textvariable=gx_l).grid(column=1, row=0)
        Label(buttons, text='height').grid(column=2, row=0)
        Entry(buttons, textvariable=gy_l).grid(column=3, row=0)

    def action(self):
        self.fr.children.clear()
        self.fr.grid_columnconfigure(self.gx + 3)
        self.fr.grid_rowconfigure(self.gy)
        for i in range(0, self.gy):
            acc = 0
            for j in range(0, self.gx):
                Label(self.fr, text=f'{i ^ j}').grid(column=i, row=j)
                acc += (i ^ j)
            Label(self.fr, text=f'{acc}').grid(column=self.gx + 2, row=i)
        for j in range(0, self.gy):
            Label(self.fr, text=' ').grid(column=self.gx + 1, row=j)
            Label(self.fr, text=f'{int((self.gx * (self.gx - 1)) / 2)}').grid(column=self.gx + 3, row=j)
        self.fr.pack(anchor=CENTER, expand=10)


if __name__ == '__main__':
    app = App(1260, 720, 30, 30)
    app.mainloop()

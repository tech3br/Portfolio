import tkinter as tk


def JanelaSalvar():

    TelaSalva= Tk()

    go_button = janela.Button(text="Salvar", command=go)
    go_button.pack()

def go():

janela.dialog = ProgressWindow()
janela.do_real_work(0)

def do_real_work():
        # simulate doing work; update the status window periodically
        .dialog.set(count)
        .after(500, lambda count=count+10: self.do_real_work(count))


class ProgressWindow(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)
        self.label = tk.Label(self, text="0%")
        self.label.pack(side="top", fill="both", expand=True)
        self.wm_geometry("200x200")

    def set(self, value):
        if value > 100:
            self.destroy()
        else:
            self.label.configure(text="%s %%" % value)


if __name__ == "__main__":
    root = tk.Tk()
    App(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
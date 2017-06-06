import tkinter as tk
import tkinter.filedialog as tkfd

class Encryptor:
    def __init__(self, okno):
        self.log = 'Welcome to The Encryptor!\n'
        self.status_lines = 1
        self.zgradi(okno)

    def zgradi(self, okno):
        status = tk.Frame(okno, height = 100, width = 100,
                          padx=5, pady=5, bd=5, relief='raised')
        algoritmi = tk.Frame(okno, height = 480, width = 100,
                             bd=3, relief='sunken')
        datoteke = tk.Frame(okno, height = 100, width = 590,
                            bd=3, relief='sunken')
        pozeni = tk.Frame(okno, height = 100, width = 100, bg='red',
                          relief='groove', bd=3)
        
        status.grid(row = 0, column = 0)
        algoritmi.grid(row = 0, column = 1)
        datoteke.grid(row = 1, column = 0)
        pozeni.grid(row = 1, column = 1)

        #status
        self.status_bar = tk.Label(status, height = 30, width = 80,
                                   bg = 'white', anchor='nw',
                                   justify='left')
        self.status_bar.grid(row=0, column=0)
        self.osvezi_status()

        #algoritmi

        #datoteke

        #pozeni

    def osvezi_status(self):
        if self.status_lines >= self.status_bar['height']:
            self.status_bar['height'] += 2
        self.status_bar['text'] = self.log

root = tk.Tk()

app = Encryptor(root)

root.mainloop()

###GENERAL TODO:
###-poveži gumbe na primerne command funkcije
###-prej napiši te command fukcije
###-naštudiraj: branje iz Entry, pridobivanje vrednosti iz IntVar,...
###-razno

import tkinter as tk
import tkinter.filedialog as tkfd
import time

class Encryptor:
    def __init__(self, okno):
        self.log = 'Welcome to Encryptor!\n'
        self.log_file = 'Encryptor_log' + str(round(time.time())) + '.txt'
        self.log_val = tk.IntVar()
        self.status_lines = 1
        
        self.alg = tk.IntVar()
        self.method = tk.IntVar()
        
        self.zgradi(okno)

    def zgradi(self, okno):
        okno.title('Encryptor')
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
        rb1 = tk.Radiobutton(algoritmi, text='Ceasar', variable = self.alg,
                            value = 1)
        rb2 = tk.Radiobutton(algoritmi, text='Vigenere', variable = self.alg,
                            value = 2)
        rb_other = tk.Radiobutton(algoritmi, text='Other', variable = self.alg,
                                 value = -1)

        rb1.pack()
        rb2.pack()
        rb_other.pack()

        #datoteke
        self.ime_dat = tk.Entry(datoteke, width = 80, justify='left')
            #TODO: command nastavi na izbiro datoteke s tkfd
        b_dat = tk.Button(datoteke, text='Choose a file...')
        rb_enc = tk.Radiobutton(datoteke, text='Encrypt',
                            variable = self.method, value = 1)
        rb_dec = tk.Radiobutton(datoteke, text='Decrypt',
                            variable = self.method, value = 2)
        cb_log = tk.Checkbutton(datoteke, text='Delete log file?',
                             variable = self.log_val, state='normal')
        
        
        self.ime_dat.grid(row = 0, column = 0)
        b_dat.grid(row = 0, column = 1)
        rb_enc.grid(row = 1, column = 0)
        rb_dec.grid(row = 2, column = 0)
        cb_log.grid(row = 3, column = 0)

        #pozeni
            #TODO: command nastavi na izvajanje funkcij
        b_go = tk.Button(pozeni, text='GO!', height = 3, width = 8,
                         bg='red', font='bold')

        b_go.pack()

    def osvezi_status(self):
        if self.status_lines >= 29:
            self.logiraj()
        self.status_bar['text'] = self.log
    def logiraj(self):
        with open(self.log_file, 'a') as log_dat:
            log_dat.write(self.log)
            self.log = 'Logirano v ' + self.log_file
            self.status_lines = 1
            self.osvezi_status()

root = tk.Tk()

root.resizable(width=False, height=False)

app = Encryptor(root)

root.mainloop()

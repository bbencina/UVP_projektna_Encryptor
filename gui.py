###GENERAL TODO:
###-poženi z večimi algoritmi
###-razno

import tkinter as tk
import tkinter.filedialog as tkfd
import time
import os

class Encryptor:
    def __init__(self, okno):
        self.log = 'Welcome to Encryptor!\n'
        self.log_file_name = 'encryptor_log' + str(round(time.time())) + '.txt'
        self.log_var = tk.IntVar()
        self.status_lines = 1
        
        self.alg = tk.IntVar()
        self.method = tk.IntVar()

        self.file_name = ''
        self.file_var = tk.IntVar()

        self.password = ''
        
        self.zgradi(okno)

    def zgradi(self, okno):
        okno.title('Encryptor')
        status = tk.Frame(okno, height = 100, width = 100,
                          padx=5, pady=5, bd=5, relief='raised')
        algoritmi = tk.Frame(okno, height = 480, width = 100,
                             bd=3, relief='raised')
        datoteke = tk.Frame(okno, height = 100, width = 590,
                            bd=3, relief='raised')
        pozeni = tk.Frame(okno, height = 100, width = 100, bg='red',
                          relief='groove', bd=3)
        
        status.grid(row = 0, column = 0)
        algoritmi.grid(row = 0, column = 1)
        datoteke.grid(row = 1, column = 0)
        pozeni.grid(row = 1, column = 1)

        #status
        self.status_bar = tk.Label(status, height = 30, width = 84,
                                   bg = 'white', anchor='nw',
                                   justify='left')
        self.status_bar.grid(row=0, column=0)
        self.osvezi_status()

        #algoritmi
        nmtag = tk.Label(algoritmi, text='Algorithms:')
        rb1 = tk.Radiobutton(algoritmi, text='Ceasar', variable = self.alg,
                            value = 1)
        rb2 = tk.Radiobutton(algoritmi, text='Vigenere', variable = self.alg,
                            value = 2)
        rb_other = tk.Radiobutton(algoritmi, text='Other', variable = self.alg,
                                 value = -1)

        nmtag.pack()
        rb1.pack()
        rb2.pack()
        rb_other.pack()

        #datoteke
        self.ime_dat = tk.Entry(datoteke, width = 80, justify='left')
        self.pw_bar = tk.Entry(datoteke, width = 60, justify='left',
                               show='*')
        b_dat = tk.Button(datoteke, text='Choose a file...',
                          command = self.file_open)
        b_help = tk.Button(datoteke, text='Open Helper',
                           command = self.open_helper)
        b_pw = tk.Button(datoteke, text='Set Password',
                         command = self.set_password, bg='green')
        rb_enc = tk.Radiobutton(datoteke, text='Encrypt',
                            variable = self.method, value = 1)
        rb_dec = tk.Radiobutton(datoteke, text='Decrypt',
                            variable = self.method, value = 2)
        cb_log = tk.Checkbutton(datoteke, text='Delete log file?',
                             variable = self.log_var, state='normal')
        cb_file = tk.Checkbutton(datoteke, text='Delete original file?',
                                 variable = self.file_var, state='normal')
        
        
        self.ime_dat.grid(row = 0, column = 0)
        self.pw_bar.grid(row = 1, column = 0)
        b_dat.grid(row = 0, column = 1)
        b_pw.grid(row = 1, column = 1)
        b_help.grid(row = 3, column = 1)
        rb_enc.grid(row = 2, column = 0)
        rb_dec.grid(row = 3, column = 0)
        cb_log.grid(row = 4, column = 0)
        cb_file.grid(row = 4, column = 1)

        #pozeni
        b_go = tk.Button(pozeni, text='GO!', height = 3, width = 8,
                         bg='red', font='bold',
                         command = self.gremo_fantje)

        b_go.pack()

    def osvezi_status(self):
        if self.status_lines >= 29:
            self.logiraj()
        self.status_bar['text'] = self.log
    
    def logiraj(self):
        with open(self.log_file_name, 'a') as log_dat:
            log_dat.write(self.log)
            self.log = 'Logged in ' + self.log_file_name + '.\n'
            self.status_lines = 1
            self.osvezi_status()

    def file_open(self):
        self.file_name = tkfd.askopenfilename()
        self.ime_dat.delete(0, tk.END)
        self.ime_dat.insert(0, self.file_name)
        self.log = self.log + 'File chosen successfully: ' + self.file_name + '\n'
        self.status_lines += 1
        self.osvezi_status()
        self.log = self.log + 'NOTE: This version of Encryptor only supports plain text files.\n'
        self.status_lines += 1
        self.osvezi_status()

    def open_helper(self):
        hwindow = tk.Tk()
        hwindow.resizable(width=False, height=False)
        helper = Helper(hwindow)
        hwindow.mainloop()

    def set_password(self):
        self.password = self.pw_bar.get()

        if self.password != '':
            self.log += 'Password set successfully.\n'
            self.status_lines += 1
            self.osvezi_status()
        else:
            self.log += 'There were problems setting the password.\n'
            self.status_lines += 1
            self.osvezi_status()

    def enc_dec_process(self, method, custom_flag):
        if custom_flag == False:
            import CEASAR
            encrypt, decrypt = CEASAR.encrypt, CEASAR.decrypt
        if custom_flag == True:
            import CUSTOM
            encrypt, decrypt = CUSTOM.encrypt, CUSTOM.decrypt

        self.log += 'Processing...'
        self.osvezi_status()
        i = 0
        with open(self.file_name) as i_dat:
            with open(self.tempfilename + '00' + self.extension, 'w') as o_dat:
                for v in i_dat:
                    for c in v:
                        if method == 1:
                            o_dat.write(encrypt(c, self.password, i))
                        if method == 2:
                            o_dat.write(decrypt(c, self.password, i))
                        i += 1
        self.log += 'Done.\n'
        self.status_lines += 1
        self.osvezi_status()

    def gremo_fantje(self):
        self.file_name = self.ime_dat.get()
        self.tempfilename, self.extension = os.path.splitext(self.file_name)
        
        if self.alg.get() == 1:
            cypher = 'Ceasar cypher'
            flag = False


        if self.alg.get() == 2:
            cypher = "Vigenere's square cypher"
            flag = False

        if self.alg.get() == -1:
            cypher = 'Custom cryptographic algorithm'
            flag = True

        self.log += '{0} selected.\n'.format(cypher)
        self.status_lines += 1
        self.osvezi_status()

        self.enc_dec_process(self.method.get(), flag)

        if self.file_var.get() == 1:
            os.remove(self.file_name)
            self.log += 'Original file removed successfully.\n'
            self.status_lines += 1
            self.osvezi_status()
        if self.log_var.get() == 1:
            self.log += 'Log file will be deleted.\n'
            self.status_lines += 1
            self.osvezi_status()
            self.logiraj()
            os.remove(self.log_file_name)
        else:
            self.logiraj()


class Helper():
    def __init__(self, okno):
        with open('help.txt') as dat:
            self.text = dat.read()
        self.zgradi(okno)

    def zgradi(self, okno):
        okno.title('Helper')
        help_text = tk.Label(okno, justify='left', anchor='w')
        help_text['text'] = self.text
        help_text.pack()



root = tk.Tk()

root.resizable(width=False, height=False)

app = Encryptor(root)

root.mainloop()

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

    def gremo_fantje(self):
        self.file_name = self.ime_dat.get()
        
        if self.alg.get() == 1:
            self.log += 'Ceasar cypher selected.\n'
            self.status_lines += 1
            self.osvezi_status()

            import CEASAR

            self.log += 'Processing...'
            self.osvezi_status()
            with open(self.file_name) as i_dat:
                with open(self.file_name[:-4] + '00' + '.txt', 'w') as o_dat:
                    for v in i_dat:
                        for c in v:
                            if self.method.get() == 1:
                                o_dat.write(CEASAR.encrypt(c, self.password))
                            if self.method.get() == 2:
                                o_dat.write(CEASAR.decrypt(c, self.password))
            self.log += 'Done.\n'
            self.status_lines += 1
            self.osvezi_status()

        if self.alg.get() == 2:
            self.log += "Vigenere's square cypher selecte.\n"
            self.status_lines += 1
            self.osvezi_status()

            import CEASAR

            self.log += 'Processing...'
            self.osvezi_status()
            i = 0
            l = len(self.password)
            with open(self.file_name) as i_dat:
                with open(self.file_name[:-4] + '00' + '.txt', 'w') as o_dat:
                    for v in i_dat:
                        for c in v:
                            if self.method.get() == 1:
                                o_dat.write(CEASAR.encrypt(c, self.password[i % l]))
                            if self.method.get() == 2:
                                o_dat.write(CEASAR.decrypt(c, self.password[i % l]))
                            i += 1
            self.log += 'Done.\n'
            self.status_lines += 1
            self.osvezi_status

        if self.alg.get() == -1:
            self.log += 'Custom cypher algorithm selected.\n'
            self.status_lines += 1
            self.osvezi_status()

            import CUSTOM

            self.log += 'Processing...'
            self.osvezi_status()
            with open(self.file_name) as i_dat:
                with open(self.file_name[:-4] + '00'+ '.txt', 'w') as o_dat:
                    for v in i_dat:
                        for c in v:
                            if self.method.get() == 1:
                                o_dat.write(CUSTOM.encrypt(c, self.password))
                            if self.method.get() == 2:
                                o_dat.write(CUSTOM.decrypt(c, self.password))
            self.log += 'Done.\n'
            self.status_lines += 1
            self.osvezi_status()


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
        self.text = 'Welcome to the helping screen of Encryptor!\n\n'
        self.text += 'NOTE: Be sure to always set your password!\n\n'
        self.text += '1 CUSTOM ENCRYPTION\n'
        self.text += '    For encryption with your custom algorithm simply\n'
        self.text += '    write your Python file, name it CUSTOM.py and then\n'
        self.text += '    select the "Other" option in the algorithms menu.\n'
        self.text += '    File MUST be in the same directory as the program.\n'
        self.text += '    BE SURE you name your file right. The file MUST contain\n'
        self.text += '    at least 2 functions named -encrypt(char, key)- and \n'
        self.text += '    -decrypt(char, key)- (no dashes) that change one character\n'
        self.text += '    into another.\n\n'
        self.text += '2 CEASAR ENYCRYPTION\n'
        self.text += '    This is a simple ceasar code, password MUST be only\n'
        self.text += '    only one character that represents indentation in\n'
        self.text += '    the alphanumerical table. The table is as such:\n'
        self.text += '    All letters of the English alphabet in order, first\n'
        self.text += '    uppercase, then lowercase, then numbers 0-9. There\n'
        self.text += '    are no special characters. If you wish to change\n'
        self.text += '    the table and/or add characters, modify the file\n'
        self.text += '    named CEASAR.py.\n\n'
        self.text += "3 VINEGERE'S SQUARE ENCRYPTION\n"
        self.text += '    This is a polyalphabetic version of the ceasar code.\n'
        self.text += '    Password should be a word, no spaces or special\n'
        self.text += '    characters. If you wish to add special characters,\n'
        self.text += '    modify the alphanumerical table much like in the ceasar\n'
        self.text += '    code case.'
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

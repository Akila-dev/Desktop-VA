import tkinter as tk
import pyttsx3
import datetime


class Pal:
    
    def __init__(self):
        self.bg = '#040410'
        self.light_bg = '#202080'
        self.opac_bg = '#060616'
        
        
        self.root = tk.Tk()
        self.root.geometry("700x480")
        self.root.minsize(700,480)
        self.root.maxsize(700,480)
        self.root.title("Personal Assistant Local (PAL)")
        self.root.configure(bg=self.bg)
        
        self.filler = tk.Label(self.root, text="", bg=self.bg, fg=self.bg)
        self.filler.pack()
        
        self.pal_text = tk.Label(self.root, text="Hi, I'm PAL, your virtual assistant", width=70, height=13, bg=self.light_bg, fg="#fff", highlightthickness=1, font=('Montserrat', 13), wraplength=500, justify="center")
        self.pal_text.pack(pady=30, padx=50)
        
        self.homeFrames = tk.Frame(self.root, bg=self.bg)
        
        self.commands_btn = tk.Button(self.homeFrames, text="Possible Commands", width=22, font=('Arial', 12), pady=10, bg=self.opac_bg, fg='#fff', activebackground=self.light_bg, activeforeground='#fff', command=self.open_commands_window)
        self.commands_btn.grid(row=0, column=0, padx=10)
        
        self.pal_image = tk.PhotoImage(file='./assets/pal.png', width=100, height=101)
        self.home_pal = tk.Button(self.homeFrames, text='pal', image=self.pal_image, bg=self.bg, activebackground=self.bg, highlightthickness=0, borderwidth=0)
        self.home_pal.grid(row=0, column=1, padx=10)
        
        # self.account_btn = tk.Button(self.homeFrames, text="User Account", width=22, font=('Arial', 12), pady=10, bg='#81afdd', command=self.open_account_window)
        # self.account_btn.grid(row=0, column=2, padx=10)
        
        self.account_btn = tk.Button(self.homeFrames, text="User Account", width=22, font=('Arial', 12), pady=10, bg=self.opac_bg, fg='#fff', activebackground=self.light_bg, activeforeground='#fff', command=self.open_dictionary_window)
        self.account_btn.grid(row=0, column=2, padx=10)
        
        self.homeFrames.pack()
        
        self.root.mainloop()
    
    def listen(self, words):
        self.user_input = words.lower()
        
        if ("write whatsapp message") in self.user_input:
            self.open_whatsapp_window()
            print("Opening Whatsapp sender")
        elif ("show commands") in self.user_input:
            self.open_commands_window()
            print("Opening Commands window")
            time = datetime.datetime.now().minute
            print(time!=38)
        else:
            print("Yikes")
    
    def open_account_window(self):
        self.account_window = tk.Toplevel(self.root)
        
        self.account_window.title("PAL User Details")
        self.account_window.geometry("350x500")
        self.account_window.configure(bg=self.bg)
    
    def open_commands_window(self):
        self.commands_window = tk.Toplevel(self.root)
        
        self.commands_window.title("PAL Commands")
        self.commands_window.geometry("380x550")
        self.commands_window.minsize(380,550)
        self.commands_window.maxsize(380,550)
        self.commands_window.configure(bg=self.bg)
        
        self.commands_head = tk.Label(self.commands_window, text="WHAT I CAN DO FOR YOU", fg="#fff", font=('Arial', 12, 'bold'), bg=self.light_bg, pady=10)
        self.commands_head.pack(pady=30, padx=10, fill='x')
        
        self.command1 = """1. Open Apps: To open any app, simply say "Open + <App name>", e.g: "Open Chrome" """
        self.command2 = """2. Search Words: To search a word, simply say "What is the meaning of + <word>", e.g: "What is the meaning of Sing" """
        self.command3 = """3. Google words or phrase: To google a word or phrase, simply say "Google + <word or phrase>", e.g: "Google Mountain Everest" """
        self.command4 = """4. Send WhatsApp message: To send a whatsapp message, simply say "Write whatsapp message" """
        self.command5 = """5. Send an Email: To send an email, simply say "Write mail message" """
        
        self.commands = [self.command1, self.command2, self.command3, self.command4, self.command5]
        
        for command in self.commands:
            self.no1 = tk.Label(self.commands_window, text=command, fg="#fff", font=('Arial', 12), bg=self.bg, wraplength=350, justify="left")
            self.no1.pack(pady=5, padx=5)
    
    def open_whatsapp_window(self):
        self.whatsapp_window = tk.Toplevel(self.root)
        
        self.whatsapp_window.title("PAL WhatsApp sender")
        self.whatsapp_window.geometry("650x370")
        self.whatsapp_window.minsize(650,370)
        self.whatsapp_window.maxsize(650,370)
        self.whatsapp_window.configure(bg=self.bg)
        
        self.whatsapp_window_frame = tk.Frame(self.whatsapp_window, bg=self.bg)
        self.whatsapp_window_frame.columnconfigure(0, weight=1)
        self.whatsapp_window_frame.columnconfigure(1, weight=4)
        
        self.whatsapp_receiver_lbl = tk.Label(self.whatsapp_window_frame, text="Receiver:", bg=self.bg, fg='#fff', font=("Arial", 12, "normal"), justify='left')
        self.whatsapp_receiver_lbl.grid(row=0, column=0, sticky=tk.W, pady=15)
        
        self.whatsapp_receiver_txt = tk.Text(self.whatsapp_window_frame, width=10, height=1, font=("Arial", 12, "normal"))
        self.whatsapp_receiver_txt.grid(row=0, column=1, sticky=tk.W+tk.E, pady=15)
        
        self.whatsapp_message_lbl = tk.Label(self.whatsapp_window_frame, text="Message:", bg=self.bg, fg='#fff', font=("Arial", 12, "normal"), justify='left')
        self.whatsapp_message_lbl.grid(row=1, column=0, sticky=tk.W+tk.N, pady=15)
        
        self.whatsapp_message_txt = tk.Text(self.whatsapp_window_frame, width=10, height=8, font=("Arial", 12, "normal"))
        self.whatsapp_message_txt.grid(row=1, column=1, sticky=tk.W+tk.E, pady=15)
        
        self.whatsapp_btn = tk.Button(self.whatsapp_window_frame, text='Send Message', bg=self.opac_bg, fg='#fff', activebackground=self.light_bg, activeforeground='#fff', font=("Arial", 12, "normal"), pady=8, command=lambda:self.send_whatsapp_message(self.whatsapp_receiver_txt.get("1.0", "end-1c"), self.whatsapp_message_txt.get("1.0", "end-1c")))
        self.whatsapp_btn.grid(row=2, column=1, sticky=tk.W+tk.E, pady=15)

        
        self.whatsapp_window_frame.pack(padx=50, pady=25, fill='x')
    
    def send_whatsapp_message(self, receiver, message):
        print(receiver)
        print(message)
    
    def open_email_window(self):
        self.email_window = tk.Toplevel(self.root)
        
        self.email_window.title("PAL Email Sender")
        self.email_window.geometry("650x420")
        self.email_window.minsize(650,420)
        self.email_window.maxsize(650,420)
        self.email_window.configure(bg=self.bg)
        
        self.email_window_frame = tk.Frame(self.email_window, bg=self.bg)
        self.email_window_frame.columnconfigure(0, weight=1)
        self.email_window_frame.columnconfigure(1, weight=4)
        
        self.email_receiver_lbl = tk.Label(self.email_window_frame, text="Receiver:", bg=self.bg, fg='#fff', font=("Arial", 12, "normal"), justify='left')
        self.email_receiver_lbl.grid(row=0, column=0, sticky=tk.W, pady=15)
        
        self.email_receiver_txt = tk.Text(self.email_window_frame, width=10, height=1, font=("Arial", 12, "normal"))
        self.email_receiver_txt.grid(row=0, column=1, sticky=tk.W+tk.E, pady=15)
        
        self.email_subject_lbl = tk.Label(self.email_window_frame, text="Subject:", bg=self.bg, fg='#fff', font=("Arial", 12, "normal"), justify='left')
        self.email_subject_lbl.grid(row=1, column=0, sticky=tk.W, pady=15)
        
        self.email_subject_txt = tk.Text(self.email_window_frame, width=10, height=1, font=("Arial", 12, "normal"))
        self.email_subject_txt.grid(row=1, column=1, sticky=tk.W+tk.E, pady=15)
        
        self.email_message_lbl = tk.Label(self.email_window_frame, text="Message:", bg=self.bg, fg='#fff', font=("Arial", 12, "normal"), justify='left')
        self.email_message_lbl.grid(row=2, column=0, sticky=tk.W+tk.N, pady=15)
        
        self.email_message_txt = tk.Text(self.email_window_frame, width=10, height=8, font=("Arial", 12, "normal"))
        self.email_message_txt.grid(row=2, column=1, sticky=tk.W+tk.E, pady=15)
        
        self.email_btn = tk.Button(self.email_window_frame, text='Send Email', bg=self.opac_bg, fg='#fff', activebackground=self.light_bg, activeforeground='#fff', font=("Arial", 12, "normal"), pady=8, command=lambda:self.send_email_message(self.email_receiver_txt.get("1.0", "end-1c"), self.email_subject_txt.get("1.0", "end-1c"), self.email_message_txt.get("1.0", "end-1c")))
        self.email_btn.grid(row=3, column=1, sticky=tk.W+tk.E, pady=15)

        
        self.email_window_frame.pack(padx=30, pady=25, fill='x')
    
    def send_email_message(self, receiver, subject, message):
        print(receiver)
        print(subject)
        print(message)
        # print(f"{datetime.time.hour} : {datetime.time.min}")
    
    def open_dictionary_window(self):
        self.dictionary_window = tk.Toplevel(self.root)
        
        self.dictionary_window.title("PAL Dico")
        self.dictionary_window.geometry("450x450")
        self.dictionary_window.configure(bg=self.bg)
        
        self.dic_filler = tk.Label(self.dictionary_window, text="", bg=self.bg, fg=self.bg)
        self.dic_filler.pack()
        
        self.word_lbl = tk.Label(self.dictionary_window, text="Enumerate", bg=self.light_bg, fg='#fff', font=('Arial', 15, 'bold', 'italic'), pady=10)
        self.word_lbl.pack(padx=20, fill='x')
        
        self.word_transcription = tk.Label(self.dictionary_window, text="/E nu me rat/", bg=self.bg, fg='#fff', font=('Arial', 11, 'bold', 'italic'), pady=10)
        self.word_transcription.pack(padx=20, pady=0, fill='x')
        
        self.word_tense = tk.Label(self.dictionary_window, text="verb", bg=self.bg, fg='#fff', font=('Arial', 10, 'bold', 'underline'), pady=0)
        self.word_tense.pack(padx=20, pady=0, fill='x')
        
        self.word_meaning = tk.Label(self.dictionary_window, text="Hi, I'm PAL, your virtual assistant I'm PAL, your virtual assistant I'm PAL, your virtual assistant I'm PAL, your virtual assistant I'm PAL, your virtual assistant", height=10, bg=self.light_bg, fg="#fff", highlightthickness=1, font=('Montserrat', 13), wraplength=350, justify="center")
        self.word_meaning.pack(padx=20, pady=30, fill='x')
        
        self.dictionary_btns_frame = tk.Frame(self.dictionary_window, bg=self.bg)
        self.dictionary_btns_frame.columnconfigure(0, weight=1)
        self.dictionary_btns_frame.columnconfigure(1, weight=1)
        
        self.google_btn = tk.Button(self.dictionary_btns_frame, text='Google', bg=self.opac_bg, fg='#fff', activebackground=self.light_bg, activeforeground='#fff', font=("Arial", 12, "normal"), pady=8)
        self.google_btn.grid(row=0, column=0, sticky=tk.W+tk.E, padx=10)
        
        self.dictionary_close_btn = tk.Button(self.dictionary_btns_frame, text='Close', bg=self.opac_bg, fg='#fff', activebackground=self.light_bg, activeforeground='#fff', font=("Arial", 12, "normal"), pady=8)
        self.dictionary_close_btn.grid(row=0, column=1, sticky=tk.W+tk.E, padx=10)
        
        self.dictionary_btns_frame.pack(fill='x')

Pal()
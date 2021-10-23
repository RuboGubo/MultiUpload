import tkinter as tk
from tkinter import ttk
from EventHandeler import postEvent

class LoginUsernamePasswordPrompt(tk.Tk):
    def __init__(self, platfrom):
        super().__init__()
        
        self.platfrom = platfrom

        self.geometry("240x100")
        self.title('Login to ' + platfrom)
        self.resizable(0, 0)

        # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        
        # Configure Variables to access UserImput
        self.Password = tk.StringVar()
        self.Username = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # username
        username_label = ttk.Label(self, text="Username:")
        username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        username_entry = ttk.Entry(self, textvariable=self.Username)
        username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

        # password
        password_label = ttk.Label(self, text="Password:")
        password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        password_entry = ttk.Entry(self,  show="*", textvariable=self.Password)
        password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

        # login button
        login_button = ttk.Button(self, text="Login")
        login_button.bind('<Button>', self.updatePreferances)
        login_button['command'] = lambda: self.quit()
        login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)
        
    def updatePreferances(self, event):
        postEvent(self.platfrom.lower() + 'UserNameAndPasswordLogin', [self.Username.get(), self.Password.get()])
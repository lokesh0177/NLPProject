from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import API



class NLPApp:

    def __init__(self):
        # create db object
        self.apio = API()
        self.dbo = Database()
        # login Gui
        self.root = Tk()
        self.root.title("NLP APP")
        self.root.geometry('350x600')
        self.root.configure(bg='#34495E')
        self.login_gui()
        self.root.mainloop()

    def login_gui(self):
        self.clear()
        heading = Label(self.root, text="NLPApp", bg='#34495E', fg='white')
        heading.pack()
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        label1 = Label(self.root, text="Enter Email")
        label1.pack(pady=(10, 10))

        self.email_input = Entry(self.root, width=50)
        self.email_input.pack(pady=(5, 10), ipady=4)

        label1 = Label(self.root, text="Enter Password")
        label1.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=50, show='*')
        self.password_input.pack(pady=(5, 10), ipady=4)

        login_btn = Button(self.root, text='Login', width=30, height=2, command=self.perform_login)
        login_btn.pack(pady=(10, 10))

        label3 = Label(self.root, text="Not a Member")
        label3.pack(pady=(20, 10))

        redirect_btn = Button(self.root, text='Register Now', command=self.register_gui)
        redirect_btn.pack(pady=(10, 10))

    def register_gui(self):
        # clear the existing GuI
        self.clear()
        heading = Label(self.root, text="NLPApp", bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        label0 = Label(self.root, text="Enter Name")
        label0.pack(pady=(10, 10))

        self.name_input = Entry(self.root, width=50)
        self.name_input.pack(pady=(5, 10), ipady=4)

        label1 = Label(self.root, text="Enter Email")
        label1.pack(pady=(10, 10))

        self.email_input = Entry(self.root, width=50)
        self.email_input.pack(pady=(5, 10), ipady=4)

        label1 = Label(self.root, text="Enter Password")
        label1.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=50, show='*')
        self.password_input.pack(pady=(5, 10), ipady=4)

        register_btn = Button(self.root, text='Register', width=30, height=2, command=self.perform_registration)
        register_btn.pack(pady=(10, 10))

        label3 = Label(self.root, text="Already a member?")
        label3.pack(pady=(20, 10))

        redirect_btn = Button(self.root, text='Login Now', command=self.login_gui)
        redirect_btn.pack(pady=(10, 10))

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def perform_registration(self):
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()
        response = self.dbo.add_data(name, email, password)

        if response:
            messagebox.showinfo('Success', 'Registration Succesful. You can login now')
        else:
            messagebox.showerror('Error', 'Email does not exist')

    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()
        response = self.dbo.search(email, password)

        if response:
            messagebox.showinfo('success', 'Login Succesful')
            self.home_gui()
        else:
            messagebox.showerror('Error', 'Incorrect email/password')

    def home_gui(self):
        self.clear()
        heading = Label(self.root, text="NLPApp", bg='#34495E', fg='white')
        heading.pack()
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))
        sentiment_btn = Button(self.root, text='Sentiment Analysis', width=30, height=4, command=self.sentiment_gui)
        sentiment_btn.pack(pady=(10, 10))
        ner_btn = Button(self.root, text='Name Entity Recognition', width=30, height=4, command=self.ner_gui)
        ner_btn.pack(pady=(10, 10))
        emotion_btn = Button(self.root, text='Emotion Prediction', width=30, height=4,command=self.emotion_gui)
        emotion_btn.pack(pady=(10, 10))

        logout_btn = Button(self.root, text='LogOut', command=self.login_gui)
        logout_btn.pack(pady=(10, 10))

    def sentiment_gui(self):
        self.clear()
        heading = Label(self.root, text="NLPApp", bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))
        heading2 = Label(self.root, text="Sentiment Analysis", bg='#34495E', fg='white')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 20))

        label1 = Label(self.root, text="Enter the text")
        label1.pack(pady=(10, 10))
        
        self.sentiment_input = Entry(self.root, width=50)
        self.sentiment_input.pack(pady=(5, 10), ipady=4)

        sentiment_btn = Button(self.root, text='Analyze Sentiment', width=30, height=4,command=self.do_sentiment_analysis)
        sentiment_btn.pack(pady=(10, 10))


        self.sentiment_result = Label(self.root, bg='#34495E', fg='white')
        self.sentiment_result.pack(pady=(10, 10))
        self.sentiment_result.configure(font=('verdana',16))


        goback_btn = Button(self.root, text='Go back', width=30, height=4, command=self.home_gui)
        goback_btn.pack(pady=(10, 10))

    def ner_gui(self):
        self.clear()
        heading = Label(self.root, text="NLPApp", bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))
        heading2 = Label(self.root, text="Name Entity Recognition", bg='#34495E', fg='white')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 20))

        label1 = Label(self.root, text="Enter the text")
        label1.pack(pady=(10, 10))

        self.ner_input = Entry(self.root, width=50)
        self.ner_input.pack(pady=(5, 10), ipady=4)

        ner_btn = Button(self.root, text='Extract', width=30, height=4,
                             command=self.do_ner_analysis)
        ner_btn.pack(pady=(10, 10))

        self.ner_result = Label(self.root, bg='#34495E', fg='white')
        self.ner_result.pack(pady=(10, 10))
        self.ner_result.configure(font=('verdana', 16))

        goback_btn = Button(self.root, text='Go back', width=30, height=4, command=self.home_gui)
        goback_btn.pack(pady=(10, 10))




    def emotion_gui(self):
        self.clear()
        heading = Label(self.root, text="NLPApp", bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))
        heading2 = Label(self.root, text="Emotion Analysis", bg='#34495E', fg='white')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 20))

        label1 = Label(self.root, text="Enter the text")
        label1.pack(pady=(10, 10))

        self.emotion_input = Entry(self.root, width=50)
        self.emotion_input.pack(pady=(5, 10), ipady=4)

        emotion_btn = Button(self.root, text='Analyze Emotion', width=30, height=4,
                               command=self.do_emotion_analysis)
        emotion_btn.pack(pady=(10, 10))

        self.emotion_result = Label(self.root, bg='#34495E', fg='white')
        self.emotion_result.pack(pady=(10, 10))
        self.emotion_result.configure(font=('verdana', 16))

        goback_btn = Button(self.root, text='Go back', width=30, height=4, command=self.home_gui)
        goback_btn.pack(pady=(10, 10))

    def do_sentiment_analysis(self):
        text = self.sentiment_input.get()
        result = self.apio.sentiment_analysis(text)

        txt = ''

        for i in result['sentiment']:
            txt = txt + i + ' -> ' + str(result['sentiment'][i]) + '\n'


        self.sentiment_result['text'] = txt

    def do_emotion_analysis(self):
        text = self.emotion_input.get()
        result = self.apio.emotion_analysis(text)


        txt = ''
        for i in result['emotion']:
            txt = txt + i + ' -> ' + str(result['emotion'][i]) + '\n'

        self.emotion_result['text'] = txt

    def do_ner_analysis(self):
        text = self.ner_input.get()
        result = self.apio.ner_analysis(text)
        print(result)

        txt = ''
        for i in result['entities']:
            name = i["name"]
            category = i["category"]
            txt += f"Category '->' {category}\n Name '->' {name}\n "

        self.ner_result['text'] = txt


nlp = NLPApp()

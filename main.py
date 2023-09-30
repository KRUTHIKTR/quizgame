from tkinter import *
from tkinter.ttk import Progressbar
from pygame import mixer
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0])

mixer.init()

mixer.music.load('kbc.mp3')
mixer.music.play(-1)


def select(event):
    callButton.place_forget()
    progressbarA.place_forget()
    progressbarB.place_forget()
    progressbarC.place_forget()
    progressbarD.place_forget()

    ProgressbarlabelA.place_forget()
    ProgressbarlabelB.place_forget()
    ProgressbarlabelC.place_forget()
    ProgressbarlabelD.place_forget()

    b = event.widget
    value = b['text']
    for i in range(15):
        if value == correct_answers[i]:
            if value == correct_answers[14]:
                def close():
                    root2.destroy()
                    root.destroy()

                def playagain():
                    lifeline50Button.config(state=NORMAL, image=image50)
                    audiencepollButton.config(state=NORMAL, image=audiencepoll)
                    phoneafriendButton.config(state=NORMAL, image=phoneafriend)
                    root2.destroy()
                    questionArea.delete(1.0, END)
                    questionArea.insert(END, questions[0])

                    optionButton1.config(text=option_1[0])
                    optionButton2.config(text=option_2[0])
                    optionButton3.config(text=option_3[0])
                    optionButton4.config(text=option_4[0])

                    amountLabel.config(image=amountimage)

                mixer.music.stop()
                mixer.music.load('Kbcwon.mp3')
                mixer.music.play()

                root2 = Toplevel()
                root2.overrideredirect(True)
                root2.config(bg='black')
                root2.geometry('500x400+140+30')
                root2.title('Failure')
                imglabel = Label(root2, image=centerimage, bd=0)
                imglabel.pack(pady=30)

                winlabel = Label(root2, text='Congratulations\nYou Won', font=('arial', 20, 'bold'), bg='black',
                                 fg='yellow')
                winlabel.pack()
                playagainbutton = Button(root2, text='Play again', font=('arial', 15, 'bold'), bg='black', fg='white',
                                         activebackground='black', activeforeground='white', bd=0, cursor='hand2',
                                         command=playagain)
                playagainbutton.pack()

                closebutton = Button(root2, text='close', font=('arial', 15, 'bold'), bg='black', fg='red',
                                     activebackground='black', activeforeground='red', bd=0, cursor='hand2',
                                     command=close)
                closebutton.pack()

                root2.mainloop()
                break

            questionArea.delete(1.0, END)
            questionArea.insert(END, questions[i + 1])

            optionButton1.config(text=option_1[i + 1],activebackground='green')
            optionButton2.config(text=option_2[i + 1],activebackground='green')
            optionButton3.config(text=option_3[i + 1],activebackground='green')
            optionButton4.config(text=option_4[i + 1],activebackground='green')
            amountLabel.config(image=amountimages[i],activebackground='green')

        if value not in correct_answers:
            def close():
                root1.destroy()
                root.destroy()

            def tryagain():
                lifeline50Button.config(state=NORMAL, image=image50)
                audiencepollButton.config(state=NORMAL, image=audiencepoll)
                phoneafriendButton.config(state=NORMAL, image=phoneafriend)
                root1.destroy()
                questionArea.delete(1.0, END)
                questionArea.insert(END, questions[0])

                optionButton1.config(text=option_1[0])
                optionButton2.config(text=option_2[0])
                optionButton3.config(text=option_3[0])
                optionButton4.config(text=option_4[0])

                amountLabel.config(image=amountimage)

            root1 = Toplevel()
            root1.overrideredirect(True)
            root1.config(bg='black')
            root1.geometry('500x400+140+30')
            root1.title('Failure')
            imglabel = Label(root1, image=centerimage, bd=0)
            imglabel.pack(pady=30)

            loselabel = Label(root1, text='Better Luck\n Next Time!!', font=('arial', 20, 'bold'), bg='black',
                              fg='yellow')
            loselabel.pack()

            tryagainbutton = Button(root1, text='Try again', font=('arial', 15, 'bold'), bg='black', fg='white',
                                    activebackground='black', activeforeground='white', bd=0, cursor='hand2',
                                    command=tryagain)
            tryagainbutton.pack()

            closebutton = Button(root1, text='close', font=('arial', 15, 'bold'), bg='black', fg='red',
                                 activebackground='black', activeforeground='red', bd=0, cursor='hand2',
                                 command=close)
            closebutton.pack()

            root1.mainloop()
            break


def lifeline50():
    lifeline50Button.config(image=image50x, state=DISABLED)
    if questionArea.get(1.0, 'end-1c') == questions[0]:
        optionButton1.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[1]:
        optionButton1.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[2]:
        optionButton1.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[3]:
        optionButton1.config(text='')
        optionButton2.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[4]:
        optionButton1.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[5]:
        optionButton1.config(text='')
        optionButton2.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[6]:
        optionButton3.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[7]:
        optionButton1.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[8]:
        optionButton1.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[9]:
        optionButton1.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[10]:
        optionButton1.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[11]:
        optionButton4.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[12]:
        optionButton4.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[13]:
        optionButton4.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[14]:
        optionButton1.config(text='')
        optionButton3.config(text='')


def audiencepolllifeline():
    audiencepollButton.config(image=audiencepollx, state=DISABLED)
    progressbarA.place(x=580, y=190)
    progressbarB.place(x=620, y=190)
    progressbarC.place(x=660, y=190)
    progressbarD.place(x=700, y=190)

    ProgressbarlabelA.place(x=580, y=320)
    ProgressbarlabelB.place(x=620, y=320)
    ProgressbarlabelC.place(x=660, y=320)
    ProgressbarlabelD.place(x=700, y=320)

    if questionArea.get(1.0, 'end-1c') == questions[0]:
        progressbarA.config(value=30)
        progressbarB.config(value=90)
        progressbarC.config(value=60)
        progressbarD.config(value=40)

    if questionArea.get(1.0, 'end-1c') == questions[1]:
        progressbarA.config(value=40)
        progressbarB.config(value=30)
        progressbarC.config(value=90)
        progressbarD.config(value=20)

    if questionArea.get(1.0, 'end-1c') == questions[2]:
        progressbarA.config(value=30)
        progressbarB.config(value=90)
        progressbarC.config(value=60)
        progressbarD.config(value=40)

    if questionArea.get(1.0, 'end-1c') == questions[3]:
        progressbarA.config(value=60)
        progressbarB.config(value=40)
        progressbarC.config(value=90)
        progressbarD.config(value=30)

    if questionArea.get(1.0, 'end-1c') == questions[4]:
        progressbarA.config(value=60)
        progressbarB.config(value=40)
        progressbarC.config(value=90)
        progressbarD.config(value=20)

    if questionArea.get(1.0, 'end-1c') == questions[5]:
        progressbarA.config(value=20)
        progressbarB.config(value=40)
        progressbarC.config(value=90)
        progressbarD.config(value=70)

    if questionArea.get(1.0, 'end-1c') == questions[6]:
        progressbarA.config(value=60)
        progressbarB.config(value=90)
        progressbarC.config(value=40)
        progressbarD.config(value=20)

    if questionArea.get(1.0, 'end-1c') == questions[7]:
        progressbarA.config(value=20)
        progressbarB.config(value=90)
        progressbarC.config(value=70)
        progressbarD.config(value=30)

    if questionArea.get(1.0, 'end-1c') == questions[8]:
        progressbarA.config(value=30)
        progressbarB.config(value=90)
        progressbarC.config(value=70)
        progressbarD.config(value=40)

    if questionArea.get(1.0, 'end-1c') == questions[9]:
        progressbarA.config(value=30)
        progressbarB.config(value=90)
        progressbarC.config(value=70)
        progressbarD.config(value=20)

    if questionArea.get(1.0, 'end-1c') == questions[10]:
        progressbarA.config(value=20)
        progressbarB.config(value=90)
        progressbarC.config(value=70)
        progressbarD.config(value=50)

    if questionArea.get(1.0, 'end-1c') == questions[11]:
        progressbarA.config(value=70)
        progressbarB.config(value=90)
        progressbarC.config(value=40)
        progressbarD.config(value=20)

    if questionArea.get(1.0, 'end-1c') == questions[12]:
        progressbarA.config(value=60)
        progressbarB.config(value=90)
        progressbarC.config(value=50)
        progressbarD.config(value=30)

    if questionArea.get(1.0, 'end-1c') == questions[13]:
        progressbarA.config(value=70)
        progressbarB.config(value=90)
        progressbarC.config(value=40)
        progressbarD.config(value=10)

    if questionArea.get(1.0, 'end-1c') == questions[14]:
        progressbarA.config(value=20)
        progressbarB.config(value=90)
        progressbarC.config(value=70)
        progressbarD.config(value=50)


def phoneafriendlifeline():
    mixer.music.load('calling.mp3')
    mixer.music.play()
    callButton.place(x=70, y=260)
    phoneafriendButton.config(image=phoneafriendx, state=DISABLED)


def phoneclick():
    for i in range(15):
        if questionArea.get(1.0, 'end-1c') == questions[i]:
            engine.say(f'the answer is{correct_answers[i]}')
            engine.runAndWait()


correct_answers = [
    'SEBI', 'FSSAI', 'Bengaluru',
    'Coal Ministry', 'Goa', 'Rs 6002 crore',
    'Magnus Carlsen', 'Austria', 'Cricket',
    'Nepal', 'WaterVision2047', 'France',
    'RBI', 'Alzheimer', 'Motor Racing',
]

questions = [
    "Which institution has urged stock exchanges to set up Investor Risk Reduction Access (IRRA) platform?",
    "G Kamala Vardhana Rao has taken over the charge as the CEO of which institution?",
    "Which city is the host of ‘Cooperative Beneficiaries Conference",
    "Which Union Ministry is developing Eco-Parks on reclaimed land and to promote mine tourism?",
    "Zuari Bridge, the second largest cable-stayed bridge in India, is located in which state/UT?",
    "What is the total investment made by the Department of Science & Technology in the Science and Technology system in 2022-23?",
    "Which sportsperson won both the World Rapid and World Blitz chess titles",
    "India recently signed a ‘Comprehensive Migration and Mobility Partnership Agreement’ in which country?",
    "Which sports authority recently introduced ‘Yo-Yo and Dexa Tests’ in team selection criteria?",
    "Which country inaugurated the Pokhara Regional International Airport (PRIA), with the support of China?",
    "What is the theme of ‘All India Annual State Ministers Conference on Water",
    "India’s National Security Adviser Ajit Doval held a Strategic Dialogue with his counterpart from which country?",
    "Which institution has authorised six fintech entities to test their products under regulatory sandbox scheme?",
    "‘Lecanemab’, which was granted approval by the US FDA, is used to treat which disease?",
    "Chirag Ghropade, who was seen in the news, plays which sports?",
]

option_1 = [
    "RBI", "myGOV", "Chennai",
    "Power Ministry", "Arunachal\nPradesh", "Rs 2002 crore",
    "R Praggnananda", "Sri Lanka", "Hockey",
    "Sri Lanka", "Bharat\nAmritKaal", "USA",
    "NITI Aayog", " COVID-19", "Chess",
]

option_2 = [
    "SEBI", " UIDAI", "Bengaluru",
    "Mines Ministry", "Punjab", "Rs 4002 crore",
    "Magnus Carlsen", "Austria", "Cricket",
    "Nepal", "WaterVision2047", "France",
    "RBI", "Alzheimer", "Motor Racing",
]

option_3 = [
    "NITI Aayog", "FSSAI", "Cochin",
    "Coal Ministry", "Goa", "Rs 6002 crore",
    "Koneru Humpy", "UAE", "Weight Lifting",
    "Bangladesh", "AmritPaani2047", "Australia",
    "SEBI", "Cancer", "Weight Lifting",
]

option_4 = [
    "SupremeCourt", "FCI", "Ahmedabad",
    "Steel Ministry", "Jammu\nKashmir", "Rs 8002 crore",
    "Harika Dronavalli", "Bangladesh", "Archery",
    "Bhutan", "Sustainable Water", "Sri Lanka",
    "NSE", "Diabetes", "Archery",
]

root = Tk()

root.geometry('1270x652+0+0')
root.title('karunada kotyadipathi')

root.config(bg='black')

leftframe = Frame(root, bg='black', padx=90)
leftframe.grid(row=0, column=0)

topFrame = Frame(leftframe, bg='black', pady=15)
topFrame.grid(row=0, column=0)

centerFrame = Frame(leftframe, bg='black', pady=15)
centerFrame.grid(row=1, column=0)

bottomFrame = Frame(leftframe)
bottomFrame.grid(row=2, column=0)

rightframe = Frame(root, pady=25, padx=50, bg='black')
rightframe.grid(row=0, column=1)

image50 = PhotoImage(file='50-50.png')
image50x = PhotoImage(file='50-50-X.png')
lifeline50Button = Button(topFrame, image=image50, bg='black', bd=0, activebackground='black', width=180, height=80,
                          command=lifeline50)
lifeline50Button.grid(row=0, column=0)

audiencepoll = PhotoImage(file='audiencePole.png')
audiencepollx = PhotoImage(file='audiencePoleX.png')
audiencepollButton = Button(topFrame, image=audiencepoll, bg='black', bd=0, activebackground='black', width=180,
                            height=80,
                            command=audiencepolllifeline)
audiencepollButton.grid(row=0, column=1)

phoneafriend = PhotoImage(file='phoneAFriend.png')
phoneafriendx = PhotoImage(file='phoneAFriendX.png')
phoneafriendButton = Button(topFrame, image=phoneafriend, bg='black', bd=0, activebackground='black', width=180,
                            height=80,
                            command=phoneafriendlifeline)
phoneafriendButton.grid(row=0, column=2)

callimage = PhotoImage(file='phone.png')

callButton = Button(root, image=callimage, bd=0, bg='black', activebackground='black', cursor='hand2',
                    command=phoneclick)

centerimage = PhotoImage(file='center.png')

logolabel = Label(centerFrame, image=centerimage, bg='black', width=300, height=200)
logolabel.grid(row=0, column=0)

amountimage = PhotoImage(file='Picture0.png')
amountimage1 = PhotoImage(file='Picture1.png')
amountimage2 = PhotoImage(file='Picture2.png')
amountimage3 = PhotoImage(file='Picture3.png')
amountimage4 = PhotoImage(file='Picture4.png')
amountimage5 = PhotoImage(file='Picture5.png')
amountimage6 = PhotoImage(file='Picture6.png')
amountimage7 = PhotoImage(file='Picture7.png')
amountimage8 = PhotoImage(file='Picture8.png')
amountimage9 = PhotoImage(file='Picture9.png')
amountimage10 = PhotoImage(file='Picture10.png')
amountimage11 = PhotoImage(file='Picture11.png')
amountimage12 = PhotoImage(file='Picture12.png')
amountimage13 = PhotoImage(file='Picture13.png')
amountimage14 = PhotoImage(file='Picture14.png')
amountimage15 = PhotoImage(file='Picture15.png')

amountimages = [amountimage1, amountimage2, amountimage3,
                amountimage4, amountimage5, amountimage6,
                amountimage7, amountimage8, amountimage9,
                amountimage10, amountimage11, amountimage12,
                amountimage13, amountimage14, amountimage15]

amountLabel = Label(rightframe, image=amountimage, bg='black')
amountLabel.grid(row=0, column=0)

layoutImage = PhotoImage(file='lay.png')
layoutLabel = Label(bottomFrame, image=layoutImage, bg='black')
layoutLabel.grid(row=0, column=0)

questionArea = Text(bottomFrame, font=('arial', 18, 'bold'), width=34, height=2, wrap='word', bg='black', fg='white',
                    bd=0)
questionArea.place(x=70, y=10)

questionArea.insert(END, questions[0])

labelA = Label(bottomFrame, text='A:', bg='black', fg='white', font=('arial', 16, 'bold'))
labelA.place(x=60, y=110)
optionButton1 = Button(bottomFrame, text=option_1[0], font=('arial', 15, 'bold'), bg='black', fg='white', bd=0,
                       activebackground='black', activeforeground='white', cursor='hand2')
optionButton1.place(x=100, y=100)

labelB = Label(bottomFrame, text='B:', bg='black', fg='white', font=('arial', 16, 'bold'))
labelB.place(x=330, y=110)
optionButton2 = Button(bottomFrame, text=option_2[0], font=('arial', 15, 'bold'), bg='black', fg='white', bd=0,
                       activebackground='black', activeforeground='white', cursor='hand2')
optionButton2.place(x=370, y=100)

labelC = Label(bottomFrame, text='C:', bg='black', fg='white', font=('arial', 16, 'bold'))
labelC.place(x=60, y=190)
optionButton3 = Button(bottomFrame, text=option_3[0], font=('arial', 15, 'bold'), bg='black', fg='white', bd=0,
                       activebackground='black', activeforeground='white', cursor='hand2')
optionButton3.place(x=100, y=180)

labelD = Label(bottomFrame, text='D:', bg='black', fg='white', font=('arial', 16, 'bold'))
labelD.place(x=330, y=190)
optionButton4 = Button(bottomFrame, text=option_4[0], font=('arial', 15, 'bold'), bg='black', fg='white', bd=0,
                       activebackground='black', activeforeground='white', cursor='hand2')
optionButton4.place(x=355, y=180)

progressbarA = Progressbar(root, orient=VERTICAL, length=120)
progressbarB = Progressbar(root, orient=VERTICAL, length=120)
progressbarC = Progressbar(root, orient=VERTICAL, length=120)
progressbarD = Progressbar(root, orient=VERTICAL, length=120)

ProgressbarlabelA = Label(root, text='A', font=('arial', 20, 'bold'), bg='black', fg='white')
ProgressbarlabelB = Label(root, text='B', font=('arial', 20, 'bold'), bg='black', fg='white')
ProgressbarlabelC = Label(root, text='C', font=('arial', 20, 'bold'), bg='black', fg='white')
ProgressbarlabelD = Label(root, text='D', font=('arial', 20, 'bold'), bg='black', fg='white')

optionButton1.bind('<Button-1>', select)
optionButton2.bind('<Button-1>', select)
optionButton3.bind('<Button-1>', select)
optionButton4.bind('<Button-1>', select)

root.mainloop()

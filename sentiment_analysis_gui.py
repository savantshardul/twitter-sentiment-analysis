import sys
import os
from tkinter import *
import getTweets as gt
import tkinter.messagebox
import time




def mainFunctionGraph():
    #mtext = ment.get()
    #mlabel2 = Label(mGui, text = mtext).pack()
    os.system('python sentiment_graph.py')
    return

def mainFunctionTweet(event):
	time.sleep(5)
	tweet = mtweet.get()
	location = mlocation.get()
	print ("Tweet key-word is "+tweet+"\n")
	print ("Tweet's location sets to "+location+"\n")
	temp="Sentiment is being generated for the keyword ("+tweet+") and location ("+location+")"
	label_5 = Label(mGui, text =temp,font=("Tahoma", 20),foreground="blue")
	label_5.grid(row=7,columnspan=3)
	open('twitter-out.txt', 'w').close()
	time.sleep(5)
	label_6 = Label(mGui, text ="Now click on - 'Get Sentiment Graph' to see the graph",font=("Tahoma", 20),foreground="blue")
	label_6.grid(row=8,columnspan=3)
	gt.ProcessTweets(tweet,location)
	#os.system('python sentiment_analysis.py ' + mtweet.get())
	return

	

mGui = Tk()
mGui.state('zoomed')
ment = StringVar()

mGui.geometry('1000x1000+1000+1000')
mGui.title('Twitter Sentiment Analysis')
logo = PhotoImage(file="data/back.png")
w1 = Label(mGui, image=logo)
w1.grid(row=0,columnspan=3)
label_1 = Label(mGui, text = 'Twitter Sentiment Analysis',font=("Tahoma", 40),foreground="green")
label_1.grid(row=1,columnspan=3)
label_2 = Label(mGui, text = '    (This application will let you get the insight of people based on location for any specific topic or brand)',font=("Tahoma", 20),foreground="red")
label_2.grid(row=2,columnspan=3)
mtweet = StringVar()
mlocation = StringVar()
label_3 = Label(mGui, text = 'Enter Interest : ',font=("Tahoma", 20),foreground="black")
label_3.grid(row=4,sticky=E)
entry_1 = Entry (mGui, bd=3,textvariable=mtweet)
entry_1.grid(row=4,column=1,sticky=W)
entry_1.insert(END, 'E.g. Apple')
label_4 = Label(mGui, text = 'Enter Location : ',font=("Tahoma", 20),foreground="black")
label_4.grid(row=6,sticky=E)
entry_2 = Entry (mGui, bd=3,textvariable=mlocation)
entry_2.grid(row=6,column=1,sticky=W)
entry_2.insert(END, 'E.g. Los Angeles')
button_1 = Button(mGui, text = 'Get Sentiment Graph',width=20, height=1,command=mainFunctionGraph)
button_1.grid(row=4,column=2,sticky=W)
button_2 = Button(mGui, text = 'Process Tweets',width=20, height=1)
button_2.grid(row=6,column=2,sticky=W)
button_2.bind("<Button-1>",mainFunctionTweet)



mGui.mainloop()





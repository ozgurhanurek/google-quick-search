#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
import webbrowser
import time
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class CustomSearch:
	def __init__(self, root):
		root.configure(background="#D7D7D7")
		frame=Frame(root)     #Frame to set paddings correctly 
		frame.grid(pady=10,padx=10)
		frame.config(background="#D7D7D7")
		self.markUpVar=IntVar()
		self.param2Var=IntVar()
		self.queriesVar=StringVar()

		self.label_1 = Label(frame, text="Queries",background="#D7D7D7")
		self.label_1.grid(row=0, column=0)	

		self.label_3 = Label(frame, text="Number of Queries Made",background="#D7D7D7")
		self.label_3.grid(row=3,column=2,sticky=S)

		#Number of Queries Label
		self.label_Number = Label(frame,text="0",background="#D7D7D7")
		self.label_Number.grid(row=4,column=2,sticky=N)

		#Queries Text Box
		self.text_Raw = Text(frame,width=50)
		self.text_Raw.grid(row=1,column=0,rowspan=5)

		#Markups Text Box
		self.text_MarkUp = Text(frame,width=50,height=10,state=DISABLED,bg=frame.cget('bg'))
		self.text_MarkUp.grid(row=7,rowspan=2)

		#Markups Check Box
		self.check_MarkUp=Checkbutton(frame, text="Append to Queries",command=self.MarkUpVisibility, variable=self.markUpVar,background="#D7D7D7")
		self.check_MarkUp.grid(row=6,column=0)

		#Search Button
		self.searchButton=Button(frame,text="Search",width=10,command=self.Search,background="#D7D7D7")
		self.searchButton.grid(row=5,column=2,sticky=N)

		#Clear Button
		self.clearButton=Button(frame,text="Clear",width=10,command=self.Clear,background="#D7D7D7")
		self.clearButton.grid(row=5,column=2,sticky=S)

	def Search(self):
		queries=self.text_Raw.get("1.0",'end-1c')			
		queriesList = []

		if self.markUpVar.get():
			for query in queries.split('\n'):
				queriesList.append(query)
				for markUp in self.text_MarkUp.get("1.0","end-1c").split('\n'):
					queriesList.append(query +" "+markUp)
		else:
			queriesList=queries.split('\n')

		numberOfQueries=0
		for query in queriesList:
			url = "https://www.google.com.tr/search?q=" + query
			webbrowser.open(url)
			numberOfQueries=numberOfQueries+1
			time.sleep(0.05)

		self.label_Number.config(text=str(numberOfQueries))

	def Clear(self):
		self.text_Raw.delete("1.0",'end-1c')
		self.label_Number.config(text="0")


	def MarkUpVisibility(self):
		if self.markUpVar.get():
			self.text_MarkUp.config(state=NORMAL,bg="white")
		else:
			self.text_MarkUp.config(state=DISABLED,bg=root.cget('bg'))


root=Tk()
root.title("Google Quick Search")
a=CustomSearch(root)
root.mainloop()
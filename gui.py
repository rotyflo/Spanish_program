'''
add: Our text to the window programaticly 
add: buttons to click for choices
'''
from tkinter import *
from PIL import Image, ImageTk
import words
import csv

# Initialize window as a subclass of Frame
class Window(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.master = master
		self.init_Window()
		
	# Create the master window
	def init_Window(self):
		# Window title
		self.master.title('GUI')
		self.pack(fill=BOTH, expand=1)

		# Create a message box
		self.text_message = StringVar()
		self.text_message.set("Press the button to start promting spanish words.")
		question_message = Message(self, textvariable=self.text_message)
		question_message.config(bg='#c0c0c0', font=('times',20), width=280)
		question_message.pack(fill=X)

		# Radiobuttons
		self.answer = IntVar()
		Radiobutton(self, text="One", variable=self.answer, value=1).pack(pady=5, padx=5, anchor=W)
		Radiobutton(self, text="Two", variable=self.answer, value=2).pack(pady=5, padx=5, anchor=W)
		Radiobutton(self, text="Three", variable=self.answer, value=3).pack(pady=5, padx=5, anchor=W)
		Radiobutton(self, text="Four", variable=self.answer, value=4).pack(pady=5, padx=5, anchor=W)

		# Create random word button. Added a function from words.py to the command attribute
		randButton = Button(self, text='Random Word', command=self.rand_row)
		randButton.pack(pady=20, padx=20, side=LEFT)		
		quitButton = Button(self, text='Quit', command=self.client_exit)
		quitButton.pack(pady=20, padx=20, side=RIGHT)

		# Create top menu bar
		menu = Menu(self.master)
		self.master.config(menu=menu)

		# Create file button with drop down menu
		file = Menu(menu)
		file.add_command(label='Exit', command=self.client_exit)
		menu.add_cascade(label='File', menu=file)

		# Create edit menu button with drop down menu
		edit = Menu(menu)
		edit.add_command(label='Show Image', command=self.showImg)
		edit.add_command(label='Show Text', command=self.showTxt)
		menu.add_cascade(label='Edit', menu=edit)

	# Show image cmd, will delete most likely
	def showImg(self):
		load = Image.open('pic.png')
		render = ImageTk.PhotoImage(load)

		img = Label(self, image=render)
		img.image = render
		img.place(x=50,y=50)

	# showtext cmd, will delete maybe if not needed
	def showTxt(self):
		text = Label(self, text='Hello')
		# The pack method tells Tk to fit the size of the window to the given text.
		text.pack()

	# quit command, probably expand on this one
	def client_exit(self):
		exit()

	# currently only sends a spanish word to our message when submited
	def rand_row(self):
		with open('100_words.csv', 'rt', encoding='utf8') as csv_file:
			open_csv_words = csv.reader(csv_file, delimiter=',')
			spanish_word, answer = words.rand_row(open_csv_words)
			self.text_message.set('What is the correct translation of: {}'.format(spanish_word.capitalize()))
		print(self.answer.get())


# root is designated as the root parent window
root = Tk()
# Tk method to set size of window
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
# Uncomment below for a centered window
root.geometry('+{}+{}'.format(positionRight,positionDown))
# uncomment below for a top left corner window
#root.geometry('400x300')
app = Window(root)

# Tkinter event loop
root.mainloop()

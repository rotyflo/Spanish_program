'''
add: Our text to the window programaticly 
add: buttons to click for choices
'''
from tkinter import *
from PIL import Image, ImageTk
import words

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
		text_message = "This is a message from a variable."
		question_message = Message(self, text=text_message)
		question_message.config(bg='#c0c0c0', font=('times', 20))
		question_message.pack()

		# Create quit button. Added a function from words.py to the command attribute
		quitButton = Button(self, text='Print 123', command=words.rand_choice)
		quitButton.place(x=0, y=0)

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

# root is designated as the root parent window
root = Tk()
# Tk method to set size of window
root.geometry("400x300")

app = Window(root)

# Tkinter event loop
root.mainloop()

'''
add: Our text to the window programaticly 
add: buttons to click for choices
'''
from tkinter import *
from PIL import Image, ImageTk

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

		# Create quit button
		quitButton = Button(self, text='Quit', command=self.client_exit)
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
		text.pack()

	# quit command, probably expand on this one
	def client_exit(self):
		exit()

# Look more into whats happening below
root = Tk()
root.geometry("400x300")
app = Window(root)

root.mainloop()
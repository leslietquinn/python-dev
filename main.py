from tkinter import *
import dev.factories as Qx

"""
Start 
"""
class App():	
	def __init__(self, root):
		self.root=root

		"""
		Ensure 100% of the width and equal height of the application window is entirely consumed by the parent frameset
		"""
		self.root.rowconfigure(0, weight=1)
		self.root.columnconfigure(0, weight=1)	

	def title(self, title):
		self.root.title(title)
		return self

	def size(self, size):
		self.root.geometry(size)
		self.root.resizable(width=False, height=False)
		return self

	def background(self, colour):
		self.root.config(bg=colour)
		return self

	def setup(self):
		factory=Qx.Setup(self.root)
		factory.make()

"""
End
"""
if __name__ == "__main__":
	root=Tk()
	
	root.tk_setPalette(
		background='#dcdcdc'
	  , foreground='#000000'
	  , activeBackground='#acacac'
	  , activeForeground="#ffffff")

	app=App(root)
	app.title("New Application").size("{}x{}".format(256, 256)).setup()
	
	root.mainloop()

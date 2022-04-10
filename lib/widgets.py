#from lib.core import *

from tkinter import *
from lib.core import *
from lib.managers import *

"""
Sharing common traits between several TKinter widgets, such as layout management
"""
class TWidgetBase():
	sticky="NESW"
	pad=TPad()

	def __init__(self):
		pass

	def flat(self):
		self.widget.config(relief="flat")
		return self

	def ridged(self):
		self.widget.config(relief="ridge")
		return self

	def raised(self):
		self.widget.config(relief="raised")
		return self

	def sunken(self):
		self.widget.config(relief="sunken")
		return self

	def grooved(self):
		self.widget.config(relief="groove")
		return self

	def east(self):
		self.sticky="E"
		return self

	def west(self):
		self.sticky="W"
		return self

	def north(self):
		self.sticky="N"
		return self

	def south(self):
		self.sticky="S"
		return self
		
	def south_east(self):
		self.sticky="SE"
		return self
		
	def north_east(self):
		self.sticky="NE"
		return self
		
	def south_west(self):
		self.sticky="SW"
		return self
		
	def north_west(self):
		self.sticky="NW"
		return self

	def pack(self, f):
		self.widget.pack(fill=f, padx=self.pad.get_x(), pady=self.pad.get_y(), ipadx=self.pad.get_x_internal(), ipady=self.pad.get_y_internal(), expand=True)
		return self

	def pack_left(self, f):
		self.widget.pack(fill=f, side=LEFT, padx=self.pad.get_x(), pady=self.pad.get_y(), ipadx=self.pad.get_x_internal(), ipady=self.pad.get_y_internal(), expand=True)
		return self

	def pack_right(self, f):
		self.widget.pack(fill=f, side=RIGHT, padx=self.pad.get_x(), pady=self.pad.get_y(), ipadx=self.pad.get_x_internal(), ipady=self.pad.get_y_internal(), expand=True)
		return self

	def pack_top(self, f):
		self.widget.pack(fill=f, side=TOP, padx=self.pad.get_x(), pady=self.pad.get_y(), ipadx=self.pad.get_x_internal(), ipady=self.pad.get_y_internal(), expand=True)
		return self

	def pack_bottom(self, f):
		self.widget.pack(fill=f, side=BOTTOM, padx=self.pad.get_x(), pady=self.pad.get_y(), ipadx=self.pad.get_x_internal(), ipady=self.pad.get_y_internal(), expand=True)
		return self

	### position entry by default, using row and column otherwise x and y pixel ###
	def position(self, hort, vert, grid=True):
		if grid:
			self.widget.grid(row=hort, column=vert, padx=self.pad.get_x(), pady=self.pad.get_y(), sticky=self.sticky)
		else:
			self.widget.place(x=hort, y=vert)
		return self

	def no_padding(self):
		self.pad.no_padding()
		return self

	def padding(self, x, y):
		self.pad.set_x(x)
		self.pad.set_y(y)
		return self

"""
Customised implementation that wraps the TKinter Frame()
"""
class TFrame(TWidgetBase):
	def __init__(self, root):
		super().__init__()

		self.widget=Frame(root)
		self.propagate_off()
		self.root=root

	def get_self(self):
		return self.widget

	def get_root(self):
		return self.root

	def propagate_on(self):
		self.widget.grid_propagate(True)
		self.widget.pack_propagate(True)
		return self

	def propagate_off(self):
		self.widget.grid_propagate(False)
		self.widget.pack_propagate(False)
		return self

	def grid_size(self):
		return self.widget.grid_size()

	def grid_info(self):
		return self.widget.grid_info()

	def background(self, colour):
		self.widget.config(bg=colour)
		return self

	def size(self, w, h):
		self.widget.config(width=w, height=h)
		return self
	
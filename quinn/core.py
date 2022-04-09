

"""
Faciliate access to a command palette through an abstraction
"""
class TCommandPalette():
	def __init__(self):
		return

	def trigger(self, variable):
		"""
		Return a new concrete instance, passing on data required
		"""
		return self.__class__(variable)

"""
A component to centralise padding for all widgets made, keeping padding equal behaviour for all widgets
"""
class TPad():
	x=0
	y=0
	internal_x=0
	internal_y=0

	def __init__(self):
		return

	def no_padding(self):
		self.x=0
		self.y=0
		self.internal_x=0
		self.internal_y=0

	def get_x(self):
		return self.x

	def get_y(self):
		return self.y

	def get_x_internal(self):
		return self.internal_x

	def get_y_internal(self):
		return self.internal_y

	def set_x(self, x):
		self.internal_x=x
		self.x=x

	def set_y(self, y):
		self.internal_y=y
		self.y=y

"""
A component to facilitate access to available font typeface and common sizes, in a standard centralised manner for the 
whole of the application to use
"""
class TFontLibrary():
	TYPEFACE = "Helvetica"

	def __init__(self):
		return

	def small(self):
		return (self.TYPEFACE, 10, "normal")

	def medium(self):
		return (self.TYPEFACE, 11, "normal")

	def large(self):
		return (self.TYPEFACE, 12, "normal")

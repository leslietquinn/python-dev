from quinnt.widgets import *
from quinnt.core import *

"""
Radio Button manager, store and facilitate access to one or more radio buttons
"""
class TRadioButtonManager():
	radio_buttons={}

	def __init__(self):
		self.radio_buttons={}

	def add_radio_button(self, root, text):
		length=len(self.radio_buttons)
		radio_button=TRadioButton(root, text)
		self.radio_buttons[length] = radio_button
		return radio_button

	def get_radio_button(self, radio_button):
		if radio_button in self.radio_buttons:
			return self.radio_buttons[radio_button]
		else:
			return None

"""
Entry manager, store and facilitate access to one or more entries
"""
class TEntryManager():
	entries={}

	def __init__(self):
		self.entries={}

	def add_entry(self, root):
		length=len(self.entries)
		entry=TEntry(root)
		self.entries[length] = entry
		return entry

	def get_entry(self, entry):
		if entry in self.entries:
			return self.entries[entry]
		else:
			return None

	def get_formatter(self):
		return self.formatter

"""
Label manager, store and facilitate access to one or more labels
"""
class TLabelManager():
	labels={}

	def __init__(self):
		self.labels={}

	def add_label(self, root, text):
		length=len(self.labels)
		label=TLabel(root, text)
		self.labels[length] = label
		return label

	def get_label(self, label):
		if label in self.labels:
			return self.labels[label]
		else:
			return None

	def get_formatter(self):
		return self.formatter

	def get_font_library(self):
		return TFontLibrary()

"""
Button manager, store and facilitate access to one or more buttons
"""
class TButtonManager():
	buttons={}

	def __init__(self):
		self.buttons={}

	def add_button(self, root, text):
		length=len(self.buttons)
		button=TButton(root, text)
		self.buttons[length] = button
		return button

	def get_button(self, button):
		if button in self.buttons:
			return self.buttons[button]
		else:
			return None

	def get_font_library(self):
		return TFontLibrary()

"""
Frameset manager, store and facilitate access to one or more frames
"""
class TFramesetManager():
	frameset={}

	def __init__(self):
		self.frameset={}

	def add_frame(self, root):
		length=len(self.frameset)
		frame=TFrame(root)
		self.frameset[length] = frame
		return frame

	def get_frame(self, frame):
		if frame in self.frameset:
			return self.frameset[frame]
		else:
			return None			

"""
LabelFrameset manager, store and facilitate access to one or more label frames
"""
class TLabelFramesetManager():
	frameset={}

	def __init__(self):
		self.frameset={}

	def add_label_frame(self, root):
		length=len(self.frameset)
		frame=TLabelFrame(root)
		self.frameset[length] = frame
		return frame

	def get_label_frame(self, frame):
		if frame in self.frameset:
			return self.frameset[frame]
		else:
			return None

"""
Spinbox manager, store and facilitate access to one or more spin boxes
"""
class TSpinBoxManager():
	boxes={}

	def __init__(self):
		self.boxes={}


	def add_spin_box(self, root):
		length=len(self.boxes)
		box=TSpinBox(root)
		self.boxes[length] = box
		return box

	def get_spin_box(self, box):
		if box in self.boxes:
			return self.boxes[box]
		else:
			return None

	def get_font_library(self):
		return TFontLibrary()
	
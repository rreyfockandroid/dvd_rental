import tkinter as tk
from model.gui_model import GuiModel

class WidgetBox():
    def __init__(self, model: GuiModel, label: tk.Label, widget: tk.Widget):
        self._widget = widget
        self._label = label
        self._model = model

    def getName(self):
        return self._label.cget("text")
    
    def getValue(self):
        return self._widget.get()
    
    def validate(self):
        try:
            self._model.type(self.getValue())
        except ValueError:
            print("validate error " + self.getName())
            return False
        return True
    


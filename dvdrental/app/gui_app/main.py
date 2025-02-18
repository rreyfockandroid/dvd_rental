import tkinter as tk
from frame.app_frame import App

from tkinter import ttk


def main():
    window = tk.Tk()
    app = App(window)
    app.run()

if __name__ == "__main__":
    main()
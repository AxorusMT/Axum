#Do NOT use this. Use the APP class instead!!!




class Window:
    def __init__(self, title, width, height, resizable, antialiasing):
        self.title = title
        self.width = width
        self.height = height
        self.resizable = resizable
        self.antialiasing = antialiasing

    def create_window(self):
        window = arcade.open_window(self.width, self.height, self.title, self.resizable, self.antialiasing)
        arcade.set
        return window



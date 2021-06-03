class AxumColor:
    #Basic Colours
    BLACK = (255, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    CYAN = (0, 255, 255)
    MAGENTA = (255, 0, 255)
    SILVER = (192, 192, 192)
    GREY = (128, 128, 128)
    GRAY = GREY
    DARK_RED = (128, 0, 0)
    DARK_YELLOW = (128, 128, 0)
    DARK_GREEN = (0, 128, 0)
    DARK_MAGENTA = (128, 0, 128)
    DARK_CYAN = (0, 128, 128)
    DARK_BLUE = (0, 0, 128)

    def invert_color(self, colour):
        c1 = 255 - colour[0]
        c2 = 255 - colour[1]
        c3 = 255 - colour[2]
        return c1, c2, c3

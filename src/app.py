import pygame
from log_error import LogError
import window

pygame.init()


class App:
    def __init__(self, title, width, height, color):
        self.title = title
        self.width = width
        self.height = height
        self.color = color


    def create_window(self):
        window_object = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)
        window_object.fill(self.color)
        pygame.display.update()
        return window_object


    def refresh_window(self, window_object, color):
        window_object.fill(color)
        pygame.display.update()

    def quit_app(self):
        LogError.warn("Quitting Application!")

    def run_app(self, runf):
        runf()
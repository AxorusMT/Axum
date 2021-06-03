from app import App
from axum_color import AxumColor
from log_error import LogError

import pygame
from pygame.locals import *

pygame.init()

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "My Axum App"

Game = App(WINDOW_TITLE, WINDOW_WIDTH, WINDOW_HEIGHT, AxumColor.MAGENTA)
Game.create_window()

run_app = True

def main():
    global run_app
    while run_app:
        for event in pygame.event.get():
            if event.type == QUIT:
                run_app = False
            if event.type == KEYDOWN:
                if event.type == K_ESCAPE:
                    run_app = False

    Game.quit_app()

Game.run_app(main)

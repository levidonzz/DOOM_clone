import pygame as pg

from settings import *


class ObjectRender:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()

    
    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()

    
    def load_wall_textures(self):
        return {
            1: self.get_texture('resources/texture/1.png'),
            2: self.get_texture('resources/texture/2.png'),
            3: self.get_texture('resources/texture/3.png'),
            4: self.get_texture('resources/texture/4.png'),
            5: self.get_texture('resources/texture/5.png')
        }
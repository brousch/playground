#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__version__ = '0.1'

from kivy.app import App
#from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image


class IconButton(ButtonBehavior, Image):
    pass


class Button_image(App):
    pass


class RootForm(BoxLayout):
    def quit(self):
        Button_image.get_running_app().stop()


if __name__ == "__main__":
#    Window.fullscreen = "auto"
    Button_image().run()
    
#!/usr/bin/env python2.7

import kivy
kivy.require('1.7.2')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class PasteTest(BoxLayout):
    pass


class PasteTestApp(App):
    def build(self):
        return PasteTest()


if __name__ == '__main__':
    PasteTestApp().run()

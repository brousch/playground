#!/usr/bin/env python2.7

import kivy
kivy.require('1.7.2')
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout

from plyer import notification

__version__ = '0.1'


class Playground(BoxLayout):

    def _do_notify(self,
                   title="Default Title",
                   message="This is the default message."):
        notification.notify(title, message)


class PlaygroundApp(App):
    def build(self):
        return Playground()


if __name__ == '__main__':
    PlaygroundApp().run()

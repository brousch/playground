#!/usr/bin/env python2.7

import random

import kivy
kivy.require('1.7.2')
from kivy.app import App
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout


class SlowTyper(BoxLayout):
    the_label = ObjectProperty(None)
    the_textbox = ObjectProperty(None)
    type_this = "Default"

    def _start_typing(self):
        Clock.unschedule(self._type_a_letter)
        self.the_label.text = ''
        self.string_pos = 0
        self.type_this = self.the_textbox.text
        self._type_a_letter(0.25)

    def _abort_typing(self):
        Clock.unschedule(self._type_a_letter)

    def _type_a_letter(self, dt):
        SoundLoader.load('9098__ddohler__typewriter.wav').play()
        self.the_label.text += self.type_this[self.string_pos]
        self.string_pos += 1
        if self.string_pos < len(self.type_this):
            Clock.schedule_once(self._type_a_letter,
                                random.uniform(0.25, 0.75))


class SlowTyperApp(App):
    def build(self):
        return SlowTyper()


if __name__ == '__main__':
    SlowTyperApp().run()

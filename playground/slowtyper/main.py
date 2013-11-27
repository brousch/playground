#!/usr/bin/env python2.7

import kivy
kivy.require('1.7.2')
from kivy.app import App
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout


class SlowTyper(BoxLayout):
    the_label = ObjectProperty(None)
    type_this = "Some long string to type."

    def __init__(self, **kwargs):
        super(SlowTyper, self).__init__(**kwargs)
        self.string_pos = 0
        Clock.schedule_once(self._type_a_letter, 0)

    def _type_a_letter(self, dt):
        self.the_label.text += self.type_this[self.string_pos]
        self.string_pos += 1
        if self.string_pos < len(self.type_this):
            Clock.schedule_once(self._type_a_letter, 0.5)


class SlowTyperApp(App):
    def build(self):
        return SlowTyper()


if __name__ == '__main__':
    SlowTyperApp().run()

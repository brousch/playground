# Clicking the Avatars button should print "I never get called"
# On Kivy 1.7.2 it prints "I always get called"
# On Kivy 1.8 it works correctly.

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.modalview import ModalView
from kivy.lang import Builder

kvs='''
BoxLayout:
    BoxLayout:
        id: menu
'''

class MPopup(ModalView):
    def __init__(self, **kwargs):
        super(MPopup, self).__init__(**kwargs)
        self.but = Button()
        self.pop = ModalView(size_hint=(None, None), size=(400, 400))
        self.but.bind(on_press=self.always_called)
        self.but.bind(on_press=self.pop.open)

    def always_called(self, some_arg):
        print "I always get called!"


root = Builder.load_string(kvs)


class MainApp(App): #Main function#
    def build(self):
        mava = MPopup()
        mbut = mava.but
        mbut.text='Avatars'
        mbut.bind(on_press=never_called)
        root.ids.menu.add_widget(mbut)
        return root

def never_called(some_arg):
    print "I never get called!"

if __name__ == '__main__':
    MainApp().run()

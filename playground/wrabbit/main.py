# File name: main.py
import kivy
kivy.require('1.7.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.widget import Widget

kv = Builder.load_file('main.kv')

class TopWidget(Widget):
    pass

class MiddleWidget(Widget):
    pass

class BottomWidget(Widget):
    pass

class MainScreenManager(ScreenManager):
    pass

class MainScreenManagerApp(App):
    def build(self):
        return MainScreenManager()

if __name__=="__main__":
    MainScreenManagerApp().run()

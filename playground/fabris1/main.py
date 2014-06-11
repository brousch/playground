# File name: main.py
from kivy.config import Config
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


class FloatLayoutApp(App):

    def build(self):
        return FloatLayout()


if __name__ == "__main__":
    
    FloatLayoutApp().run()
    
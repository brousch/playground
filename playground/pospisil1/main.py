from kivy.app import App
from kivy.uix.textinput import TextInput

__version__ = '0.1.0'

class MyApp(App):
    def build(self):
        return TextInput()

MyApp().run()

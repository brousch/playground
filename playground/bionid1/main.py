from kivy.app import App
from kivy.uix.button import Button
 
class TestApp(App):
    def build(self):
        b = Button()
        b.bind(on_press=self.stop)
        return b
 
TestApp().run()
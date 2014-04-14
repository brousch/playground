from kivy.interactive import InteractiveLauncher
from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        return Button(test='Hello Shell')

launcher = InteractiveLauncher(MyApp())
launcher.run()
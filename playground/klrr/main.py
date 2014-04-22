from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.properties import ObjectProperty
 
class RiderPlayer(Widget):
    pass
 
class RiderGame(Widget):
    lbl = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(RiderGame, self).__init__(**kwargs)
        Clock.schedule_interval(self.update, 2)
        pass
    def update(self, dt):
        self.lbl.text += "!"
 
class RiderApp(App):
    def build(self):
        return RiderGame()
 
if __name__ == '__main__':
    RiderApp().run()
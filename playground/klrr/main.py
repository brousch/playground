from kivy.app import App
from kivy.uix.widget import Widget
 
class RiderPlayer(Widget):
    pass
 
class RiderGame(Widget):
    pass
 
class RiderApp(App):
    def build(self):
        return RiderGame()
 
if __name__ == '__main__':
    RiderApp().run()
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout

class AnchorTest(AnchorLayout):
    pass

class AnchorTestApp(App):
    def build(self):
        return AnchorTest()

if __name__ == '__main__':
    AnchorTestApp().run()

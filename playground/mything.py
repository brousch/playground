from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout

class MyThing(AnchorLayout):
    pass

class MyThingApp(App):
    def build(self):
        return MyThing()

if __name__ == '__main__':
    MyThingApp().run()

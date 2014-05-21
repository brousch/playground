import kivy
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition
from kivy.uix.widget import Widget

class BigCircle(Widget):
    pass

class MainScreen(Screen):
    pass

class MyApp(App):
    def build(self):
        sm = ScreenManager(transition=NoTransition())
        sm.add_widget(MainScreen(name="Main"))
        return sm

if __name__ == '__main__':
    MyApp().run()
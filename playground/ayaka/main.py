import kivy
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
from kivy.app import App

class SensorWidgets(BoxLayout):
    def __init__(self,**kwargs):
        super(SensorWidgets, self).__init__(**kwargs)
class SensorMonitorApp(App):
    def build(self):
        return SensorWidgets()

if __name__ == '__main__':
    SensorMonitorApp().run()
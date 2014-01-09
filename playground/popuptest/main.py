import gc

from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
 
 
kv = """
#:kivy 1.4

<PopupTest>:
    id: bl
    orientation: "vertical"
    popup: popup.__self__
    canvas:
        Color:
            rgba: .18, .18, .18, .91
        Rectangle:
            size: self.size
            pos: self.pos
    Bubble:
        size_hint: (None, None)
        size: (150, 50)
        pos_hint: {'center_x': .5, 'y': .6}
        arrow_pos: 'bottom_mid'
        orientation: 'horizontal'
        BubbleButton:
            text: 'This is'
        BubbleButton:
            text: 'a'
        BubbleButton:
            text: 'Bubble'
    Button:
        text: 'press to show popup'
        on_release: root.popup.open()
    Popup:
        id: popup
        on_parent: if self.parent == bl: bl.remove_widget(self)
        title: "An example popup"
        content: popupcontent
        Button:
            id: popupcontent
            text: "press to dismiss"
            on_release: root.popup.dismiss()
"""
 
Builder.load_string(kv)
 
 
class PopupTest(BoxLayout):
    mypopup = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(PopupTest, self).__init__(**kwargs)
        Clock.schedule_interval(self.collect_garbage, 10)

    def collect_garbage(self, dt=0):
        print("Collecting garbage")
        gc.collect()

class PopupTestApp(App):
    def build(self):
        return PopupTest()
 
if __name__ == '__main__':
    PopupTestApp().run()

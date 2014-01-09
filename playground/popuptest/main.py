import gc

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
 
 
kv = """
<PopupTest>:
    Button:
        text: "Press me for a popup"
        on_press: root.make_popup()
    Button:
        text: "Press me to collect garbage"
        on_press: root.collect_garbage()
"""
 
Builder.load_string(kv)
 
 
class PopupTest(BoxLayout):
    def __init__(self, **kwargs):
        super(PopupTest, self).__init__(**kwargs)

    def make_popup(self):
        popup = Popup(title='Test popup',
                      content=Label(text='Now resize the window!'))
        popup.open()

    def collect_garbage(self):
        gc.collect()

class PopupTestApp(App):
    def build(self):
        return PopupTest()
 
if __name__ == '__main__':
    PopupTestApp().run()

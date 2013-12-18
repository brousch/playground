import kivy
import kivy
kivy.require("1.7.2")

from kivy.config import Config
Config.set('graphics', 'width', '540')
Config.set('graphics', 'height', '600')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.graphics import Rectangle

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

kv = '''
#:kivy 1.7.2
<RootWidget>:
    orientation: "vertical"
    padding: 10
    spacing: 15
    GridLayout:
        rows: 2
        size_hint: 1, .333
        Label:
            text: "App Name"
            color: 0, 0, 0, 1
        Label:
            text: "Some Info ..."
            color: 0, 0, 0, 1
    GridLayout:
        cols: 2
        spacing: 15
        Button:
            text: "1"
        Button:
            text: "2"
        Button:
            text: "3"
        Button:
            text: "4"
'''

Builder.load_string(kv)


class RootWidget(BoxLayout):
    pass


class MyApp(App):

    def build(self):
        # self.root = root = RootWidget(source = "snowy_mountains.jpg")
        self.root = root = RootWidget()
        root.bind(size=self._update_rect,
                  pos=self._update_rect)
        with root.canvas.before:
            self.rect = Rectangle(size=root.size,
                                pos=root.pos)

        return root

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


if __name__ == "__main__":
    app = MyApp()
    app.run()

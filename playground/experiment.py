from kivy.uix.modalview import ModalView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivy.app import App

class ExampleGridLayout(GridLayout):
    pass

class ExampleButton(RelativeLayout):
    text = StringProperty('')

class MainView(RelativeLayout):

    def __init__(self, **kwargs):
        self.size_hint = (.5, .3)
        self.pos_hint = {'center_x': .5, 'center_y': .5}
        super(MainView, self).__init__(**kwargs)

        button_container = ExampleGridLayout()
        self.add_widget(button_container)

class TestApp(App):

    def build(self):
        root = MainView()
        return root

Builder.load_string("""
<ExampleButton>:
    state_image: 'atlas://data/images/defaulttheme/button'
    canvas:
        Color:
            rgb: 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size
        BorderImage:
            source: self.state_image
            pos: self.pos
            size: self.size

    BoxLayout
        orientation: 'horizontal'
        #center_y: root.center_y
        pos_hint: {'center_x': .5, 'center_y': .5}
        size_hint: .75, .75
        Label:
            text: root.text
            shorten: True

<ExampleGridLayout>:
    cols: 1
    size_hint_y: None

    ExampleButton:
        text: "This Text should go INSIDE the button!"
    ExampleButton:
        text: "This gap between buttons shouldn't be here..."
""")

if __name__ == '__main__':
    TestApp().run()
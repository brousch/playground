from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


kv = """
<MainScreen>:
    orientation: 'vertical'
    Label:
        text: "User Name"
        size_hint: 1, None
        height: 80
    TextInput:
        id: username1
        multiline: False
        size_hint: 1, None
        height: 80
    Label:
        text: "Password"
        size_hint: 1, None
        height: 80
    TextInput:
        id: password1
        password: True
        multiline: False
        size_hint: 1, None
        height: 80
    BoxLayout:
        orientation: 'horizontal'
        Label:
            text: "User Name"
            size_hint: 1, None
        TextInput:
            id: username2
            multiline: False
            size_hint: 1, None
    BoxLayout:
        orientation: 'horizontal'
        Label:
            text: "Password"
            size_hint: 1, None
        TextInput:
            id: password2
            password: True
            multiline: False
            size_hint: 1, None
"""

Builder.load_string(kv)



class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)



class TestApp(App):
    def build(self):
        return MainScreen()


if __name__ == '__main__':
    TestApp().run()
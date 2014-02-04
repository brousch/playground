from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


kv = """
<Test>:
    orientation: 'horizontal' if root.width > root.height else 'vertical'
    Button:
        text: "Button1\\n{}x{}".format(self.width, self.height)
        size_hint: (None, 1) if root.width > root.height else (1, None)
    Button:
        text: "Button2\\n{}x{}".format(self.width, self.height)
        size_hint: (0.75, 1) if root.width > root.height else (1, 0.75)
"""

Builder.load_string(kv)


class Test(BoxLayout):
    def __init__(self, **kwargs):
        super(Test, self).__init__(**kwargs)


class TestApp(App):
    def build(self):
        return Test()

if __name__ == '__main__':
    TestApp().run()
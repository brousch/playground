from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout


kv = """
<Test>:
    canvas:
        Color:
            rgba: 1,1,1,1
        Rectangle:
            pos: self.pos
            size: self.size
    Button:
"""
 
Builder.load_string(kv)
 
 
class Test(GridLayout):
    def __init__(self, **kwargs):
        super(Test, self).__init__(**kwargs)
 
 
class TestApp(App):
    def build(self):
        return Test()
 
if __name__ == '__main__':
    TestApp().run()
from kivy.app import App
from kivy.atlas import Atlas
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
 
 
kv = """
<Test>:
    img: img
    Image:
        id: img
        source: None
"""
 
Builder.load_string(kv)
 
 
class Test(BoxLayout):
    def __init__(self, **kwargs):
        super(Test, self).__init__(**kwargs)
        Clock.schedule_interval(App.get_running_app().nxt, 1)
 
 
class TestApp(App):
    curimg = 1

    def build(self):
        return Test()

    def nxt(self, dt):
        print("showing {}".format(self.curimg))
        self.root.img.source = 'atlas://myatlas.atlas/{}'.format(self.curimg)
        self.curimg += 1
        if self.curimg >= 5:
            self.curimg = 1
 
if __name__ == '__main__':
    TestApp().run()

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

from jnius import autoclass


BuildVersion = autoclass('android.os.Build$VERSION')


kv = """
<Test>:
    BoxLayout:
        orientation: 'horizontal'
        Label:
            text: 'CODENAME'
        Label:
            text: {}
    BoxLayout:
        orientation: 'horizontal'
        Label:
            text: 'INCREMENTAL'
        Label:
            text: {}
    BoxLayout:
        orientation: 'horizontal'
        Label:
            text: 'RELEASE'
        Label:
            text: {}
    BoxLayout:
        orientation: 'horizontal'
        Label:
            text: 'SDK'
        Label:
            text: {}
    BoxLayout:
        orientation: 'horizontal'
        Label:
            text: 'SDK_INT'
        Label:
            text: {}
""".format(BuildVersion.CODENAME, BuildVersion.INCREMENTAL,
           BuildVersion.RELEASE, BuildVersion.SDK, BuildVersion.SDK_INT)

Builder.load_string(kv)
 
 
class Test(BoxLayout):
    def __init__(self, **kwargs):
        super(Test, self).__init__(**kwargs)
 
 
class TestApp(App):
    def build(self):
        return Test()
 
if __name__ == '__main__':
    TestApp().run()
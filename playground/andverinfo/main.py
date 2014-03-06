from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

from jnius import autoclass


BuildVersion = autoclass('android.os.Build$VERSION')


kv = """
<Test>:
"""

Builder.load_string(kv)
 
 
class Test(BoxLayout):
    def __init__(self, **kwargs):
        super(Test, self).__init__(**kwargs)
        self.add_widget(Label(text="CODENAME: {}".format(BuildVersion.CODENAME)))
        self.add_widget(Label(text="INCREMENTAL: {}".format(BuildVersion.INCREMENTAL)))
        self.add_widget(Label(text="RELEASE: {}".format(BuildVersion.RELEASE)))
        self.add_widget(Label(text="SDK: {}".format(BuildVersion.SDK)))
        self.add_widget(Label(text="SDK_INT: {}".format(BuildVersion.SDK_INT)))
 
 
class TestApp(App):
    def build(self):
        return Test()
 
if __name__ == '__main__':
    TestApp().run()
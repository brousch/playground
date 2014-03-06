from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.utils import platform


if platform == "android":
    from jnius import autoclass
    BuildVersion = autoclass('android.os.Build$VERSION')
else:
    class BV():
        def __init__(self, codename, incremental, release, sdk, sdk_int):
            self.CODENAME = codename
            self.INCREMENTAL = incremental
            self.RELEASE = release
            self.SDK = sdk
            self.SDK_INT = sdk_int
    BuildVersion = BV("Stub", "Wat", "Maybe", "Nope", 0)


kv = """
<Test>:
    orientation: 'vertical'
    Label:
        text: "Android Version Info"
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
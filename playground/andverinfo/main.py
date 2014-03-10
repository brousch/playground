from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.utils import platform


if platform == "android":
    from jnius import autoclass
    BuildVersion = autoclass('android.os.Build$VERSION')
    
    PythonActivity = autoclass('org.renpy.android.PythonActivity')
    Secure = autoclass('android.provider.Settings.Secure')
    ANDROID_ID = Secure.getString(PythonActivity.mActivity.getContentResolver(),
                                  Secure.ANDROID_ID)
else:
    class BV():
        def __init__(self, codename, incremental, release, sdk, sdk_int):
            self.CODENAME = codename
            self.INCREMENTAL = incremental
            self.RELEASE = release
            self.SDK = sdk
            self.SDK_INT = sdk_int
    BuildVersion = BV("Stub", "Wat", "Maybe", "Nope", 0)

    ANDROID_ID = "Fake ID"




kv = """
<Test>:
    orientation: 'vertical'
    Label:
        text: "Android Info"
"""

Builder.load_string(kv)


class Test(BoxLayout):
    def __init__(self, **kwargs):
        super(Test, self).__init__(**kwargs)
        self.append_widget("CODENAME", BuildVersion.CODENAME)
        self.append_widget("INCREMENTAL", BuildVersion.INCREMENTAL)
        self.append_widget("RELEASE", BuildVersion.RELEASE)
        self.append_widget("SDK", BuildVersion.SDK)
        self.append_widget("SDK_INT", BuildVersion.SDK_INT)
        self.append_widget("ANDROID_ID", ANDROID_ID)

    def append_widget(self, heading, text):
        self.add_widget(Label(text="{}: {}".format(heading, text)))

 
class TestApp(App):
    def build(self):
        return Test()
 
if __name__ == '__main__':
    TestApp().run()
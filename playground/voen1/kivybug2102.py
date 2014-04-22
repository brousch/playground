from kivy.app import App
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
 
try:
    from urllib.request import urlretrieve
except:
    from urllib import urlretrieve
 
urlretrieve("http://i.imgur.com/GJCLwBD.gif", "test_01.gif")
 
kv = """
<Test>:
    Image:
        source: 'test_01.gif'
        size: 320, 320
        size_hint: None, None
        anim_delay: 0.2
"""
 
Builder.load_string(kv)
 
 
class Test(AnchorLayout):
    pass
 
 
class TestApp(App):
    def build(self):
        return Test()
 
if __name__ == '__main__':
    TestApp().run()
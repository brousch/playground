from kivy.app import App
from kivy.lang import Builder


kv = """
AnchorLayout:
    AsyncImage:
        source: 'https://i.imgur.com/OS2E1.jpg'
        size_hint: None, None
        size: 500, 500
        anim_delay: 0.1
"""


class TestApp(App):
    def build(self):
        return Builder.load_string(kv)

if __name__ == '__main__':
    TestApp().run()
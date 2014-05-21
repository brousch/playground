import kivy
kivy.require('1.8.0')

from kivy.app import runTouchApp
from kivy.lang import Builder

kv = '''
#:kivy 1.8.0

AnchorLayout:
    canvas:
        Color:
            rgba: 1,1,1,1
        Rectangle:
            pos: self.pos
            size: self.size
    Image:
        size_hint: None, None
        size: '128dp', '128dp'
        source: 'resources/loading_icon.gif'  
'''

if __name__ == '__main__':
    runTouchApp(Builder.load_string(kv))
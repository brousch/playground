from kivy.app import App
from kivy.lang import Builder
 
kv = '''
Scatter:
    pos: 300, 300
    size: 400, 400
    TextInput:
        text: 'asdf !select me! asdf asdf'
        use_handles: True
        use_bubble: True
'''
 
 
class HandleApp(App):
    def build(self):
        return Builder.load_string(kv)
 
if __name__ == '__main__':
    HandleApp().run()
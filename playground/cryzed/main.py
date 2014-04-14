from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
 
 
kv = '''
<Test>:
    BoxLayout:
        orientation: 'vertical'
        size: root.size
 
        TextInput:
            id: text_input_1
            text: str(text_input_2.minimum_height)
            multiline: True
            size_hint_y: 1 if self.height <= 199 else None
            height: 200
 
        BoxLayout:
            orientation: 'horizontal'
            size_hint: 1, 0.05
 
            Button:
                id: button_1
                text: "Fetch"
                on_press: root.change_size()
            TextInput:
                id: text_input_2
                text: "URL"
'''

 
Builder.load_string(kv)
 
 
class Test(BoxLayout):
    def __init__(self, **kwargs):
        super(Test, self).__init__(**kwargs)
    def change_size(self):
        Window.height = 100
        Window.width = 100

class TestApp(App):
    def build(self):
        return Test()
 
if __name__ == '__main__':
    TestApp().run()


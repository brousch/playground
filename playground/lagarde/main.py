
from kivy.app import App
import kivy
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_string('''
<Main>
    MyToggleButton:
        on_press: self.ModInput()
        text: 'Normal: readonly = True         Down: readonly = False'
    MyTextInput:
        text:'Hello'
''')

class Main(BoxLayout):
    def __init__(self, **kwargs):
        super(Main, self).__init__(**kwargs)

class MyToggleButton(ToggleButton):
    def __init__(self, **kwargs):
        super(MyToggleButton, self).__init__(**kwargs)
    def ModInput(self):
        MyTextInput().ModInput2(self.state)
    
class MyTextInput(TextInput):
    def __init__(self, **kwargs):
        super(MyTextInput, self).__init__(**kwargs)
        readonly = True
    def ModInput2(self, state):
        if state == 'normal':
            self.readonly = True
            print(state)
            print (self.readonly)
        else:
            self.readonly = False
            print(state)
            print (self.readonly)

        
class myApp(App):
    def build(self):
        return Main()
if __name__ == '__main__':
    myApp().run()
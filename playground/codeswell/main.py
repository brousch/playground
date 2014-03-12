import kivy
kivy.require('1.8.0')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

# <need> The following is needed for .kv to be able to set properties
#     see https://groups.google.com/forum/#!topic/kivy-users/iQJERos4PNY
from kivy.properties import ObjectProperty, NumericProperty, StringProperty 
from kivy.uix.widget import Widget

class JLblTxtBtn(BoxLayout):
    # my_property = ObjectProperty(None)
    # some_other_property = NumericProperty(0)
    l_text = StringProperty('') 
    b_text = StringProperty('') 

kv = Builder.load_file('dynamic.kv')

class MyLayout(BoxLayout):
    pass


class MyApp(App):    
    def build(self):      
        return MyLayout()

MyApp().run() 
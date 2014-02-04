# If you click on Avatars it should crash.
import kivy
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.factory import Factory
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.modalview import ModalView
from kivy.lang import Builder
kvs='''
BoxLayout:
	BoxLayout:
		id: menu
		size_hint_y: 0.1
'''
class MPopup(ModalView):
	def __init__(self, **kwargs):
		super(MPopup, self).__init__(**kwargs)
		self.but = Button()
		def a(x=0):
			print self.but.text, 'pressed'
		self.pop = ModalView(size_hint=(None, None), size=(400, 400))
		self.but.bind(on_press=a)
		self.but.bind(on_press=self.pop.open)
root = Builder.load_string(kvs)	
def mavatar(a=0):
	hahaha()
def o(a=0):
	hahaha()
class MainApp(App): #Main function#
	def build(self):
 		
		
		mava = MPopup()
		mbut = mava.but
		mbut.text='Avatars'
		mbut.bind(on_press=mavatar)
		root.ids.menu.add_widget(mbut)
		filed = Button(text='text', border= (0,0,0,0), group = 'filelist')
		filed.bind(on_touch=o)
		root.ids.menu.add_widget(filed)
		return root
if __name__ == '__main__':
    MainApp().run()
    
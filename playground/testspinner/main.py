import sys

# add kivy paths
sys.path.append('/Applications/Kivy.app/Contents/Resources/kivy')
sys.path.append('/Applications/Kivy.app/Contents/Resources/lib')
sys.path.append('/Applications/Kivy.app/Contents/Resources/lib/sitepackages')


import kivy
from kivy.app import App
from kivy.uix.spinner import Spinner
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder

Builder.load_string('''
<SpinnerOption>:
#    halign: 'left'
    font_size: 12''')



class TestSpinnerApp(App):
	pass

if __name__ == '__main__':
	TestSpinnerApp().run()
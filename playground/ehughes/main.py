from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import Widget

 
class Test(Widget):
    def __init__(self, **kwargs):
        super(Test, self).__init__(**kwargs)
        self.start()
        
    def start(self):
        Clock.schedule_interval(self.callback, 0.5)
    
    def callback(self, dt):
        print('In callback')
 
 
class TestApp(App):
    def build(self):
        return Test()
 
if __name__ == '__main__':
    TestApp().run()

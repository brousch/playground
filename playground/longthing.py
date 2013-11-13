
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
 
i = 0
def print_on_widget(dt):
    global i
    for j in xrange(10):
        App.get_running_app().root.out.text += 'Next line %d\n' % i
        i += 1
class RootWidget(BoxLayout):
    out = ObjectProperty()
class TestApp(App):
    def build(self, **kwargs):
        root = RootWidget()
        Clock.schedule_interval(print_on_widget, 0.1)
        return root
if __name__ == '__main__':
    # Logger.setLevel('WARNING')
    TestApp().run()
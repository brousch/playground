from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ListProperty, ObjectProperty
 
 
kv = '''
#:import Animation kivy.animation.Animation
 
<BezierCord>:
    point: self.center
 
    canvas:
        Line:
            bezier:
                (
                self.center_x, self.y,
                self.point[0], self.point[1],
                self.center_x, self.top
                )
            width: 5
 
    on_touch_down:
        self.anim and self.anim.stop(self)
        self.anim = None
        self.point = args[1].pos
 
    on_touch_move:
        self.point = args[1].pos
 
    on_touch_up:
        self.anim = Animation(point=self.center, d=2, t='out_elastic')
        self.anim.start(self)
'''
 
 
class BezierCord(Widget):
    point = ListProperty([0, 0])
    anim = ObjectProperty(None, allownone=True)
 
 
class BCApp(App):
    def build(self):
        Builder.load_string(kv)
        return BezierCord()
 
 
if __name__ == '__main__':
    BCApp().run()
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.graphics import Rectangle
from kivy.core.image import Image as CoreImage
from kivy.core.window import Window


class MyWidget(Widget):
    def __init__(self, **kw):
        super(MyWidget, self).__init__(**kw)

        with self.canvas:
            texture = CoreImage('Sky_back_layer.png').texture
            texture.wrap = 'repeat'
            self.rect_1 = Rectangle(texture=texture, size=self.size, pos=self.pos)

            texture = CoreImage('Vegetation_(middle_layer).png').texture
            texture.wrap = 'repeat'
            self.rect_2 = Rectangle(texture=texture, size=self.size, pos=self.pos)

            texture = CoreImage('Ground_(front_layer).png').texture
            texture.wrap = 'repeat'
            self.rect_3 = Rectangle(texture=texture, size=self.size, pos=self.pos)

        Clock.schedule_interval(self.txupdate, 0)

    def txupdate(self, *l):
        t = Clock.get_boottime()
        #print t
        self.rect_1.tex_coords = -(t * 0.001), 0, -(t * 0.001 + 10), 0,  -(t * 0.001 + 10), -10, -(t * 0.001), -10
        self.rect_2.tex_coords = -(t * 0.01), 0, -(t * 0.01 + 1), 0,  -(t * 0.01 + 1), -1, -(t * 0.01), -1
        self.rect_3.tex_coords = -(t * 0.1), 0, -(t * 0.1 + 1), 0,  -(t * 0.1 + 1), -1, -(t * 0.1), -1


class MyApp(App):
    def build(self):
        return MyWidget(size=Window.size)


if __name__ == '__main__':
    MyApp().run()

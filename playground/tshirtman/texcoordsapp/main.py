from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, ListProperty
from kivy.core.image import Image as CoreImage

kv = '''
#:import chain itertools.chain
RootWidget:
    canvas:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: root.pos
            size: root.size
            texture: app.texture
            # here is our usage of the calculated texture coordinates
            # we devide by 100 because we took the input with a 100x100
            # rectangle as default value
            tex_coords: [x / 100. for x in chain(*root.points)]

        PushMatrix
        # translate the rectangle to make it easier to play with
        Translate:
            xy: root.width / 2, root.height / 2

        Color:
            rgba: 1, 0, 0, .5
        Line:
            points: chain(*root.points + root.points[:1])
            width: 2
        PopMatrix
'''


def dist(point, pos):
    return ((point[0] - pos[0]) ** 2 + (point[1] - pos[1]) ** 2)
    # ** .5 # who cares about square root here? it doesn't change the order


class RootWidget(Widget):
    # the default values, a 100x100 square, displayed around the middle of the screen
    points = ListProperty([[0, 0], [100, 0], [100, 100], [0, 100]])

    def on_touch_down(self, touch, *args):
        # compensate the translation done in canvas
        pos = touch.pos[0] - self.width / 2, touch.pos[1] - self.height / 2

        touch.ud['point'] = min(
            range(4), key=lambda x: dist(self.points[x], pos))

    def on_touch_move(self, touch, *args):
        # compensate the translation done in canvas
        pos = touch.pos[0] - self.width / 2, touch.pos[1] - self.height / 2
        # update the point
        self.points[touch.ud['point']] = pos


class TexCoordsApp(App):
    texture = ObjectProperty(None)

    def build(self):
        self.root = Builder.load_string(kv)
        self.texture = CoreImage.load(
            'GrassGreenTexture0002.jpg').texture
        self.texture.wrap = 'repeat'
        return self.root


if __name__ == '__main__':
    TexCoordsApp().run()
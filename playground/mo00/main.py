from kivy.app import App
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout


kv = '''
<FullImage>:
    canvas:
        Rectangle:
            texture: self.texture
            size: self.size
            pos: self.pos
'''
Builder.load_string(kv)


class FullImage(Image):
    def __init__(self, **kwargs):
        super(FullImage, self).__init__(**kwargs)
        self.source = "test.png"


class Test(BoxLayout):
    def __init__(self, **kwargs):
        super(Test, self).__init__(**kwargs)
        self.add_widget(FullImage())


class TestApp(App):
    def build(self):
        return Test()


if __name__ == '__main__':
    #Create the background image
    from PIL import Image, ImageDraw
    img = Image.new('RGBA', (100, 100))
    draw = ImageDraw.Draw(img)
    draw.ellipse((25, 25, 75, 75), outline=(255, 0, 0))
    img.save('test.png', 'PNG', transparency=0)

    TestApp().run()

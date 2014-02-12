from random import random
import pprint
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
from kivy.logger import Logger
from kivy.network.urlrequest import UrlRequest
 
class MyPaintWidget(Widget):
 
        def on_touch_down(self, touch):
                color = (random(), 1, 1)
                with self.canvas:
                        Color(*color, mode='hsv')
                        d = 30.
                        Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
                        touch.ud['line'] = Line(points=(touch.x, touch.y))
 
        def on_touch_move(self, touch):
                touch.ud['line'].points += [touch.x, touch.y]
 
class MyPaintApp(App):
 
        def build(self):
                parent = Widget()
                painter = MyPaintWidget()
                clearbtn = Button(text='Clear')
                parent.add_widget(painter)
                parent.add_widget(clearbtn)
 
                def success(req, result):
                        Logger.info(result)
 
                def failure(req, result):
                        Logger.info("Failed")
                        Logger.info(pprint.pformat(result))
 
                def clear_canvas(obj):
                        painter.canvas.clear()
                        Logger.info('Starting URL call.')
                        clearbtn.text = 'start!'
                        req = UrlRequest('https://api.twitter.com/1/trends/1.json', success, success, failure)
 
                clearbtn.bind(on_release=clear_canvas)
 
                return parent
 
if __name__ == '__main__':
        MyPaintApp().run()
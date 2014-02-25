from kivy.uix.label import Label
from kivy.app import App


class MyApp(App):
    def build(self):
        #Label()
        return Label(text='test')


if __name__ == '__main__':
    MyApp().run()


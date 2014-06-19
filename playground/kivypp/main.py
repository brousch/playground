from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import sp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.videoplayer import VideoPlayer


videos = ['C:/Users/ben/Downloads/2013-12-18 00.28.00.mp4',
          'C:/Users/ben/Downloads/2013-12-18 00.28.00.mp4',
          'C:/Users/ben/Downloads/2013-12-18 00.28.00.mp4',
          'C:/Users/ben/Downloads/2013-12-18 00.28.00.mp4',
          'C:/Users/ben/Downloads/2013-12-18 00.28.00.mp4',
          'C:/Users/ben/Downloads/2013-12-18 00.28.00.mp4', ]
 
class VidGrid(GridLayout):
    def __init__(self, **kwargs):
        super(VidGrid, self).__init__(**kwargs)
        self.cols = 3
        self.padding = (sp(10), sp(10))
        self.spacing = (sp(10), sp(10))
        for vid in videos:
            self.add_widget(VideoPlayer(source=vid, play=True))
 
 
class VidViewerApp(App):
    def build(self):
        return VidGrid()
 
if __name__ == '__main__':
    VidViewerApp().run()

# python file
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

########################################################################
class KVBoxLayout(BoxLayout):
    pass

class KVBoxLayoutApp(App):
    """"""

    #----------------------------------------------------------------------
    def build(self):
        """"""
        return KVBoxLayout()
        
#----------------------------------------------------------------------
if __name__ == "__main__":
    app = KVBoxLayoutApp()
    app.run()

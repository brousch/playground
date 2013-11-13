from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.app import App
#from scapy.all import *
from kivy.uix.floatlayout import FloatLayout
Builder.load_string('''
<NetTool>:
    button: button
    box: box
    s_range: s_range
    e_range: e_range
    size: 300, 300
    canvas:
        Rectangle:
            source: 'pyton.jpg'
            size: self.size
    TextInput:
        id: s_range
        text: "0"
        pos_hint: {'x': .27, 'y': .9}
        size_hint: (.05, .05)


    TextInput:
        id: e_range
        text: "254"
        pos_hint: {'x': .33, 'y': .9}
        size_hint: (.05, .05)

    Label:
        text: "Scan Network: 192.168.10."
        pos_hint: {'x': -.35, 'y': .42}
    BoxLayout:
        id: box
        orientation: 'vertical'
        spacing: -400
        #size_hint_x: 1
        #pos_hint: {'x': .3, 'y': .3}

    Button:
        id: button
        text: "Scan Now"
        size_hint: (.20, .10)
        pos_hint: {'x': .3, 'y': .05}
        on_release: root.do_action()
    Button:
        text: "Exit"
        size_hint: (.20, .10)
        pos_hint: {'x': .55, 'y': .05}

''')


class NetTool(FloatLayout):
    button = ObjectProperty()
    box = ObjectProperty()

    def do_action(self):
        self.s_range = ObjectProperty() ## text input
        self.e_range = ObjectProperty() ## text input  ## progress bar ## 
        for i in range(int(self.s_range.text), int(self.e_range.text)):
            IP = '192.168.0.' + str(i)
#            ARPREQUEST = Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=IP,hwdst='ff:ff:ff:ff:ff:ff')
#            ARPRESPONSE = srp1(ARPREQUEST,timeout=2,verbose=0)\
            ARPRESPONSE = True
            if ARPRESPONSE:
                self.box.add_widget(
                    Label(text='\nIP:' + ARPRESPONSE.psrc + '  ' + 'MAC:' + ARPRESPONSE.hwsrc))
        print 'Scan finished'


class NetApp(App):
    def build(self):
        return NetTool()


if __name__ == '__main__':
    NetApp().run()

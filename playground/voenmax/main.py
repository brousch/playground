from kivy.utils import platform
platform = platform()
 
if platform == 'win':
    import ctypes
 
    SPI_GETWORKAREA = 48
 
    class WorkArea(ctypes.Structure):
        _fields_ = [('left', ctypes.c_int), ('top', ctypes.c_int),
            ('right', ctypes.c_int), ('bottom', ctypes.c_int)]
 
    user32 = ctypes.windll.user32
    r = WorkArea()
    user32.SystemParametersInfoA(SPI_GETWORKAREA, 0, ctypes.byref(r), 0)
 
    app_pos_size = [r.left + 10, r.top + 32, r.right - r.left - 20,
        r.bottom - r.top - 42]
else:
    app_pos_size = [100, 100, 1024, 600]
 
from kivy.config import Config
Config.set('graphics', 'position', 'custom')
Config.set('graphics', 'left', app_pos_size[0])
Config.set('graphics', 'top', app_pos_size[1])
Config.set('graphics', 'width', app_pos_size[2])
Config.set('graphics', 'height', app_pos_size[3])
Config.set('kivy', 'desktop', 1)
Config.set('input', 'mouse', 'mouse,disable_multitouch')
 
from kivy.core.window import Window
 
if platform == 'win':
    from win32process import GetWindowThreadProcessId, GetCurrentProcessId
    from win32gui import ShowWindow, EnumWindows, GetWindowText
 
    SW_MAXIMIZE = 3
    app_proc_id = GetCurrentProcessId()
 
    def get_app_window(handle, _arg):
        global resized
        win_proc_id = GetWindowThreadProcessId(handle)
        if win_proc_id[1] == app_proc_id:
            title = GetWindowText(handle)
            if title == 'Kivy':
                ShowWindow(handle, SW_MAXIMIZE)
 
    EnumWindows(get_app_window, None)
 
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
 
kv = """
<Test>:
    Button:
"""
 
Builder.load_string(kv)
 
 
class Test(BoxLayout):
    pass
 
 
class TestApp(App):
    def build(self):
        return Test()
 
if __name__ == '__main__':
    TestApp().run()
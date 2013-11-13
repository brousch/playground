from kivy.app import App
from kivy.clock import Clock
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import StringProperty
from kivy.utils import platform
import os
from os.path import exists, join

platform = platform()
tmpfileindex = 0

class PictureImporterBase(RelativeLayout):

    raw_source = StringProperty()
    source = StringProperty()

    def __init__(self, **kwargs):
        self.tempfiles = []
        super(PictureImporterBase, self).__init__(**kwargs)
        Clock.schedule_once(self.init, -1)
        self.clear_tmpfiles()

    def clear_tmpfiles(self):
        tmpdir = self.get_temporary_dir()
        for fn in os.listdir(tmpdir):
            if fn.startswith('picture-importer-'):
                try:
                    os.unlink(join(tmpdir, fn))
                except:
                    pass

    def init(self, *args):
        self._display = self.ids.display.__self__
        self._selector = self.ids.selector.__self__
        self.remove_widget(self._display)

    def open_select(self):
        # XXX must be implemented
        pass

    def close_select(self):
        # XXX must be implemented
        pass

    def select(self, filename, is_temp=False):
        if not filename:
            return
        filename = filename[0]
        if not exists(filename):
            return
        if is_temp:
            dest = filename
            self.tempfiles.append(filename)
        else:
            dest = self.create_temporary_file()
        filename = self.convert(filename, dest)
        if not filename:
            return
        self.raw_source = self.source = filename
        self.remove_widget(self._selector)
        self.add_widget(self._display)
        self._display.source = filename
        self.close_select()

    def clear_selection(self):
        while self.tempfiles:
            try:
                os.unlink(self.tempfiles.pop())
            except:
                pass
        self.source = self.raw_source = ''
        self.remove_widget(self._display)
        self.add_widget(self._selector)

    def convert(self, src, dest):
        try:
            from PIL import Image
            isrc = Image.open(src)
            MAX = 1024
            w, h = isrc.size
            ratio = w / float(h)
            if w > h:
                if w > MAX:
                    w = 1024
                    h = int(w / ratio)
            else:
                if h > MAX:
                    h = 1024
                    w = int(h * ratio)

            if isrc.size == (w, h):
                return src

            idst = isrc.resize((w, h))
            idst.save(dest)

            if src != dest:
                self.tempfiles.append(dest)

            return dest

        except:
            import traceback
            traceback.print_exc()

    def create_temporary_file(self):
        global tmpfileindex
        tmpdir = self.get_temporary_dir()
        while True:
            fn = join(tmpdir, 'picture-importer-{}.jpg'.format(tmpfileindex))
            if not exists(fn):
                return fn
            tmpfileindex += 1

    def get_temporary_dir(self):
        return '.'



if platform == 'android':

    from kivy.properties import ObjectProperty
    from kivy.uix.popup import Popup
    from jnius import autoclass
    from android import activity

    Intent = autoclass('android.content.Intent')
    PythonActivity = autoclass('org.renpy.android.PythonActivity')
    Uri = autoclass('android.net.Uri')

    class CameraGalleryPopup(Popup):
        importer = ObjectProperty()

    class PictureImporter(PictureImporterBase):

        def open_select(self):
            self._popup = CameraGalleryPopup(importer=self)
            self._popup.open()

        def take_picture(self):
            self._popup.dismiss()

            from plyer import camera
            fn = self.create_temporary_file()
            print 'taking picture to', fn
            camera.take_picture(fn, self._on_picture_complete)

        def _on_picture_complete(self, fn):
            Clock.schedule_once(lambda *x: self.select([fn], True), 0)

        def choose_gallery(self):
            self._popup.dismiss()
            activity.bind(on_activity_result=self._on_activity_result)
            picker = Intent(Intent.ACTION_PICK)
            picker.setType('image/*')
            PythonActivity.mActivity.startActivityForResult(picker, 0x100)

        def _on_activity_result(self, request_code, result_code, intent):
            if request_code == 0x100:
                activity.unbind(on_activity_result=self._on_activity_result)
                if result_code != -1:
                    return
                uri = intent.getData()
                fn = self._convert_uri_to_filename(uri)
                Clock.schedule_once(lambda *x: self.select([fn]), 0)

        def _convert_uri_to_filename(self, uri):
            scheme = uri.getScheme()

            if scheme == 'content':
                cursor = PythonActivity.mActivity.getContentResolver().query(
                    uri, None, None, None, None)
                if cursor.moveToFirst():
                    index = cursor.getColumnIndexOrThrow('_data') #MediaStore.Images.Media.DATA
                    uri = Uri.parse(cursor.getString(index))
                    return uri.getPath()
            elif scheme == 'file':
                return uri.getPath()

            print 'Unknow filename/scheme', uri.getScheme(), uri.toString()
            return None

        def get_temporary_dir(self):
            d = '/sdcard/.pictureimporter'
            if not exists(d):
                os.makedirs(d)
            return d


else:
    from kivy.garden.filechooserthumbview import FileChooserThumbView
    from kivy.uix.popup import Popup

    class PictureImporter(PictureImporterBase):

        def open_select(self):
            content = FileChooserThumbView(
                    path=os.getcwd(),
                    filters=['*.png', '*.jpg', '*.jpeg'])
            content.bind(on_submit=lambda instance, selection, touch:
                    self.select(selection))
            self._popup = Popup(
                    content=content,
                    title='Importer une image',
                    size_hint=(.9, .9))
            self._popup.open()

        def close_select(self):
            if not self._popup:
                return
            self._popup.dismiss()
            self._popup = None


class PictureImporterApp(App):
    def build(self):
        root = PictureImporter()
        return root


if __name__ == '__main__':
    PictureImporterApp().run()

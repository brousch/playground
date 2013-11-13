from jnius import autoclass
from jnius import cast
from android import activity
from android.runnable import run_on_ui_thread

Toast = autoclass('android.widget.Toast')
context = autoclass('org.renpy.android.PythonActivity').mActivity

@run_on_ui_thread
def make_toast(text, length_long=False):
    if length_long:
        duration = Toast.LENGTH_LONG
    else:
        duration = Toast.LENGTH_SHORT
    JavaString = autoclass('java.lang.String')
    CharSequence = cast('java.lang.CharSequence', JavaString(text))
    toast = Toast.makeText(context, CharSequence, duration)
    toast.show()

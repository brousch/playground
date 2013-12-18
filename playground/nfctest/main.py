__version__ = '1.0'
 
from jnius import autoclass, cast
from android.runnable import run_on_ui_thread
from android import activity
from kivy.app import App
from kivy.lang import Builder
 
NfcAdapter = autoclass('android.nfc.NfcAdapter')
PythonActivity = autoclass('org.renpy.android.PythonActivity')
Intent = autoclass('android.content.Intent')
IntentFilter = autoclass('android.content.IntentFilter')
PendingIntent = autoclass('android.app.PendingIntent')
NdefRecord = autoclass('android.nfc.NdefRecord')
NdefMessage = autoclass('android.nfc.NdefMessage')
 
 
class NfcApp(App):
 
    def nfc_init(self):
        print 'nfc_init()'
 
        print 'configure nfc'
        self.j_context = context = PythonActivity.mActivity
        self.nfc_adapter = NfcAdapter.getDefaultAdapter(context)
        self.nfc_pending_intent = PendingIntent.getActivity(context, 0,
            Intent(context, context.getClass()).addFlags(
                Intent.FLAG_ACTIVITY_SINGLE_TOP), 0)
 
        print 'p2p filter'
        self.ndef_detected = IntentFilter(NfcAdapter.ACTION_NDEF_DISCOVERED)
        self.ndef_detected.addDataType('text/plain')
        self.ndef_exchange_filters = [self.ndef_detected]
 
    def on_new_intent(self, intent):
        print 'on_new_intent()', intent.getAction()
        if intent.getAction() != NfcAdapter.ACTION_NDEF_DISCOVERED:
            print 'unknow action, avoid.'
            return
 
        rawmsgs = intent.getParcelableArrayExtra(NfcAdapter.EXTRA_NDEF_MESSAGES)
        print 'raw messages', rawmsgs
        if not rawmsgs:
            return
 
        for message in rawmsgs:
            message = cast(NdefMessage, message)
            print 'got message', message
            payload = message.getRecords()[0].getPayload()
            print 'payload: {}'.format(''.join(map(chr, payload)))
 
    def nfc_disable(self):
        print 'nfc_disable()'
        activity.unbind(on_new_intent=self.on_new_intent)
 
    def nfc_enable(self):
        print 'nfc_enable()'
        activity.bind(on_new_intent=self.on_new_intent)
 
    @run_on_ui_thread
    def nfc_enable_ndef_exchange(self):
        print 'create record'
        ndef_record = NdefRecord(
                NdefRecord.TNF_MIME_MEDIA,
                'text/plain', '', 'hello world')
        print 'create message'
        ndef_message = NdefMessage([ndef_record])
 
        print 'enable ndef push'
        self.nfc_adapter.enableForegroundNdefPush(self.j_context, ndef_message)
 
        print 'enable dispatch', self.j_context, self.nfc_pending_intent
        self.nfc_adapter.enableForegroundDispatch(self.j_context,
                self.nfc_pending_intent, self.ndef_exchange_filters, [])
 
    @run_on_ui_thread
    def nfc_disable_ndef_exchange(self):
        self.nfc_adapter.disableForegroundNdefPush(self.j_context)
        self.nfc_adapter.disableForegroundDispatch(self.j_context)
 
    def on_pause(self):
        self.nfc_disable()
        return True
 
    def on_resume(self):
        self.nfc_enable()
 
    def build(self):
        self.nfc_init()
        return Builder.load_string('''
BoxLayout:
    Button:
        text: 'Enable NDEF exchange'
        on_press: app.nfc_enable_ndef_exchange()
    Button:
        text: 'Disable NDEF exchange'
        on_press: app.nfc_disable_ndef_exchange()
''')
 
NfcApp().run()
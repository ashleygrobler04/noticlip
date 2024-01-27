import time
import clipboard
import accessible_output2.outputs.auto
import observer
import subject

o = accessible_output2.outputs.auto.Auto()

# A simple global function to speak text


def speak(text):
    o.speak(text)


class ClipboardObserver(observer.Observer):
    def notify(self, event, updated_text):
        if event == "textChanged":
            speak(updated_text)


class Application:
    def __init__(self):
        # observe the clipboard to see if any text has changed.
        self.co = ClipboardObserver()
        # We need this to listen to the observer from the clipboard
        self.sub = subject.Subject()
        # add the clipboard observer to the subject.
        self.sub.addObserver(self.co)
        self.text = clipboard.paste()
        print("Monitoring clipboard for any changes...")

    def loop(self):
        current_clipboard_data = clipboard.paste()
        if isinstance(current_clipboard_data, str):
            if not self.text == current_clipboard_data:
                self.text = current_clipboard_data
                self.sub.notify("textChanged", self.text)


running = True
app = Application()
while running:
    time.sleep(0.05)
    try:
        app.loop()
    except Exception as err:
        pass

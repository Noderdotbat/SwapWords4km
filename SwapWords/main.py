import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.core.text import LabelBase
from kivy.config import Config
import getData

LabelBase.register(name="Arial", fn_regular="Arial.ttf")
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

class MainScreen(Widget):
    ttc = ObjectProperty(None)
    ct = ObjectProperty(None)

    def btn(self):
        self.ct.text = getData.HE_EN(text=self.ttc.text.lower())

    pass
class MyApp(App):
    def build(self):
        self.title = "SwapWords"
        return MainScreen()

if __name__ == "__main__":
    MyApp().run()

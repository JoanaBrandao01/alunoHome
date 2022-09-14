from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivymd.uix.button import MDFlatButton

class MainScream(FloatLayout):
    pass

class Seila(MDApp):
    def build(self):
        return MainScream()
Seila().run()
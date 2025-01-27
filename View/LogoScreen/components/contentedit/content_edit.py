from kivy.properties import StringProperty
from kivymd.uix.boxlayout import MDBoxLayout


class ContentEdit(MDBoxLayout):
    text_marka = StringProperty()
    text_model = StringProperty()
    hint_marka = StringProperty()
    hint_model = StringProperty()
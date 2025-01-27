from kivy.properties import StringProperty
from kivymd.uix.list import OneLineAvatarIconListItem


class ListItem(OneLineAvatarIconListItem):
    """n hbh"""
    text = StringProperty()

    def __init__(self, **kwargs):
        super(ListItem, self).__init__(**kwargs)




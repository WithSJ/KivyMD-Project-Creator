import utils
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase

utils.load_kv("tab_two.kv")


class TabTwo(FloatLayout, MDTabsBase):
    pass

from kivymd.uix.tab import MDTabs
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.tab import MDTabsBase

from kivy.uix.scrollview import ScrollView
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty, ListProperty
from kivymd.uix.list.list import OneLineListItem
from kivy.graphics import Rectangle
class Tab(MDFloatLayout, MDTabsBase):
    pass


class ContentNavigationDrawer(MDBoxLayout):
    pass


class InfoContent(ScrollView):
    pass


class MemberRow(BoxLayout):
    text = StringProperty()
    color = ListProperty()


class OweTextField(MDTextField):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hint_text = None if self.focus else self._hint_text

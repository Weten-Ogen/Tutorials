from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout


# The page layout
class MyPageLayout(PageLayout):
    pass

#The layout Page
class MyLayout(GridLayout):
    pass
class PageApp(App):
    def build(self):
        return MyPageLayout()


if __name__ == "__main__":
    PageApp().run()
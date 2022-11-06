from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button



# The layout Page
class MyLayout(GridLayout):
    pass

# The main App
class SiriApp(App):
    def build(self):
        return MyLayout()


if __name__ == "__main__":
    SiriApp().run()
from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.uix.button import Button


class MyWid(Widget):
    pass



class WidetsApp(App):
    def build(self):
        return MyWid()




if __name__ == "__main__":
    WidetsApp().run()
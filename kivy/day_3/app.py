from kivy.app import App 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Label

class Loggo(GridLayout):
    def __init__(self, **kwargs):
        super(Loggo, self).__init__(**kwargs)
        self.cols= 2
        self.add_widget(Label(text='Username')) 
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget = (Label(text='Password'))
        

class GesApp(App):
    def build(self):
        return Loggo()





if __name__ == "__main__":
    GesApp().run()

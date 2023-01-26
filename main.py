import kivy
from datetime import date
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.relativelayout import RelativeLayout

kivy.require('2.1.0') # replace with your current kivy version !

class MyRoot(RelativeLayout):

    def __init__(self):
            super(MyRoot, self).__init__()

    def countdown(self):
            present= date.today()
            future=date(2022, 10, 3)
            difference= str(future - present)[:5]
            self.days_left.text = difference+"days"
    
def callback(instance):
        print('The button <%s> is being pressed' % instance.text)
        btn1 = Button(text='Hello world 1')
        btn1.bind(on_press=callback)

class MyApp(App):
    def build (self):
        return MyRoot()



runapp = MyApp()
runapp.run()
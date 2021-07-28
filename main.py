from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
Window.clearcolor = (255/255, 150/255, 1/255, 1)
Window.size = (400, 200)


class CanApp(App):

    def __init__(self):
        super().__init__()
        self.Empty = Label(text="Заправить:")
        self.Remaining = Label(text="Остаток:")
        self.input_data = TextInput(hint_text='Введите объем бензина в баке в %', multiline=False)
        self.input_data.bind(text=self.on_text)

    def on_text(self, *args):
        V = 47
        data = self.input_data.text
        if data.isnumeric() and 0 <= float(data) <= 100:
            self.Empty.text = (f"Заправить {V - (float(data)*V)/100} литров")
            self.Remaining.text = (f"Осталось {(float(data) * V) / 100} литров")
        else:
            self.input_data.text = ''


    def build(self):
        box = BoxLayout(orientation = 'vertical')
        box.add_widget(self.input_data)
        box.add_widget(self.Empty)
        box.add_widget(self.Remaining)

        return box


if __name__ == "__main__":
    CanApp().run()

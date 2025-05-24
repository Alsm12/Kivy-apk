from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.name_input = TextInput(hint_text='Entrez votre nom')
        self.output_label = Label(text='')

        submit_button = Button(text='Valider')
        submit_button.bind(on_press=self.on_submit)

        layout.add_widget(self.name_input)
        layout.add_widget(submit_button)
        layout.add_widget(self.output_label)

        return layout

    def on_submit(self, instance):
        nom = self.name_input.text
        self.output_label.text = f"Bienvenue, {nom} !"

if __name__ == '__main__':
    MyApp().run()
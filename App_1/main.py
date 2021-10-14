from kivy.app import App
from kivy.uix.button import Button


class StartApp(App):
    def build(self):
        return Button(text="Python ist gigantisch")


if __name__ == "__main__":
    my_app = StartApp()
    my_app.run()

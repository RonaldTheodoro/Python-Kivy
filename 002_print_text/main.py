from kivy.app import App
from kivy.uix.label import Label


def build():
    label = Label()
    label.text = 'Hello World'
    label.italic = True
    label.font_size = 50
    return label


if __name__ == '__main__':
    root = App()

    root.build = build

    root.run()
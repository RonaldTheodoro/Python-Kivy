from kivy.app import App
from kivy.uix.label import Label


def build():
    return Label(text='Hello World')


if __name__ == '__main__':
    root = App()

    root.build = build

    root.run()
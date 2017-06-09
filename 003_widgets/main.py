from kivy.app import App
from kivy.uix.button import Button


def click():
    print('Hey listen')


def build():
    button = Button(text='Push me')
    button.on_press = click
    return button


if __name__ == '__main__':
    root = App()
    root.build = build
    root.run()

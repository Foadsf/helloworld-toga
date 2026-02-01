import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER

class HelloWorld(toga.App):
    def startup(self):
        # ERROR FIX: 'padding' is now 'margin'
        self.label = toga.Label(
            "Hello, World!",
            style=Pack(margin=20, text_align=CENTER)
        )

        button = toga.Button(
            "Click me",
            on_press=self.on_button_press,
            # ERROR FIX: 'padding' is now 'margin'
            style=Pack(margin=10)
        )

        # ERROR FIX: 'padding' is now 'margin'
        # ERROR FIX: 'alignment' is now 'align_items'
        box = toga.Box(
            children=[self.label, button],
            style=Pack(direction=COLUMN, align_items=CENTER, margin=20)
        )

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = box
        self.main_window.show()

    def on_button_press(self, widget):
        self.label.text = "Button was clicked!"

def main():
    return HelloWorld("Hello World", "org.example.helloworld")

if __name__ == "__main__":
    main().main_loop()

from kivy.app import App
from kivy.lang import Builder

class BoxLayoutDemo(App):
    """Main application class for the Box Layout Demo app."""
    def build(self):
        """Build the Kivy GUI."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Update greeting label when Greet button is pressed."""
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """Clear the name input and greeting label."""
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = ''

BoxLayoutDemo().run()

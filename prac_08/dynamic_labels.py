from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    """Main application class that builds a Kivy GUI with dynamic labels."""
    def build(self)
        """Create label widgets from a list of names and add them to the GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create label widgets from a list of names and add them to the GUI."""
        list_of_names = ["Alice", "Bob", "Charlie", "David"]
        for name in list_of_names:
            # create a label for each name
            temp_label = Label(text=name)
            # add the label to the "main" BoxLayout widget
            self.root.ids.main.add_widget(temp_label)

if __name__ == '__main__':
    DynamicLabelsApp().run()

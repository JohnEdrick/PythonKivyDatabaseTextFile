import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty


class Root(FloatLayout):
    name = ObjectProperty(None)
    email = ObjectProperty(None)

    def press(self):
        name = self.name.text
        email = self.email.text
        with open("contact.txt", mode="a") as myfile:
            myfile.writelines(f"{name},{email}\n")
            print("Name: ", name, "\nEmail: ", email,"\nADDED!")

        self.name.text = ""
        self.email.text = ""


class MyApp(App):
    title = "Record"

    def build(self):
        return Root()


if __name__ == "__main__":
    MyApp().run()

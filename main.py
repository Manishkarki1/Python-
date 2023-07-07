from kivymd.apk import MDApp
from kivymd.uix.label import MDLabel

class Main_App(MDApp):
    def build(self):
        return MBLabel(text="Welcome to LearntoTeach",halign="center")
if __name__=="__main__":
    Main_App().run()
    
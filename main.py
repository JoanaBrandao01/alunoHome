from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivy.lang import Builder

class Home(MDApp):
    Window.size=(540,960)

    def build(self):
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(
            '''
MDScreen:
    

    MDBottomNavigation:
        panel_color: "#000000"
        text_color_active: "lightgrey"
        

        MDBottomNavigationItem:
            name: 'screen 1'
            icon: 'compass'
            Image:
                source:'imgm.jpg'
                allow_stretch:True
            MDLabel:
                
                BoxLayout:
                    orientation: 'horizontal'
                    
                    Label:
                        text: 'Rota1'
                        size_hint_x: None
                        size: self.texture_size
                        pos_hint: {'right': 1}

        MDBottomNavigationItem:
            name: 'screen 2'
            icon: 'bus'

        MDBottomNavigationItem:
            name: 'screen 3'
            icon: 'bell'

            MDLabel:
                text: 'notificações, mudanças ou algo relacionado a rota'
                halign: 'center'
        MDBottomNavigationItem:
            name: 'screen 4'
            icon: 'cog'

            MDLabel:
                text: 'aqui colocaremos as configurações do app para alunos'
                halign: 'center'
'''
        )


Home().run()
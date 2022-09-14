import secrets
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import Screen
from kivy.core.window import Window
from kivy.properties import StringProperty, ObjectProperty

class Gerenciador(ScreenManager):
    pass

class JanelaPrincipal(Screen):
    pass

class LoginAluno(Screen):
    
    def login(self):
        if self.ids.email.text == "" and self.ids.senha.text == "":
            self.manager.current = "telaprincipalaluno"

class ErroUsuario(Screen):
    pass

class ErroSenha(Screen):
    pass

class RedefinirSenha(Screen):
    pass

class Cadastrar(Screen):
    pass

class ConcluirCadastro(Screen):
    pass

class MainScreenAluno(Screen):
     def switch(self):
        self.parent.current = 'screen 1'


class UABusJ(MDApp):
      def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Blue'
        self.theme_cls.primary_hue = '700'
        gerenciador = Gerenciador()
        return gerenciador
aplicativo = UABusJ()
Window.size = (540,960)
aplicativo.run()
# Um programa com interface gráfica
# Armazenar o site/software para o qual a senha será gerada
# Armazenar o usuário e email
# Possibilitar configurar o tamanho da senha

import random
import PySimpleGUI as sg
import os

# Layout do programa


class PassGen:
    def __init__(self):
        # Layout
        sg.theme('Black')
        layout = [
            [sg.Text('Site/Software:', size=(11, 1)),
             sg.Input(key='site', size=(23, 1))],
            [sg.Text('E-mail/Usuário:', size=(11, 1)),
             sg.Input(key='usuário', size=(23, 1))],
            [sg.Text('Quantidade de caracteres'), sg.Combo(values=list(
                range(6, 17)), key='total_chars', default_value=10, size=(3, 1))],
            [sg.Output(size=(36, 5))],
            [sg.Button('Gerar Senha')],
            [sg.Button('Salvar')],
            [sg.Button('Limpar')],
            [sg.Button('Sair')],
        ]
        # Declarar a Janela
        self.janela = sg.Window('Gerador de Senha 2023', layout)

        # Event Loop
    def Iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                break
            if evento == 'Gerar Senha':
                nova_senha = self.gerar_senha(valores)
                print(nova_senha)
            if evento == 'Sair':
                break

    def gerar_senha(self, valores):
        char_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijk1lmnopgrstuvwxyz1234567890!@#$%&*"
        chars = random.choices(char_list, k=int(valores['total_chars']))
        new_pass = ''.join(chars)
        return new_pass

    def salvar_senha(self, nova_senha, valores):
        with open('senhas.txt', 'a', newline='') as arquivo:
            arquivo.write(
                f"Site: {valores[site]}, Usuário: {valores['usuario']}, Nova Senha: {nova_senha}")
            print("Senha salva para o arquivo 'Senhas.txt'")


gen = PassGen()
gen.Iniciar()

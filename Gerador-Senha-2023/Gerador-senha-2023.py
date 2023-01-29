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
             sg.Input(key='site', size=(23, 1), expand_x=True)],
            [sg.Text('E-mail/Usuário:', size=(11, 1)),
             sg.Input(key='usuario', size=(23, 1), expand_x=True)],
            [sg.Text('Quantidade de caracteres:'), sg.Combo(values=list(
                range(6, 17)), key='total_chars', default_value=10, size=(3, 1), expand_x=True)],
            [sg.Output(key='textbox', size=(36, 6),
                       expand_x=True, expand_y=True)],
            [sg.Button('Gerar Senha', expand_x=True),
             sg.Button('Limpar', expand_x=True)],
            [sg.Button('Salvar', expand_x=True), sg.Button(
                'Remover Senhas', expand_x=True)],
            [sg.Button('Sair', expand_x=True)]
        ]
        # Declarar a Janela
        self.janela = sg.Window('Gerador de Senha 2023', layout)

        # Event Loop
    def Iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WIN_CLOSED or evento == 'Sair':
                break
            if evento == 'Gerar Senha':
                nova_senha = self.gerar_senha(valores)
                print(
                    f"Site/Software: {valores['site']}\nUsuário: {valores['usuario']}\nSenha: {nova_senha}\n")
            if evento == 'Salvar':
                self.salvar_senha(nova_senha, valores)
            if evento == 'Limpar':
                self.limpar_entradas(valores)
            if evento == 'Remover Senhas':
                self.remover_senha()

    def gerar_senha(self, valores):
        char_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijk1lmnopgrstuvwxyz1234567890!@#$%&*"
        chars = random.choices(char_list, k=int(valores['total_chars']))
        new_pass = ''.join(chars)
        return new_pass

    def salvar_senha(self, nova_senha, valores):
        with open('Senhas.txt', 'a') as file:
            file.write(
                f"Site/Software: {valores['site']}\nUsuário: {valores['usuario']}\nSenha: {nova_senha}\n\n")
        print("Senha salva no arquivo 'Senhas.txt'")

    def limpar_entradas(self, valores):
        for key in valores:
            self.janela[key].update('')
            self.janela['textbox'].update('')
        return None

    def remover_senha(self):
        with open('Senhas.txt', 'w') as file:
            file.write("")
            print("Todas as senhas removida com sucesso do arquivo 'Senha.txt'")


gen = PassGen()
gen.Iniciar()

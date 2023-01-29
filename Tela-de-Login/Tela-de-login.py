from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme = ('Reddit')
layout = [
    [sg.Text('Usuário:'), sg.Input(key='usuario', expand_x=True)],
    [sg.Text('Senha:'), sg.Input(
        key='senha', password_char='*', expand_x=True)],
    [sg.Checkbox('Salvar o Login?')],
    [sg.Button('Entrar'), sg.Button('Sair')]
]

# Janela
window = sg.Window('Tela de Login', layout)

# Ler os eventos
while True:
    eventos, valores = window.read()
    if eventos == sg.WIN_CLOSED or eventos == 'Sair':
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'Lucas' and valores['senha'] == '123':
            sg.Popup('Bem vindo!!!')
        else:
            sg.Popup('Digite a senha correta')

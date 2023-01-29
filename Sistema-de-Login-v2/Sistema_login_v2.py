from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme = ('Reddit')
layout = [
    [sg.Text('Usuário:')],
    [sg.Input(key='usuario', expand_x=True)],
    [sg.Text('Senha:')],
    [sg.Input(key='senha', password_char='*', expand_x=True)],
    [sg.Text('', key='mensagem')],
    [sg.Button('Login'), sg.Button('Sair')]
]

# Janela
window = sg.Window('Login v2', layout=layout)

# Ler os eventos
while True:
    eventos, valores = window.read()
    print(valores)
    if eventos == sg.WIN_CLOSED or eventos == 'Sair':
        break
    elif eventos == 'Login':
        senha_correta = '123'
        usuario_correto = 'Lucas'
        usuario = valores['usuario']
        senha = valores['senha']
        if usuario == usuario_correto and senha == senha_correta:
            window['mensagem'].update('Login realizado com sucesso!')
        else:
            window['mensagem'].update('Usuário ou senha inválida!')
window.close ()
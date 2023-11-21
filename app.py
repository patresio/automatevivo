from threading import Thread

import PySimpleGUI as sg

from bot_vivo import bot_vivo


def principal_window():
    sg.theme('Reddit')
    layout = [
        [sg.Text('\U0001F916 Bem vindo(a), eu sou o ROBO AUTOMATEVIVO',
                 text_color='black', font='helvetica 12')],
        [sg.Text('Escolha a automação:', text_color='black', font='helvetica 10')],
        [sg.Text()],
        [sg.Button('Automação Download Faturas VIVO', key='automate_vivo'),],
        [sg.Text('')],
        [sg.Button('Sair', size=10)]
    ]
    window_size = (400, 200)
    window = sg.Window('\U0001F916 ROBO AUTOMATEVIVO',
                       layout, size=window_size)
    while True:
        event, values = window.read()
        if event == 'Sair' or event == sg.WIN_CLOSED:
            break
        if event == 'automate_vivo':
            window.close()
            window_bot_vivo()

    window.close()


def window_bot_vivo():
    sg.theme('Reddit')
    layout = [
        [sg.Text('\U0001F916 Bora começar!!!!!')],
        [sg.Text('\U0001F916 Sou melhor que qualquer estagiário!!!')],
        [sg.Text('')],
        [sg.Button('Iniciar', key='botao_iniciar', size=(20, 1)), sg.Combo(['Firefox', 'Chrome'], default_value='Firefox', readonly=True, key='navegador'),
         sg.Button('Voltar', key='botao_voltar', size=(20, 1))],
        [sg.Output(size=(400, 200))],
    ]

    window_size = (800, 800)

    window = sg.Window(
        '\U0001F916 Download das Faturas da VIVO', layout, size=window_size)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'botao_voltar':
            window.close()
            principal_window()
        elif event == 'botao_iniciar':
            browser = values['navegador']
            thread = Thread(target=bot_vivo(browser), daemon=True)
            thread.start()

            window['botao_iniciar'].update(disabled=False)
            window['botao_voltar'].update(disabled=True)


if __name__ == '__main__':
    principal_window()

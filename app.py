from threading import Thread

import PySimpleGUI as sg

from bot.bot_vivo import bot_vivo


def principal_window():  # sourcery skip: merge-comparisons
    sg.theme('Reddit')
    layout = [
        [sg.Text('\U0001F916 Bem vindo(a), eu sou o ROBO AUTOMATEVIVO',
                 text_color='black', font='helvetica 12')],
        [sg.Text('Escolha a automação:', text_color='black', font='helvetica 10')],
        [sg.Text()],
        [sg.Button('Automação Download Faturas VIVO no FIREFOX',
                   key='automate_vivo_firefox'),],
        [sg.Button('Automação Download Faturas VIVO no CHROME',
                   key='automate_vivo_chrome'),],
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
        elif event == 'automate_vivo_firefox':
            window.close()
            window_bot_vivo_firefox()
        elif event == 'automate_vivo_chrome':
            window.close()
            window_bot_vivo_chrome()

    window.close()


def window_bot_vivo_chrome():
    sg.theme('Reddit')
    layout = [
        [sg.Text('\U0001F916 Bora começar!!!!!')],
        [sg.Text('\U0001F916 Sou melhor que qualquer estagiário!!!')],
        [sg.Text('\U0001F916 Abrirá o navegador CHROME, certifique de ter instalado!!!')],
        [sg.Text('')],
        [sg.Button('Iniciar', key='botao_iniciar_chrome', size=(20, 1)),
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
        elif event == 'botao_iniciar_chrome':
            browser = 'Chrome'
            thread = Thread(target=bot_vivo(browser), daemon=True)
            thread.start()

            window['botao_iniciar'].update(disabled=False)
            window['botao_voltar'].update(disabled=True)


def window_bot_vivo_firefox():
    sg.theme('Reddit')
    layout = [
        [sg.Text('\U0001F916 Bora começar!!!!!')],
        [sg.Text('\U0001F916 Sou melhor que qualquer estagiário!!!')],
        [sg.Text('\U0001F916 Abrirá o navegador FIREFOX, certifique de ter instalado!!!')],
        [sg.Text('')],
        [sg.Button('Iniciar', key='botao_iniciar_firefox', size=(20, 1)),
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
        elif event == 'botao_iniciar_firefox':
            browser = 'Firefox'
            thread = Thread(target=bot_vivo(browser), daemon=True)
            thread.start()

            window['botao_iniciar'].update(disabled=False)
            window['botao_voltar'].update(disabled=True)


if __name__ == '__main__':
    principal_window()

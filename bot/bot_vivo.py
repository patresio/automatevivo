from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions

from utils.functions import *


def bot_vivo(browser):
    print(browser)
    print(Fore.BLUE, '\U0001F916',
          'OLÁ EU SOU O ROBÔ DO AUTOMATEVIVO VAMOS COMEÇAR EM INSTANTES', '\U000023F3')
    print('\U0001F5A5', 'Confira se o computador esta com a',
          '\U0001F50B', 'cheia. E conectado a', '\U0001F50C')
    print('Vou utilizar seus componentes: ', '\U00002328', '\U0001F5B1')
    create_folder_download()
    create_folder_faturas()
    download_folder = config_download_folder()
    local_folder = config_initial_local_folder()
    site_map, site_link, user_data = config_initial_data()

    driver, wait = initial_drivers(browser=browser)
    print(Fore.CYAN, '\U0001F916',
          'ROBO DIZ: Vou entrar no site e tentar fazer o login ....', '\U0001F412')
    driver.get(site_link)
    wait.until(
        expected_conditions.presence_of_element_located(
            (By.XPATH, site_map['input']['email']['xpath']))
    ).send_keys(user_data['email'], Keys.ENTER)
    random_wait()
    wait.until(
        expected_conditions.presence_of_element_located(
            (By.XPATH, site_map['input']['password']['xpath']))
    ).send_keys(user_data['password'], Keys.ENTER)
    print(Fore.WHITE, '\U0001F916',
          'ROBO DIZ: Estamos com sorte o login foi efetuado com sucesso', '\U0001F310')
    random_wait(20, 35)
    wait.until(expected_conditions.presence_of_element_located(
        (By.XPATH, site_map['link']['linkVivoMovel']['xpath']))).click()
    random_wait(2, 5)
    wait.until(expected_conditions.presence_of_element_located(
        (By.XPATH, site_map['link']['linkSolucoesCorporativa']['xpath']))).click()
    random_wait(15, 20)
    print('\U0001F916', 'ROBO DIZ: Se chegou até aqui vamos ver se trocamos de aba meu pequeno gafanhoto', '\U000131A7')
    nova_aba = driver.window_handles[1]
    driver.switch_to.window(nova_aba)
    print(Fore.WHITE, '\U0001F916', 'ROBO DIZ: Calma Mussarello', '\U0001F9C0', '\n', '\U0001F51C', driver.title,
          'Conseguimos ir para a aba filho!!!!')
    random_wait()
    wait.until(expected_conditions.presence_of_element_located(
        (By.XPATH, site_map['button']['buttonComboBox']['xpath']))).click()

    #### Listando os Telefones #####
    print('Aqui passou!!!')
    element_numbers_phones = wait.until(expected_conditions.presence_of_all_elements_located(
        (By.XPATH, site_map['telefones']['listPhoneNumbers']['xpath'])))
    print(Fore.GREEN, '\U0001F916', 'O ROBO DIZ: UAUUUUUUUU Você tem',
          len(element_numbers_phones), '\U0000260E', 'faturas para fazer Downloads!!!')

    #### Clicando em cada telefone ####
    list_number_phone = [
        number_phone.text for number_phone in element_numbers_phones]
    csv_phone = []
    data_phone = []
    for phone in list_number_phone:
        fatura_download = f'{
            download_folder}/fatura_{mes_texto}{ano_atual}.pdf'
        fatura_rename = f'{download_folder}/{phone}.pdf'
        fatura_local_folder = f'{local_folder}/Faturas-{mes_txt}/{phone}.pdf'
        # Ajuste para erro!!!
        if os.path.isfile(fatura_local_folder):
            xpath = f"//span[@data-value='{phone}']"
            random_wait(30, 40)
            print(Fore.WHITE, '-'*43)
            print(Fore.GREEN, '\U0001F916',
                  f'O ROBO clica no telefone {phone}')
            print(Fore.WHITE, '-'*43)
            wait.until(expected_conditions.element_to_be_clickable(
                (By.XPATH, xpath))).click()
            random_wait(30, 40)
            try:
                mes_vigencia = driver.find_element(
                    By.XPATH, site_map['tabela']['mesVigencia']['xpath'])
                status_pagamento = driver.find_element(
                    By.XPATH, site_map['tabela']['statusPagamento']['xpath'])
                valor_pagemento = driver.find_element(
                    By.XPATH, site_map['tabela']['valorPagamento']['xpath'])
                data_phone.append(
                    [phone, status_pagamento.text, valor_pagemento.text])
            except NoSuchElementException:
                random_wait(30, 50)
                driver.refresh()
                random_wait(30, 50)
        else:
            xpath = f"//span[@data-value='{phone}']"
            random_wait(30, 40)
            print(Fore.WHITE, '-'*43)
            print(Fore.GREEN, '\U0001F916',
                  f'O ROBO clica no telefone {phone}')
            print(Fore.WHITE, '-'*43)
            wait.until(expected_conditions.element_to_be_clickable(
                (By.XPATH, xpath))).click()
            random_wait(30, 40)
            try:
                mes_vigencia = driver.find_element(
                    By.XPATH, site_map['tabela']['mesVigencia']['xpath'])
                status_pagamento = driver.find_element(
                    By.XPATH, site_map['tabela']['statusPagamento']['xpath'])
                valor_pagemento = driver.find_element(
                    By.XPATH, site_map['tabela']['valorPagamento']['xpath'])
                data_phone.append(
                    [phone, status_pagamento.text, valor_pagemento.text])
                txt_pronto = f'O ROBO  abriu com êxito a linha: {phone}. Sendo a fatura em vigor {
                    mes_vigencia.text}. Com status {status_pagamento.text} |'
                print(Fore.CYAN, '-'*109)
                print(Fore.CYAN, '|', '\U0001F916', txt_pronto)
                print(Fore.CYAN, '-'*109)
                if status_pagamento.text == "Pendente":
                    wait.until(expected_conditions.element_to_be_clickable(
                        (By.XPATH, site_map['img']['download']['xpath']))).click()
                    random_wait()
                    wait.until(expected_conditions.element_to_be_clickable(
                        (By.XPATH, site_map['link']['downloadPDF']['xpath']))).click()
                    random_wait(30, 40)
                    '''
                                Tratamento do arquivo da fatura baixado
                                e variaveis utilizadas
                    '''

                    rename_arquivo(fatura_local_folder,
                                   fatura_download, fatura_rename, phone)
            except NoSuchElementException:
                print(
                    Fore.RED, '\U0001F916', f'O ROBO não achou nada para download do telefone {phone}')
                data_phone.append([phone, None, None])
        # Ultimo passo do FOR
        random_wait()
        wait.until(expected_conditions.presence_of_element_located(
            (By.XPATH, site_map['button']['buttonComboBox']['xpath']))).click()
    filename_csv = f'Faturas-{mes_txt}/Relatório-{mes_txt}.csv'
    header_csv = ['Número Telefone',
                  'Status do Pagamento', 'Valor do Pagamento']
    create_csv(header_csv, data_phone, filename_csv)

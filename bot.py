import webbrowser
from urllib.parse import quote
import pyautogui
from time import sleep


nome = 'Márcia'
telefone = '5511966545221'

mensagem = f'Olá {nome}, estou fazendo um bot de whatsapp pelo python, esta mensagem é automatica'

link_mensagem = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}'

webbrowser.open(link_mensagem)
sleep(30)
pyautogui.keyDown('enter')
sleep(5)
pyautogui.hotkey('ctrl', 'w')

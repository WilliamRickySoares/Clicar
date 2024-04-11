import pyautogui
import time
import keyboard
  

print("Iniciando...")
time.sleep(2)

# Defina as coordenadas x e y para o local de clique
posicao_x = 310 
posicao_y = 283

# Defina o número de pixels para mover o cursor
movimento_x = 0
movimento_y = -50

# Defina o intervalo de tempo entre os cliques
intervalo_entre_cliques = 5

try:
    while True:
        print("Começou!")
        
        # Mova o cursor para a posição desejada
        pyautogui.moveTo(posicao_x, posicao_y, duration=0.5)
        print("Cursor movido para a posição:", posicao_x, posicao_y)
        print("Vai clicar")
        pyautogui.click()
        print("Clicou na tela!")
        time.sleep(0.5)
        
        # Mova o cursor alguns pixels
        pyautogui.moveRel(movimento_x, movimento_y, duration=0.5)
        print("Cursor movido por", movimento_x, movimento_y, "pixels")

        # Clique na posição atual do cursor
        print("Vai clicar")
        pyautogui.click()
        print("Clicou na tela!")
        time.sleep(0.5)
        pyautogui.press('space')

        # Aguarde o intervalo especificado
        time.sleep(intervalo_entre_cliques)
        
        if keyboard.is_pressed('esc'):
            break
except KeyboardInterrupt:
    print("\nAutomação encerrada pelo usuário.")

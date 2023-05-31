from modulos import time,pyautogui,numpy

def deley (seconds):
    time.sleep(0)
    
    
#def vita():
    #vita_cheia = 1500
    #vitalidade = 50
    
    #if vita_cheia >= 1480:
       # print('Vitalidade está cheia')
        #pyautogui.press('b')
    #elif vita_cheia <= 30:
        #bag = pyautogui.locateOnScreen('bag.png', confidence= 0.7)
        #pyautogui.click (bag.x,bag.y)
        #deley(3)
        #itens = pyautogui.locateOnScreen('itens.png', confidence=0.7)
        #pyautogui.click (itens.x, itens.y)
        #deley(2)
        #vitalidade = pyautogui.locateOnScreen('vitalidade.png', confidence=0.7)
        #for in range (14):
            #pyautogui.doubleClick(vitalidade.x, vitalidade.y)


def trial_5():
    selecao = pyautogui.locateOnScreen('selecao.png', confidence=0.7)
    pyautogui.click(selecao.x, selecao.y)
    deley(1)
    instancia = pyautogui.locateOnScreen('instancia.png', confidence=0.7)
    pyautogui.click(instancia.x, instancia.y)
    deley(1)
    trial_5 = pyautogui.locateOnScreen('trial_5.png', confidence= 0.7)
    pyautogui.click(trial_5.x, trial_5.y)
    deley(1)
    dificuldade = pyautogui.locateOnScreen('dificuldade.png', confidence=0.7)
    pyautogui.click(dificuldade.x, dificuldade.y)
    deley(2)
    sim = pyautogui.locateOnScreen('sim.png', confidence=0.7)
    pyautogui.click(sim.x, sim.y)
    deley(2)
    inicio = pyautogui.locateOnScreen('inicio.png', confidence=0.7)
    pyautogui.click(inicio.x, inicio.y)
    deley (5)
    
            
            
        
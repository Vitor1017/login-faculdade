import pyautogui                    
import subprocess
import time

url_site = "https://www.colaboraread.com.br/login/auth" 

# Abrir o Chrome diretamente com a URL desejada

subprocess.run(r"C:\Program Files\Google\Chrome\Application\chrome.exe")

time.sleep(2)  # Espera o navegador abrir e a página carregar
pyautogui.write(url_site)

time.sleep(2) 
pyautogui.press("enter")

pyautogui.hotkey('win', 'up') # maximizar o navegador 

for _ in range(5):            # permite aperta tab 5 vezes
    pyautogui.press("tab") 

time.sleep(2) 

pyautogui.write("CPF")
pyautogui.press("tab")
pyautogui.write("SENHA")

pyautogui.press("enter")

pyautogui.click(957,950, duration=1.5)   # coordenada do OK 
pyautogui.click(551,636, duration=1.5)   # coordenada do enter 




















               

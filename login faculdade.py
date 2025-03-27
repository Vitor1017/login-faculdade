from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Inicializa o driver do Chrome
driver = webdriver.Chrome()

try:
    # Maximiza a janela do navegador
    driver.maximize_window()

    # Abre a página de login
    driver.get('https://www.colaboraread.com.br/login/auth')
    sleep(5)

    # Preenche o campo de usuário
    campo_usuario = driver.find_element(By.XPATH, "//input[@id='username']")
    campo_usuario.send_keys('**********') # só colocar seu usuario AVA
    sleep(2)

    # Preenche o campo de senha
    campo_senha = driver.find_element(By.XPATH, "//input[@name='password']")
    campo_senha.send_keys('************') # só colocar sua senha AVA
    sleep(2)

    # Clica no botão de login
    botao_login = driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-lg btn-block mb-10']")
    botao_login.click()
    sleep(5)  # Aguarda o carregamento da próxima página

    # Clica no botão do curso 
    botao_curso = driver.find_element(By.XPATH, "//button[@class='btn btn-primary entrar']")
    botao_curso.click()
    sleep(5)  # Aguarda o carregamento da próxima página

    # Mantém o navegador aberto até que o usuário pressione Enter
    input("Pressione Enter para fechar o navegador...")

except Exception as e:
    print(f"Ocorreu um erro: {e}")

finally:
    # Fecha o navegador
    driver.quit()




















               

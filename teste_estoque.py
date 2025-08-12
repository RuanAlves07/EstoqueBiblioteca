from selenium import webdriver
from selenium.webdriver.common.by import by 
import time

service = webdriver.ChromeService(executable_path="C:/Users/ruan_a_alves/Downloads/chrome-win64")
driver = webdriver.Chrome(service=service)

try:

    driver.get("C:/xampp/htdocs/php_RuanAlves/PHP/FormFront_Back/backendform.php")

    campo_nome = driver.find.element(By.ID, "id-do-campo-nome")
    campo_quantidade = driver.find.element(By.ID, "id-do-campo-quantidade")
    campo_preco = driver.find.element(By.ID, "id-do-campo-preco")
    botao_adicionar = driver.find.element(By.ID, "id-do-botao-adicionar")

    campo_nome.send_keys("Laptop Gamer")
    campo_quantidade.send_keys("5")
    campo_preco.send_keys("7500.00")

    botao_adicionar.click()
    time.sleep(2)

    tabela = driver.find_element(By.ID, "id-da-tabela")

    if "Laptop Gamer" in tabela.text and "5" in tabela.text and "7500.00" in tabela.text:
        print("💚 Teste de cadastro de produto: SUCESSO")
    else:
        print("❤️ Teste de cadastro de produto: FALHA!")
finally:

    driver.quit()
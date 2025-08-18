from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:
    driver.get("C:/xampp/htdocs/php_RuanAlves/PHP/FormFront_Back/backendform.php")

    # DEBUG: Check where we are
    print("URL:", driver.current_url)
    print("Title:", driver.title)
    driver.save_screenshot("debug_load.png")

    # Wait for body first
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    print("Page body loaded.")

    # Now wait for the specific element
    campo_nome = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "id-do-campo-nome"))
    )
    campo_quantidade = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "id-do-campo-quantidade"))
    )
    campo_preco = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "id-do-campo-preco"))
    )
    botao_adicionar = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID, "id-do-botao-adicionar"))
    )

    campo_nome.send_keys("Laptop Gamer")
    campo_quantidade.send_keys("5")
    campo_preco.send_keys("7500.00")
    botao_adicionar.click()

    tabela = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "id-da-tabela"))
    )

    if "Laptop Gamer" in tabela.text and "5" in tabela.text and "7500.00" in tabela.text:
        print("💚 Teste de cadastro de produto: SUCESSO")
    else:
        print("❤️ Teste de cadastro de produto: FALHA!")

finally:
    driver.quit()
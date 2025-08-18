from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    # ✅ Acesse via localhost, não via caminho de arquivo
    driver.get("http://localhost:8080/php_RuanAlves/PHP/FormFront_Back/produtos.php")

    # Espera o formulário carregar
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

    # Preenche os campos
    campo_nome.send_keys("Laptop Gamer")
    campo_quantidade.send_keys("5")
    campo_preco.send_keys("7500.00")

    # Clica no botão
    botao_adicionar.click()

    # Aqui, você pode querer verificar a tabela ou redirecionamento
    print("Formulário enviado com sucesso!")

finally:
    driver.quit()  # Fecha o navegador
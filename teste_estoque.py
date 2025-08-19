from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    
    driver.get("http://localhost:8080/php_RuanAlves/PHP/FormFront_Back/produtos.html")

    
    campo_nome = driver.find_element(By.ID, "nome")
    campo_descricao = driver.find_element(By.ID, "descricao")
    campo_categoria = driver.find_element(By.ID, "categoria")
    campo_quantidade = driver.find_element(By.ID, "quantidade")
    campo_preco = driver.find_element(By.ID, "preco")
    campo_fornecedor = driver.find_element(By.ID, "fornecedor")
    botao_adicionar = driver.find_element(By.ID, "Enviar")

    # Preenche os campos
    campo_nome.send_keys("Livro legal")
    campo_descricao.send_keys("Livro super massa")
    campo_categoria.send_keys("Juvenil")
    campo_quantidade.send_keys("5")
    campo_preco.send_keys("7500.00")
    campo_fornecedor.send_keys("Super legal")

    # Clica no botão
    botao_adicionar.click()
    time.sleep(2)

   # ✅ Obtém os valores dos campos após o preenchimento
    nome_valor = campo_nome.get_attribute("value")
    descricao_valor = campo_descricao.get_attribute("value")
    categoria_valor = campo_categoria.get_attribute("value")
    quantidade_valor = campo_quantidade.get_attribute("value")
    preco_valor = campo_preco.get_attribute("value")
    fornecedor_valor = campo_fornecedor.get_attribute("value")

    # ✅ Verifica se os valores estão corretos
    if (nome_valor == "Livro legal" and descricao_valor == "Livro super massa" and categoria_valor == "Juvenil" and quantidade_valor == "5" and preco_valor == "7500.00" and fornecedor_valor == "Super legal"):
        print("💚 Teste de cadastro de produto: SUCESSO!")
    else:
        print("❤️ Teste de cadastro de produto: FALHA!")

finally:
    driver.quit()
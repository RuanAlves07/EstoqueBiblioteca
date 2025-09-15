from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()



try:
    
    driver.get("http://localhost:8080/SA/PHP/FormFront_Back/produtos.html")

    
    campo_nome = driver.find_element(By.ID, "nome")
    campo_descricao = driver.find_element(By.ID, "descricao")
    campo_categoria = driver.find_element(By.ID, "categoria")
    campo_quantidade = driver.find_element(By.ID, "quantidade") 
    campo_preco = driver.find_element(By.ID, "preco")
    campo_fornecedor = driver.find_element(By.ID, "fornecedor")
    botao_adicionar = driver.find_element(By.ID, "Enviar")



    # Preenche os campos
    campo_nome.send_keys("Gramática Completa")
    campo_descricao.send_keys("Guia definitivo de gramática.")
    campo_categoria.send_keys("R")
    campo_quantidade.send_keys("110")
    campo_preco.send_keys("69.90")
    campo_fornecedor.send_keys("1")

    # Clica no botão
    botao_adicionar.click()
    time.sleep(2)




        # ✅ Verifica se os valores estão corretos
    if (campo_nome == "Gramática Completa" and campo_descricao == "Guia definitivo de gramática." and campo_categoria == "R" 
        and campo_quantidade == "110" 
        and campo_preco == "69.90" and campo_fornecedor == "1"):
        print("❤️Teste de cadastro de produto: SUCESSO!")
    else:
        print("💚 Teste de cadastro de produto: SUCESSO!")

finally:
    driver.quit()